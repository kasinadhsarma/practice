"""
==========================================================
  OOP IN PYTHON -- PART 5: ABSTRACTION
==========================================================
  1. Abstract Base Classes (ABC)
  2. @abstractmethod
  3. @abstractproperty / abstract @property
  4. Abstract class methods & static methods
  5. Interfaces (Python-style using ABC)
  6. Concrete class must implement all abstract methods
  7. Abstract class can have concrete methods too
  8. Registering virtual subclasses
  9. __subclasshook__ -- customising isinstance checks
  10. Protocol (structural subtyping -- Python 3.8+)
"""

from abc import ABC, abstractmethod, ABCMeta
from typing import Protocol, runtime_checkable

# ----------------------------------------------------------
# 1. ABSTRACT BASE CLASS -- ABC
# ----------------------------------------------------------
print("=== ABSTRACT BASE CLASS ===")

class Shape(ABC):               # inheriting ABC makes it abstract

    @abstractmethod
    def area(self) -> float:
        """Must be implemented by every concrete subclass."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    # Concrete method in abstract class -- shared logic
    def describe(self):
        return (f"{type(self).__name__}: "
                f"area={self.area():.4f}, "
                f"perimeter={self.perimeter():.4f}")

    def scale(self, factor):
        """Default scaling -- subclasses may override."""
        return f"{type(self).__name__} scaled by {factor}"

try:
    s = Shape()           # cannot instantiate abstract class!
except TypeError as e:
    print("Cannot instantiate:", e)

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

class Circle(Shape):
    import math
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.r

for s in [Rectangle(3,4), Circle(5)]:
    print(s.describe())

# ----------------------------------------------------------
# 2. ABSTRACT PROPERTY
# ----------------------------------------------------------
print("\n=== ABSTRACT PROPERTY ===")

class Vehicle(ABC):
    @property
    @abstractmethod
    def fuel_type(self) -> str:
        """Every vehicle must declare its fuel type."""
        pass

    @property
    @abstractmethod
    def max_speed(self) -> int:
        pass

    @abstractmethod
    def start(self):
        pass

    def info(self):
        return (f"{type(self).__name__}: "
                f"fuel={self.fuel_type}, max_speed={self.max_speed}km/h")

class Petrol_Car(Vehicle):
    @property
    def fuel_type(self): return "Petrol"

    @property
    def max_speed(self): return 200

    def start(self): return "Vroom!"

class ElectricCar(Vehicle):
    @property
    def fuel_type(self): return "Electric"

    @property
    def max_speed(self): return 250

    def start(self): return "Whirr..."

for v in [Petrol_Car(), ElectricCar()]:
    print(v.info(), "|", v.start())

# ----------------------------------------------------------
# 3. ABSTRACT CLASS METHODS & STATIC METHODS
# ----------------------------------------------------------
print("\n=== ABSTRACT CLASS & STATIC METHODS ===")

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data):
        pass

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Each processor must have a name."""
        pass

    @staticmethod
    @abstractmethod
    def validate(data) -> bool:
        """Each processor must validate its input."""
        pass

    # Concrete template method that uses abstract methods
    def run(self, data):
        if not self.validate(data):
            raise ValueError(f"Invalid data for {self.get_name()}")
        return self.process(data)

class CSVProcessor(DataProcessor):
    def process(self, data):
        return [row.split(',') for row in data.strip().split('\n')]

    @classmethod
    def get_name(cls): return "CSV Processor"

    @staticmethod
    def validate(data): return isinstance(data, str) and ',' in data

class JSONProcessor(DataProcessor):
    import json
    def process(self, data):
        import json
        return json.loads(data)

    @classmethod
    def get_name(cls): return "JSON Processor"

    @staticmethod
    def validate(data):
        import json
        try: json.loads(data); return True
        except: return False

csv = CSVProcessor()
print("CSV:", csv.run("a,b,c\n1,2,3"))

jsn = JSONProcessor()
print("JSON:", jsn.run('{"x": 1, "y": 2}'))

# ----------------------------------------------------------
# 4. INTERFACE-STYLE ABC (multiple abstract methods)
# ----------------------------------------------------------
print("\n=== INTERFACES (ABC-based) ===")

class Serializable(ABC):
    @abstractmethod
    def to_json(self) -> str: pass

    @abstractmethod
    def from_json(cls, data: str): pass

class Printable(ABC):
    @abstractmethod
    def print_info(self): pass

class Saveable(ABC):
    @abstractmethod
    def save(self, filepath: str): pass

    @abstractmethod
    def load(cls, filepath: str): pass

# Implementing multiple "interfaces"
import json

class User(Serializable, Printable):
    def __init__(self, name, email, age):
        self.name  = name
        self.email = email
        self.age   = age

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, data):
        d = json.loads(data)
        return cls(d['name'], d['email'], d['age'])

    def print_info(self):
        print(f"User: {self.name} <{self.email}>, age {self.age}")

u = User("Alice", "alice@example.com", 30)
u.print_info()
serialized = u.to_json()
print("Serialized:", serialized)
u2 = User.from_json(serialized)
u2.print_info()

# ----------------------------------------------------------
# 5. REGISTERING VIRTUAL SUBCLASSES
#    Tell ABC that a class is a subclass even without inheriting
# ----------------------------------------------------------
print("\n=== VIRTUAL SUBCLASS REGISTRATION ===")

class Drawable(ABC):
    @abstractmethod
    def draw(self): pass

class LegacyCircle:           # doesn't inherit Drawable
    def draw(self):
        return "Legacy circle drawn"

Drawable.register(LegacyCircle)   # register as virtual subclass

lc = LegacyCircle()
print("isinstance(lc, Drawable):", isinstance(lc, Drawable))   # True
print(lc.draw())

# ----------------------------------------------------------
# 6. __subclasshook__ -- CUSTOM isinstance BEHAVIOR
# ----------------------------------------------------------
print("\n=== __subclasshook__ ===")

class Quackable(ABC):
    @abstractmethod
    def quack(self): pass

    @classmethod
    def __subclasshook__(cls, C):
        # Any class with a 'quack' method is considered a Quackable
        if cls is Quackable:
            if any("quack" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented

class Duck:
    def quack(self): return "Quack!"

class Person:
    def quack(self): return "I'm quacking like a duck!"

class Cat:
    def meow(self): return "Meow"

print("Duck is Quackable:", isinstance(Duck(), Quackable))    # True
print("Person is Quackable:", isinstance(Person(), Quackable))  # True
print("Cat is Quackable:", isinstance(Cat(), Quackable))      # False

# ----------------------------------------------------------
# 7. PROTOCOL -- Structural Subtyping (Python 3.8+)
#    Like interfaces but checked structurally, not nominally
# ----------------------------------------------------------
print("\n=== PROTOCOL ===")

@runtime_checkable
class Drawable2(Protocol):
    def draw(self) -> str: ...
    def resize(self, factor: float) -> None: ...

class Square:
    def __init__(self, side): self.side = side
    def draw(self): return f"Square({self.side})"
    def resize(self, factor): self.side *= factor

class Triangle2:
    def __init__(self, base): self.base = base
    def draw(self): return f"Triangle({self.base})"
    def resize(self, factor): self.base *= factor

class Text:
    def render(self): return "text"   # different method name!

sq = Square(5)
tr = Triangle2(3)
tx = Text()

print("Square is Drawable2:", isinstance(sq, Drawable2))    # True
print("Triangle is Drawable2:", isinstance(tr, Drawable2))  # True
print("Text is Drawable2:", isinstance(tx, Drawable2))      # False

# Works with any object that has draw() and resize()
def render(d: Drawable2):
    d.resize(2)
    return d.draw()

print(render(sq))   # Square(10)
print(render(tr))   # Triangle(6)

print("\n[Y] Abstraction done!")
