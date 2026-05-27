"""
==========================================================
  OOP IN PYTHON -- PART 4: POLYMORPHISM
==========================================================
  1. Method Overriding (runtime polymorphism)
  2. Method Overloading (Python approach -- default args)
  3. Duck Typing
  4. Operator Overloading (all arithmetic, comparison, etc.)
  5. Function Polymorphism (built-ins working on many types)
  6. Parametric Polymorphism (generics-like)
  7. @singledispatch (type-based dispatch)
"""

from functools import singledispatch

# ----------------------------------------------------------
# 1. METHOD OVERRIDING -- Runtime Polymorphism
#    Same interface, different implementations
# ----------------------------------------------------------
print("=== METHOD OVERRIDING ===")

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        # This calls the overridden version at runtime
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

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

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

    def perimeter(self):
        return self.a + self.b + self.c

# Polymorphic usage -- same function call, different behavior
shapes = [Rectangle(4, 5), Circle(7), Triangle(3, 4, 5)]
for s in shapes:
    print(s.describe())

# ----------------------------------------------------------
# 2. METHOD OVERLOADING -- Python style
#    Python doesn't support true overloading; use defaults
# ----------------------------------------------------------
print("\n=== METHOD OVERLOADING (Python style) ===")

class Calculator:
    def add(self, a, b=0, c=0):
        """Works with 1, 2, or 3 arguments."""
        return a + b + c

    def multiply(self, *args):
        """Works with any number of arguments."""
        result = 1
        for v in args:
            result *= v
        return result

    def power(self, base, exp=2):
        return base ** exp

calc = Calculator()
print("add(5):", calc.add(5))           # 5
print("add(3,4):", calc.add(3, 4))     # 7
print("add(1,2,3):", calc.add(1,2,3)) # 6
print("multiply(2,3,4):", calc.multiply(2,3,4))
print("power(3):", calc.power(3))      # 9 (exp defaults to 2)
print("power(2,10):", calc.power(2,10)) # 1024

# ----------------------------------------------------------
# 3. DUCK TYPING
#    "If it walks like a duck and quacks like a duck, it is a duck"
#    Python doesn't check type -- checks behavior (methods)
# ----------------------------------------------------------
print("\n=== DUCK TYPING ===")

class Dog:
    def sound(self): return "Woof"
    def move(self): return "run"

class Cat:
    def sound(self): return "Meow"
    def move(self): return "slink"

class Robot:
    def sound(self): return "Beep"
    def move(self): return "roll"

class Fish:
    def sound(self): return "..."
    def move(self): return "swim"

# This function works on ANY object that has .sound() and .move()
def describe_creature(creature):
    print(f"Sound: {creature.sound()}, Moves: {creature.move()}")

for c in [Dog(), Cat(), Robot(), Fish()]:
    describe_creature(c)

# ----------------------------------------------------------
# 4. OPERATOR OVERLOADING
#    Define behavior of Python operators for custom classes
# ----------------------------------------------------------
print("\n=== OPERATOR OVERLOADING ===")

class Vector:
    def __init__(self, x, y, z=0):
        self.x, self.y, self.z = x, y, z

    # Arithmetic operators
    def __add__(self, other):           # self + other
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):           # self - other
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, scalar):          # self * scalar  (scalar mult)
        return Vector(self.x*scalar, self.y*scalar, self.z*scalar)

    def __rmul__(self, scalar):         # scalar * self
        return self.__mul__(scalar)

    def __truediv__(self, scalar):      # self / scalar
        return Vector(self.x/scalar, self.y/scalar, self.z/scalar)

    def __neg__(self):                  # -self (unary)
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self):                  # abs(self) -- magnitude
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    # Comparison operators
    def __eq__(self, other):            # self == other
        return self.x==other.x and self.y==other.y and self.z==other.z

    def __ne__(self, other):            # self != other
        return not self.__eq__(other)

    def __lt__(self, other):            # self < other (by magnitude)
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    # Augmented assignment
    def __iadd__(self, other):          # self += other
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    # Dot product using @
    def __matmul__(self, other):        # self @ other
        return self.x*other.x + self.y*other.y + self.z*other.z

    # Container-like
    def __len__(self):                  # len(self) -- dimension
        return 3

    def __getitem__(self, idx):         # self[idx]
        return (self.x, self.y, self.z)[idx]

    def __iter__(self):                 # for v in self
        yield self.x; yield self.y; yield self.z

    # Representations
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __hash__(self):                 # needed if __eq__ defined
        return hash((self.x, self.y, self.z))

    def __bool__(self):                 # bool(self) -- non-zero?
        return abs(self) != 0

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("v1:", v1)
print("v1 + v2:", v1 + v2)
print("v1 - v2:", v1 - v2)
print("v1 * 3:", v1 * 3)
print("3 * v1:", 3 * v1)       # rmul
print("-v1:", -v1)
print("|v1|:", round(abs(v1), 4))
print("v1 @ v2 (dot):", v1 @ v2)    # 1*4+2*5+3*6 = 32
print("v1 == v2:", v1 == v2)
print("v1 < v2:", v1 < v2)
print("len(v1):", len(v1))
print("v1[0], v1[1]:", v1[0], v1[1])
print("iter:", list(v1))
print("bool(v1):", bool(v1))
print("bool(Vector(0,0)):", bool(Vector(0,0)))

v1 += v2; print("v1 += v2:", v1)

# ----------------------------------------------------------
# 5. STRING / CONTAINER OPERATOR OVERLOADING
# ----------------------------------------------------------
print("\n=== CONTAINER OPERATORS ===")

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)
        return self   # for chaining

    def pop(self):
        return self._data.pop()

    def __len__(self):          # len(stack)
        return len(self._data)

    def __contains__(self, item):   # item in stack
        return item in self._data

    def __add__(self, other):       # stack1 + stack2
        new = Stack()
        new._data = self._data + other._data
        return new

    def __str__(self):
        return f"Stack{self._data}"

    def __repr__(self):
        return f"Stack({self._data!r})"

    def __bool__(self):
        return bool(self._data)

s1 = Stack()
s1.push(1).push(2).push(3)
s2 = Stack()
s2.push(4).push(5)
s3 = s1 + s2

print("s1:", s1)
print("s3:", s3)
print("len(s1):", len(s1))
print("2 in s1:", 2 in s1)
print("bool(s1):", bool(s1))

# ----------------------------------------------------------
# 6. @singledispatch -- type-based function overloading
# ----------------------------------------------------------
print("\n=== @singledispatch ===")

@singledispatch
def process(data):
    raise NotImplementedError(f"Cannot process type: {type(data)}")

@process.register(int)
def _(data):
    return f"Processing integer: {data * 2}"

@process.register(str)
def _(data):
    return f"Processing string: {data.upper()}"

@process.register(list)
def _(data):
    return f"Processing list: {sorted(data)}"

@process.register(float)
def _(data):
    return f"Processing float: {round(data, 2)}"

print(process(42))
print(process("hello"))
print(process([3, 1, 2]))
print(process(3.14159))

print("\n[Y] Polymorphism done!")
