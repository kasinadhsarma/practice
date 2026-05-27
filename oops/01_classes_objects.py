"""
==========================================================
  OOP IN PYTHON -- PART 1: CLASSES & OBJECTS
==========================================================
  1. Class definition & instantiation
  2. Instance variables vs Class variables
  3. Instance methods
  4. __init__ constructor
  5. __del__ destructor
  6. __new__ (object creation hook)
  7. __str__ and __repr__
  8. Passing objects as arguments
  9. Returning objects from functions
  10. Object identity, equality, type checks
"""

# ----------------------------------------------------------
# 1. CLASS DEFINITION & INSTANTIATION
# ----------------------------------------------------------
class Dog:
    # Class variable -- shared by ALL instances
    species = "Canis lupus familiaris"
    count   = 0

    # Constructor -- called when object is created
    def __init__(self, name, age, breed):
        # Instance variables -- unique to each instance
        self.name  = name
        self.age   = age
        self.breed = breed
        Dog.count += 1          # increment class variable

    # Instance method -- first param is always 'self'
    def bark(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    # Destructor -- called when object is garbage collected
    def __del__(self):
        Dog.count -= 1
        # print(f"{self.name} has been deleted")  # uncomment to see

    # __str__  -- human-readable string (used by print())
    def __str__(self):
        return f"Dog: {self.name} ({self.breed}, {self.age}yr)"

    # __repr__ -- unambiguous developer string (used in REPL)
    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age}, breed={self.breed!r})"


# Instantiation
d1 = Dog("Rex",   3, "German Shepherd")
d2 = Dog("Buddy", 5, "Golden Retriever")
d3 = Dog("Max",   2, "Labrador")

print("=== CLASS & OBJECTS ===")
print(d1)                    # calls __str__
print(repr(d2))              # calls __repr__
print(d1.bark())
print(d1.info())

# ----------------------------------------------------------
# 2. CLASS VARIABLE vs INSTANCE VARIABLE
# ----------------------------------------------------------
print("\n=== CLASS vs INSTANCE VARIABLES ===")
print("Species (class var):", Dog.species)
print("Dog count:", Dog.count)           # 3

# Instance variable shadows class variable
d1.species = "Wolf-Dog"                  # creates INSTANCE copy
print("d1.species:", d1.species)         # Wolf-Dog (instance copy)
print("d2.species:", d2.species)         # Canis lupus... (class var)
print("Dog.species:", Dog.species)       # unchanged

# ----------------------------------------------------------
# 3. __new__ -- OBJECT CREATION (before __init__)
# ----------------------------------------------------------
print("\n=== __new__ ===")

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        else:
            print("Reusing existing instance")
        return cls._instance

    def __init__(self, value):
        self.value = value

s1 = Singleton(10)
s2 = Singleton(20)
print("Same object?", s1 is s2)    # True
print("s1.value:", s1.value)        # 20 (overwritten by second __init__)

# ----------------------------------------------------------
# 4. PASSING OBJECTS & RETURNING OBJECTS
# ----------------------------------------------------------
print("\n=== PASSING & RETURNING OBJECTS ===")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):       # passing object as argument
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5

    def translate(self, dx, dy):        # returning a new object
        return Point(self.x + dx, self.y + dy)

    def midpoint(self, other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2)

p1 = Point(0, 0)
p2 = Point(3, 4)
print("Distance:", p1.distance_to(p2))    # 5.0
print("Translate p1 by (2,3):", p1.translate(2, 3))
print("Midpoint:", p1.midpoint(p2))

# ----------------------------------------------------------
# 5. OBJECT IDENTITY, EQUALITY, TYPE CHECKS
# ----------------------------------------------------------
print("\n=== IDENTITY & TYPE CHECKS ===")

a = Dog("Alpha", 1, "Poodle")
b = a                          # same object (alias)
c = Dog("Alpha", 1, "Poodle") # different object, same values

print("a is b:", a is b)       # True  -- identity
print("a is c:", a is c)       # False -- different objects
print("type(a):", type(a))
print("isinstance(a, Dog):", isinstance(a, Dog))     # True
print("isinstance(a, object):", isinstance(a, object))  # True (every class inherits object)
print("issubclass(Dog, object):", issubclass(Dog, object))

# dir() -- list all attributes and methods
print("\nAttributes of Dog instance:")
attrs = [x for x in dir(a) if not x.startswith('__')]
print(attrs)

# hasattr / getattr / setattr / delattr
print("\nhasattr(a, 'name'):", hasattr(a, 'name'))
print("getattr(a, 'age'):", getattr(a, 'age'))
setattr(a, 'color', 'brown')
print("setattr color:", a.color)
delattr(a, 'color')
print("After delattr, hasattr color:", hasattr(a, 'color'))

# ----------------------------------------------------------
# 6. OBJECT __dict__
# ----------------------------------------------------------
print("\n=== __dict__ ===")
print("Instance __dict__:", d1.__dict__)
print("Class __dict__ keys:", list(Dog.__dict__.keys()))

# ----------------------------------------------------------
# 7. CLASS WITH DEFAULT ARGUMENTS & *args / **kwargs
# ----------------------------------------------------------
print("\n=== FLEXIBLE CONSTRUCTORS ===")

class Config:
    def __init__(self, host="localhost", port=8080, **options):
        self.host    = host
        self.port    = port
        self.options = options

    def __str__(self):
        return f"Config(host={self.host}, port={self.port}, opts={self.options})"

c1 = Config()
c2 = Config("192.168.1.1", 443, debug=True, timeout=30)
print(c1)
print(c2)

# ----------------------------------------------------------
# 8. NESTED CLASSES
# ----------------------------------------------------------
print("\n=== NESTED CLASS ===")

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    class Department:
        def __init__(self, name, head):
            self.name = name
            self.head = head

        def __str__(self):
            return f"Dept({self.name}, head={self.head})"

    def add_dept(self, name, head):
        dept = University.Department(name, head)
        self.departments.append(dept)
        return dept

u = University("MIT")
dept = u.add_dept("CS", "Prof. Smith")
print(u.name, "->", dept)

print("\n[Y] Classes & Objects done!")
