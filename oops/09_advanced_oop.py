"""
==========================================================
  OOP IN PYTHON -- PART 9: ADVANCED OOP
==========================================================
  1. Descriptors (__get__, __set__, __delete__)
  2. __slots__ -- memory optimisation
  3. Metaclasses (__metaclass__, type, custom meta)
  4. Class decorators
  5. __init_subclass__
  6. __set_name__
  7. dataclasses (@dataclass)
  8. NamedTuple
  9. Iterator Protocol (__iter__, __next__)
  10. Generator class
"""

import sys
from dataclasses import dataclass, field, asdict, astuple
from typing import ClassVar, List
from collections import namedtuple

# ----------------------------------------------------------
# 1. DESCRIPTORS
#    Objects that define __get__, __set__, or __delete__
#    Used by properties, classmethod, staticmethod internally
# ----------------------------------------------------------
print("=== DESCRIPTORS ===")

class TypedField:
    """Descriptor that enforces type + optional range."""
    def __init__(self, expected_type, min_val=None, max_val=None):
        self.expected_type = expected_type
        self.min_val = min_val
        self.max_val = max_val
        self.name = None    # set by __set_name__

    def __set_name__(self, owner, name):
        """Called when the class is created -- sets attribute name."""
        self.name = name
        self.storage_name = '_' + name

    def __get__(self, obj, objtype=None):
        if obj is None: return self   # accessed on class
        return getattr(obj, self.storage_name, None)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}, "
                            f"got {type(value).__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}")
        setattr(obj, self.storage_name, value)

    def __delete__(self, obj):
        delattr(obj, self.storage_name)


class Product:
    name   = TypedField(str)
    price  = TypedField(float, min_val=0.0)
    stock  = TypedField(int, min_val=0, max_val=10000)

    def __init__(self, name, price, stock):
        self.name  = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product({self.name}, ${self.price}, stock={self.stock})"

p = Product("Laptop", 999.99, 50)
print(p)

try: p.price = "free"
except TypeError as e: print("TypeError:", e)

try: p.price = -10.0
except ValueError as e: print("ValueError:", e)

try: p.stock = 99999
except ValueError as e: print("ValueError:", e)

# Non-data descriptor (only __get__)
class ClassLogger:
    def __get__(self, obj, objtype=None):
        name = objtype.__name__ if objtype else type(obj).__name__
        import logging
        logger = logging.getLogger(name)
        return logger

class Service:
    logger = ClassLogger()

# Service.logger  # returns a Logger named "Service"
print("Logger name:", Service.logger.name)

# ----------------------------------------------------------
# 2. __slots__ -- MEMORY OPTIMISATION
# ----------------------------------------------------------
print("\n=== __slots__ ===")

class NormalPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ('x', 'y')   # no __dict__, no __weakref__

    def __init__(self, x, y):
        self.x = x
        self.y = y

np = NormalPoint(1, 2)
sp = SlottedPoint(1, 2)

print(f"Normal  __dict__: {np.__dict__}")
print(f"Slotted has __dict__: {hasattr(sp, '__dict__')}")  # False

# Memory comparison
normal_objs  = [NormalPoint(i, i) for i in range(1000)]
slotted_objs = [SlottedPoint(i, i) for i in range(1000)]
print(f"Normal size: {sys.getsizeof(np)} bytes")
print(f"Slotted size: {sys.getsizeof(sp)} bytes")

# Slots prevent adding extra attributes
try:
    sp.z = 3
except AttributeError as e:
    print("Cannot add attribute to slotted:", e)

# Slots with inheritance
class Base:
    __slots__ = ('x',)
    def __init__(self, x): self.x = x

class Derived(Base):
    __slots__ = ('y',)
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

d = Derived(1, 2)
print("Derived slotted:", d.x, d.y)

# ----------------------------------------------------------
# 3. METACLASSES
# ----------------------------------------------------------
print("\n=== METACLASSES ===")

# type IS the metaclass of all classes
print("type(int):", type(int))          # <class 'type'>
print("type(str):", type(str))          # <class 'type'>

# Creating a class dynamically with type
DynClass = type('DynClass', (object,), {
    'x': 10,
    'greet': lambda self: f"Hello from {self.__class__.__name__}"
})
obj = DynClass()
print("Dynamic class:", obj.greet(), "x =", obj.x)

# Custom Metaclass -- validates class definition
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self, debug=False):
        self.debug = debug

c1 = Config(True)
c2 = Config(False)
print("Singleton:", c1 is c2)   # True -- same object

# Metaclass that auto-registers subclasses
class PluginMeta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        if bases:   # don't register the base class itself
            mcs.registry[name] = cls
        return cls

class Plugin(metaclass=PluginMeta):
    def run(self): raise NotImplementedError

class CSVPlugin(Plugin):
    def run(self): return "Processing CSV"

class JSONPlugin(Plugin):
    def run(self): return "Processing JSON"

print("Registered plugins:", list(PluginMeta.registry.keys()))
# Run all plugins
for name, cls in PluginMeta.registry.items():
    print(f"  {name}: {cls().run()}")

# ----------------------------------------------------------
# 4. CLASS DECORATORS
# ----------------------------------------------------------
print("\n=== CLASS DECORATORS ===")

def singleton(cls):
    """Class decorator to make any class a singleton."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

def validate_init(cls):
    """Class decorator that adds type checking to __init__."""
    original_init = cls.__init__
    import inspect
    hints = {}
    try:
        hints = original_init.__annotations__
    except AttributeError:
        pass

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        for attr, expected_type in hints.items():
            if attr == 'return': continue
            val = getattr(self, attr, None)
            if val is not None and not isinstance(val, expected_type):
                raise TypeError(f"{attr} should be {expected_type.__name__}")
    cls.__init__ = new_init
    return cls

@singleton
class DatabaseConnection:
    def __init__(self, url="localhost"):
        self.url = url
        print(f"Connecting to {url}")

db1 = DatabaseConnection("db1.example.com")
db2 = DatabaseConnection("db2.example.com")  # ignored -- db1 returned
print("Same instance:", db1 is db2)

# ----------------------------------------------------------
# 5. __init_subclass__ -- hook when subclass is created
# ----------------------------------------------------------
print("\n=== __init_subclass__ ===")

class PluginBase:
    _subclasses = []

    def __init_subclass__(cls, required_method=None, **kwargs):
        super().__init_subclass__(**kwargs)
        PluginBase._subclasses.append(cls)
        if required_method and not hasattr(cls, required_method):
            raise TypeError(f"{cls.__name__} must implement {required_method}()")

class AlphaPlugin(PluginBase, required_method='execute'):
    def execute(self): return "Alpha running"

class BetaPlugin(PluginBase, required_method='execute'):
    def execute(self): return "Beta running"

try:
    class BrokenPlugin(PluginBase, required_method='execute'):
        pass  # missing execute!
except TypeError as e:
    print("Caught:", e)

print("Registered:", [c.__name__ for c in PluginBase._subclasses])

# ----------------------------------------------------------
# 6. DATACLASSES
# ----------------------------------------------------------
print("\n=== DATACLASSES ===")

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0   # default value

    def distance(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5

@dataclass(order=True, frozen=True)    # frozen = immutable
class Color:
    red:   int = field(compare=True)
    green: int = field(compare=True)
    blue:  int = field(compare=True)
    name:  str = field(default="", compare=False, repr=True)

    def __post_init__(self):
        for attr in ['red', 'green', 'blue']:
            val = getattr(self, attr)
            if not 0 <= val <= 255:
                raise ValueError(f"{attr} must be 0-255")

@dataclass
class Inventory:
    items:   List[str] = field(default_factory=list)
    counter: ClassVar[int] = 0   # ClassVar -- not in __init__

    def add(self, item):
        self.items.append(item)
        Inventory.counter += 1

p1 = Point(3, 4)
p2 = Point(1, 2, 3)
print(p1, "distance:", p1.distance())
print(p1 == Point(3, 4, 0))   # True

c1 = Color(255, 0, 0, "Red")
c2 = Color(0, 255, 0, "Green")
print(c1, "<", c2, ":", c1 < c2)   # compare by r,g,b tuple
print("Dict:", asdict(c1))
print("Tuple:", astuple(p1))

inv = Inventory()
inv.add("Apple"); inv.add("Banana")
print(inv)

try:
    Color(300, 0, 0)
except ValueError as e:
    print("Frozen/validated:", e)

# ----------------------------------------------------------
# 7. NAMEDTUPLE
# ----------------------------------------------------------
print("\n=== NAMEDTUPLE ===")

# Classic namedtuple
Employee = namedtuple('Employee', ['name', 'dept', 'salary'])
e = Employee("Alice", "Engineering", 90000)
print(e)
print("Name:", e.name, "Salary:", e.salary)
print("As dict:", e._asdict())

# Typed NamedTuple
from typing import NamedTuple

class Vector3D(NamedTuple):
    x: float
    y: float
    z: float = 0.0

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

v = Vector3D(1, 2, 3)
print("Vector:", v, "magnitude:", round(v.magnitude(), 4))
print("Immutable -- try v.x=5:", end=" ")
try: v.x = 5
except AttributeError as e: print(e)

# ----------------------------------------------------------
# 8. ITERATOR PROTOCOL
# ----------------------------------------------------------
print("\n=== ITERATOR PROTOCOL ===")

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):    # makes it ITERABLE -- returns iterator
        return CountdownIterator(self.start)

class CountdownIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):    # makes it an ITERATOR too
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for n in Countdown(5):
    print(n, end=" ")
print()

# Combined iterable+iterator in one class
class Range2:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop  = stop
        self.step  = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += self.step
        return val

    def __len__(self):
        return max(0, (self.stop - self.start + self.step - 1) // self.step)

r = Range2(0, 10, 2)
print(list(r))   # [0,2,4,6,8]
print(list(r))   # iterates again because __iter__ resets current

# Generator class using __iter__ + yield
class FibonacciSeq:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        a, b = 0, 1
        while a <= self.limit:
            yield a
            a, b = b, a + b

print("Fibonacci <= 100:", list(FibonacciSeq(100)))

print("\n[Y] Advanced OOP done!")
