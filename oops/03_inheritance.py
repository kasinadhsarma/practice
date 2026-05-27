"""
==========================================================
  OOP IN PYTHON -- PART 3: INHERITANCE
==========================================================
  1. Single Inheritance
  2. Multi-level Inheritance
  3. Hierarchical Inheritance
  4. Multiple Inheritance
  5. Hybrid Inheritance
  6. super() -- calling parent methods
  7. MRO (Method Resolution Order) -- C3 Linearization
  8. Diamond Problem & its resolution
  9. isinstance() and issubclass()
  10. Overriding __init__ properly
  11. Mixin classes
"""

# ----------------------------------------------------------
# 1. SINGLE INHERITANCE
#    Child IS-A Parent (one parent)
# ----------------------------------------------------------
print("=== SINGLE INHERITANCE ===")

class Animal:
    def __init__(self, name, sound):
        self.name  = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def breathe(self):
        return f"{self.name} breathes"

class Dog(Animal):              # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Woof")    # call parent __init__
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball!"

    # Override parent method
    def speak(self):
        return f"{self.name} ({self.breed}) barks: Woof Woof!"

d = Dog("Rex", "German Shepherd")
print(d.speak())             # overridden
print(d.breathe())           # inherited
print(d.fetch())             # own method
print(d.name, d.sound, d.breed)

# ----------------------------------------------------------
# 2. MULTI-LEVEL INHERITANCE
#    A -> B -> C  (chain)
# ----------------------------------------------------------
print("\n=== MULTI-LEVEL INHERITANCE ===")

class LivingThing:
    def __init__(self, name):
        self.name = name

    def live(self):
        return f"{self.name} is alive"

class Animal2(LivingThing):
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs

    def move(self):
        return f"{self.name} moves with {self.legs} legs"

class Cat(Animal2):
    def __init__(self, name, indoor):
        super().__init__(name, 4)
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs..."

cat = Cat("Whiskers", True)
print(cat.live())     # from LivingThing
print(cat.move())     # from Animal2
print(cat.purr())     # from Cat

# ----------------------------------------------------------
# 3. HIERARCHICAL INHERITANCE
#    One parent, multiple children
# ----------------------------------------------------------
print("\n=== HIERARCHICAL INHERITANCE ===")

class Shape:
    def __init__(self, color="white"):
        self.color = color

    def area(self):
        raise NotImplementedError

    def describe(self):
        return f"A {self.color} shape with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, w, h, color="blue"):
        super().__init__(color)
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

class Triangle(Shape):
    def __init__(self, base, height, color="red"):
        super().__init__(color)
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height

class Circle2(Shape):
    import math
    def __init__(self, r, color="green"):
        super().__init__(color)
        self.r = r

    def area(self):
        import math
        return math.pi * self.r ** 2

shapes = [Rectangle(4,5), Triangle(3,6), Circle2(7)]
for s in shapes:
    print(s.describe())

# ----------------------------------------------------------
# 4. MULTIPLE INHERITANCE
#    Class inherits from TWO or more parents
# ----------------------------------------------------------
print("\n=== MULTIPLE INHERITANCE ===")

class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying"

    def altitude(self):
        return "High altitude"

class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming"

    def depth(self):
        return "Deep water"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        Animal.__init__(self, name, "Quack")

    def speak(self):
        return f"{self.name} says Quack!"

donald = Duck("Donald")
print(donald.speak())
print(donald.fly())
print(donald.swim())
print(donald.breathe())

# ----------------------------------------------------------
# 5. DIAMOND PROBLEM & MRO
# ----------------------------------------------------------
print("\n=== DIAMOND PROBLEM & MRO ===")

#        Base
#       /    \
#    Left    Right
#       \    /
#       Child

class Base:
    def greet(self):
        return "Hello from Base"

class Left(Base):
    def greet(self):
        return "Hello from Left -> " + super().greet()

class Right(Base):
    def greet(self):
        return "Hello from Right -> " + super().greet()

class Child(Left, Right):
    def greet(self):
        return "Hello from Child -> " + super().greet()

c = Child()
print(c.greet())
# Child -> Left -> Right -> Base  (C3 Linearization)

# MRO -- Method Resolution Order
print("MRO:", [cls.__name__ for cls in Child.__mro__])
# [Child, Left, Right, Base, object]

# ----------------------------------------------------------
# 6. super() IN DETAIL
# ----------------------------------------------------------
print("\n=== super() ===")

class Vehicle:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year

    def info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors=4):
        super().__init__(make, model, year)   # call Vehicle.__init__
        self.doors = doors

    def info(self):
        return super().info() + f" [{self.doors} doors]"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kwh):
        super().__init__(make, model, year)   # calls Car.__init__
        self.battery = battery_kwh

    def info(self):
        return super().info() + f" [Electric {self.battery}kWh]"

ec = ElectricCar("Tesla", "Model S", 2024, 100)
print(ec.info())

# ----------------------------------------------------------
# 7. isinstance & issubclass
# ----------------------------------------------------------
print("\n=== isinstance & issubclass ===")

print("isinstance(ec, ElectricCar):", isinstance(ec, ElectricCar))   # True
print("isinstance(ec, Car):", isinstance(ec, Car))                   # True
print("isinstance(ec, Vehicle):", isinstance(ec, Vehicle))           # True
print("isinstance(ec, object):", isinstance(ec, object))             # True (always)
print("isinstance(ec, Duck):", isinstance(ec, Duck))                 # False

print("issubclass(ElectricCar, Car):", issubclass(ElectricCar, Car))       # True
print("issubclass(ElectricCar, Vehicle):", issubclass(ElectricCar, Vehicle)) # True
print("issubclass(Car, ElectricCar):", issubclass(Car, ElectricCar))       # False

# ----------------------------------------------------------
# 8. MIXIN CLASSES
#    Provide reusable behaviors without being standalone
# ----------------------------------------------------------
print("\n=== MIXIN CLASSES ===")

class LogMixin:
    """Adds logging capability to any class."""
    def log(self, message):
        print(f"[LOG] {self.__class__.__name__}: {message}")

class SerializeMixin:
    """Adds JSON-like serialization."""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}

    def to_string(self):
        return str(self.to_dict())

class CompareMixin:
    """Adds comparison based on a 'key' attribute."""
    def __eq__(self, other):
        return self.key == other.key

    def __lt__(self, other):
        return self.key < other.key

class Product(LogMixin, SerializeMixin):
    def __init__(self, name, price):
        self.name  = name
        self.price = price
        self.key   = price    # for CompareMixin if used

    def discount(self, pct):
        self.price *= (1 - pct/100)
        self.log(f"Price discounted by {pct}%, new price: {self.price:.2f}")

p = Product("Laptop", 999.99)
p.discount(10)
print("Dict:", p.to_dict())
print("String:", p.to_string())
p.log("Product processed")

# ----------------------------------------------------------
# 9. PREVENTING INHERITANCE -- final-like behavior
# ----------------------------------------------------------
print("\n=== PREVENTING INHERITANCE ===")

class Final:
    def __init_subclass__(cls, **kwargs):
        raise TypeError(f"Class {cls.__name__} cannot inherit from Final")

try:
    class Attempt(Final):
        pass
except TypeError as e:
    print("Caught:", e)

print("\n[Y] Inheritance done!")
