# Complete OOP in Python — Full Reference

11 files covering **every Object-Oriented Programming concept** from basics to advanced patterns.

---

## File Map

| File | Core Topics |
|------|-------------|
| `01_classes_objects.py` | Class definition, instantiation, instance vs class vars, `__init__`, `__del__`, `__new__`, `__str__`, `__repr__`, `__dict__`, nested classes, `hasattr/getattr/setattr/delattr` |
| `02_encapsulation.py` | Public / Protected / Private, name mangling, manual getters/setters, `@property`, `@setter`, `@deleter`, read-only, write-only, computed properties, Bank Account |
| `03_inheritance.py` | Single, Multi-level, Hierarchical, Multiple, Hybrid; `super()`, MRO (C3), Diamond problem, `isinstance`, `issubclass`, Mixin classes, `__init_subclass__` |
| `04_polymorphism.py` | Method overriding, method overloading (Python style), Duck typing, ALL operator overloading (`__add__`,`__mul__`,`__matmul__`,`__lt__`, etc.), `@singledispatch` |
| `05_abstraction.py` | `ABC`, `@abstractmethod`, abstract properties, abstract classmethods, Interface-style ABCs, virtual subclass registration, `__subclasshook__`, `Protocol` |
| `06_magic_methods.py` | All dunder groups: Representation, Numeric ops, Comparison, Container (`__len__`,`__getitem__`,`__setitem__`,`__delitem__`,`__iter__`,`__next__`), Context Manager, `__call__`, Attribute access, `__copy__`/`__deepcopy__` |
| `07_class_static_methods_properties.py` | `@classmethod`, `@staticmethod`, instance methods, alternative constructors, factory methods, `@cached_property`, method type decision guide |
| `08_composition_aggregation.py` | Association, Dependency, Aggregation, Composition, Composition vs Inheritance, Favour Composition, Strategy via Composition, swappable runtime behaviour |
| `09_advanced_oop.py` | Descriptors (`__get__`,`__set__`,`__delete__`,`__set_name__`), `__slots__`, Metaclasses (`type`, custom meta, `PluginMeta`), class decorators, `@dataclass`, `NamedTuple`, Iterator protocol, Generator class |
| `10_design_patterns.py` | **Creational**: Singleton, Factory, Abstract Factory, Builder, Prototype. **Structural**: Adapter, Decorator, Facade, Proxy, Composite. **Behavioural**: Observer, Strategy, Template Method, Command, Iterator |
| `11_solid_principles.py` | S-SRP, O-OCP, L-LSP, I-ISP, D-DIP — each with BAD example and GOOD refactored solution |

---

## OOP Concept Map

```
OOP
|
+-- CLASSES & OBJECTS
|     Class definition, instantiation
|     Instance vs Class variables
|     __init__, __del__, __new__
|     __str__, __repr__, __dict__
|     Nested classes
|
+-- ENCAPSULATION
|     Public   (name)
|     Protected (_name)  -- convention
|     Private  (__name) -- name mangling -> _Class__name
|     @property / @setter / @deleter
|     @cached_property
|
+-- INHERITANCE
|     Single        A -> B
|     Multi-level   A -> B -> C
|     Hierarchical  A -> B, A -> C
|     Multiple      B,C -> D
|     Hybrid        combination
|     MRO (C3 Linearization)
|     super() -- cooperative calls
|     Diamond Problem
|     Mixin classes
|
+-- POLYMORPHISM
|     Method Overriding    (runtime)
|     Method Overloading   (default args / *args)
|     Duck Typing
|     Operator Overloading (__add__, __eq__, ...)
|     @singledispatch
|
+-- ABSTRACTION
|     Abstract Base Class (ABC)
|     @abstractmethod
|     Abstract @property
|     Abstract @classmethod / @staticmethod
|     Interface style (multiple ABCs)
|     Protocol (structural typing)
|
+-- METHOD TYPES
|     Instance method  -- self
|     Class method     -- cls (@classmethod)
|     Static method    -- none (@staticmethod)
|
+-- MAGIC / DUNDER METHODS
|     __str__, __repr__, __format__, __bytes__
|     __add__, __sub__, __mul__, __truediv__, ...
|     __eq__, __ne__, __lt__, __le__, __gt__, __ge__
|     __len__, __getitem__, __setitem__, __delitem__
|     __contains__, __iter__, __next__, __reversed__
|     __enter__, __exit__  (context manager)
|     __call__             (callable objects)
|     __getattr__, __setattr__, __delattr__
|     __hash__, __bool__, __int__, __float__
|     __copy__, __deepcopy__
|     __new__, __init__, __del__
|
+-- RELATIONSHIPS
|     Association   -- A uses B
|     Dependency    -- A uses B temporarily
|     Aggregation   -- A HAS-A B (B survives)
|     Composition   -- A HAS-A B (B owned by A)
|
+-- ADVANCED
|     Descriptors  (__get__, __set__, __delete__, __set_name__)
|     __slots__    -- memory optimisation
|     Metaclasses  -- class of a class (type)
|     @dataclass   -- auto-generated boilerplate
|     NamedTuple   -- immutable records
|     Iterator Protocol (__iter__ + __next__)
|     Generator classes (yield in __iter__)
|
+-- DESIGN PATTERNS
|     Creational:  Singleton, Factory, Abstract Factory, Builder, Prototype
|     Structural:  Adapter, Decorator, Facade, Proxy, Composite
|     Behavioural: Observer, Strategy, Template, Command, Iterator
|
+-- SOLID PRINCIPLES
      S -- Single Responsibility
      O -- Open / Closed
      L -- Liskov Substitution
      I -- Interface Segregation
      D -- Dependency Inversion
```

---

## Quick Reference

### Access Modifiers
```python
self.name   = x    # Public    -- anyone
self._name  = x    # Protected -- by convention (internal)
self.__name = x    # Private   -- name-mangled to _Class__name
```

### Method Types
```python
class Foo:
    def instance(self):        ...  # access instance state
    @classmethod
    def class_m(cls):          ...  # access class state / alt constructors
    @staticmethod
    def static():              ...  # utility -- no state needed
```

### Property
```python
@property
def x(self): return self._x      # getter

@x.setter
def x(self, v): self._x = v      # setter

@x.deleter
def x(self): del self._x         # deleter
```

### MRO
```python
print(ClassName.__mro__)          # tuple of classes in resolution order
# C3: left-to-right, depth-first, never revisit
```

### Abstract Class
```python
from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def method(self): ...          # subclasses MUST implement
```

### Dataclass
```python
@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float = 0.0
```

### Context Manager
```python
class Ctx:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False    # False = don't suppress exceptions
```

### SOLID One-liners
```
S: One class = one responsibility = one reason to change
O: Add new classes to extend; never edit existing code
L: Subclass must honour ALL contracts of the base class
I: Many small interfaces > one fat interface
D: Import abstractions (ABC/Protocol), inject concrete via constructor
```
