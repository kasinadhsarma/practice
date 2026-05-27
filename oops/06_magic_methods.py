"""
==========================================================
  OOP IN PYTHON -- PART 6: MAGIC / DUNDER METHODS
==========================================================
  Group A -- Representation:  __str__, __repr__, __format__,
                               __bytes__, __hash__
  Group B -- Numeric:         __add__,__sub__,__mul__,__truediv__,
                               __floordiv__,__mod__,__pow__,
                               __neg__,__pos__,__abs__,__round__,
                               __ceil__,__floor__,__trunc__
  Group C -- Comparison:      __eq__,__ne__,__lt__,__le__,__gt__,__ge__
  Group D -- Container:       __len__,__getitem__,__setitem__,__delitem__,
                               __contains__,__iter__,__next__,__reversed__
  Group E -- Context Manager: __enter__, __exit__
  Group F -- Callable:        __call__
  Group G -- Attribute:       __getattr__,__setattr__,__delattr__,
                               __getattribute__
  Group H -- Class creation:  __new__,__init__,__del__,__init_subclass__
  Group I -- Copy:            __copy__, __deepcopy__
  Group J -- Misc:            __bool__, __int__, __float__,
                               __index__, __len__, __sizeof__
"""

import copy
import math
from contextlib import contextmanager

# ==========================================================
# GROUP A: REPRESENTATION
# ==========================================================
print("=== GROUP A: REPRESENTATION ===")

class Fraction:
    def __init__(self, num, den=1):
        from math import gcd
        g = gcd(abs(num), abs(den))
        sign = -1 if den < 0 else 1
        self.num = sign * num // g
        self.den = sign * den // g

    def __str__(self):
        """Human-readable: used by print(), str()."""
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def __repr__(self):
        """Developer-repr: used in REPL, lists, dicts."""
        return f"Fraction({self.num}, {self.den})"

    def __format__(self, spec):
        """Custom format: f'{obj:spec}'."""
        if spec == 'decimal':
            return f"{self.num/self.den:.6f}"
        elif spec == 'mixed':
            whole = self.num // self.den
            rem   = self.num % self.den
            return f"{whole} {rem}/{self.den}" if whole else str(self)
        return str(self)

    def __bytes__(self):
        return bytes(f"{self.num}/{self.den}", 'utf-8')

    def __hash__(self):
        return hash((self.num, self.den))

f = Fraction(3, 4)
print(str(f))                    # 3/4
print(repr(f))                   # Fraction(3, 4)
print(f"{f}")                    # 3/4
print(f"{f:decimal}")            # 0.750000
print(f"{Fraction(7,2):mixed}")  # 3 1/2
print(bytes(f))                  # b'3/4'
print(hash(f))

# ==========================================================
# GROUP B: NUMERIC OPERATORS
# ==========================================================
print("\n=== GROUP B: NUMERIC ===")

class Fraction2(Fraction):
    def __add__(self, other):
        if isinstance(other, int): other = Fraction(other)
        return Fraction2(self.num*other.den + other.num*self.den,
                         self.den * other.den)

    def __radd__(self, other):      # other + self  (when other doesn't know)
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int): other = Fraction(other)
        return Fraction2(self.num*other.den - other.num*self.den,
                         self.den * other.den)

    def __rsub__(self, other):
        return Fraction2(other).__sub__(self)

    def __mul__(self, other):
        if isinstance(other, int): other = Fraction(other)
        return Fraction2(self.num*other.num, self.den*other.den)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int): other = Fraction(other)
        return Fraction2(self.num*other.den, self.den*other.num)

    def __floordiv__(self, other):
        if isinstance(other, int): other = Fraction(other)
        return (self.num * other.den) // (self.den * other.num)

    def __mod__(self, other):
        if isinstance(other, int): other = Fraction(other)
        div = self // other
        return Fraction2(self.num*other.den - div*other.num*self.den,
                         self.den*other.den)

    def __pow__(self, exp):
        return Fraction2(self.num**exp, self.den**exp)

    def __neg__(self):  return Fraction2(-self.num, self.den)
    def __pos__(self):  return Fraction2(self.num, self.den)
    def __abs__(self):  return Fraction2(abs(self.num), self.den)

    def __round__(self, n=0):
        return round(self.num/self.den, n)

    def __floor__(self):    return math.floor(self.num/self.den)
    def __ceil__(self):     return math.ceil(self.num/self.den)
    def __trunc__(self):    return math.trunc(self.num/self.den)

    def __int__(self):      return int(self.num/self.den)
    def __float__(self):    return self.num/self.den
    def __bool__(self):     return self.num != 0

    # Comparison
    def __eq__(self, other):
        if isinstance(other, int): return self.num == other * self.den
        return self.num*other.den == other.num*self.den
    def __lt__(self, other):
        if isinstance(other, int): return self.num < other * self.den
        return self.num*other.den < other.num*self.den
    def __le__(self, other): return self == other or self < other
    def __gt__(self, other): return not self <= other
    def __ge__(self, other): return not self < other

a = Fraction2(1,2); b = Fraction2(1,3)
print(f"a={a}, b={b}")
print(f"a+b = {a+b}")           # 5/6
print(f"a-b = {a-b}")           # 1/6
print(f"a*b = {a*b}")           # 1/6
print(f"a/b = {a/b}")           # 3/2
print(f"a**3 = {a**3}")         # 1/8
print(f"-a = {-a}")             # -1/2
print(f"|{-a}| = {abs(-a)}")    # 1/2
print(f"round(a,2) = {round(a,2)}")
print(f"int(a) = {int(a)}")
print(f"float(a) = {float(a)}")
print(f"bool(a) = {bool(a)}, bool(Fraction2(0)) = {bool(Fraction2(0))}")
print(f"a == 0.5? {a == Fraction2(1,2)}")
print(f"a < b? {a < b}")

# ==========================================================
# GROUP D: CONTAINER PROTOCOL
# ==========================================================
print("\n=== GROUP D: CONTAINER ===")

class Matrix:
    def __init__(self, rows):
        self._data = [list(r) for r in rows]
        self._rows = len(self._data)
        self._cols = len(self._data[0]) if self._data else 0

    def __len__(self):              # len(matrix) -> rows
        return self._rows

    def __getitem__(self, key):     # matrix[i][j] or matrix[i,j]
        if isinstance(key, tuple):
            r, c = key
            return self._data[r][c]
        return self._data[key]

    def __setitem__(self, key, val):
        if isinstance(key, tuple):
            r, c = key
            self._data[r][c] = val
        else:
            self._data[key] = list(val)

    def __delitem__(self, key):
        del self._data[key]
        self._rows -= 1

    def __contains__(self, item):   # item in matrix
        return any(item in row for row in self._data)

    def __iter__(self):             # for row in matrix
        return iter(self._data)

    def __reversed__(self):         # reversed(matrix)
        return reversed(self._data)

    def __str__(self):
        return '\n'.join(str(row) for row in self._data)

    def __repr__(self):
        return f"Matrix({self._data})"

m = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix:\n", m)
print("len:", len(m))
print("m[1]:", m[1])
print("m[1,2]:", m[1,2])       # 6
m[0,0] = 99
print("After m[0,0]=99:", m[0])
print("5 in m:", 5 in m)
print("Rows:", list(m))
print("Reversed rows:", list(reversed(m)))

# ==========================================================
# GROUP E: CONTEXT MANAGER
# ==========================================================
print("\n=== GROUP E: CONTEXT MANAGER ===")

class FileManager:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode     = mode
        self.file     = None

    def __enter__(self):
        print(f"Opening {self.filename}")
        # self.file = open(self.filename, self.mode)
        return self     # 'as' target

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        # if self.file: self.file.close()
        if exc_type:
            print(f"Exception suppressed: {exc_val}")
            return True   # suppress exception
        return False

    def write(self, data):
        print(f"  Writing: {data!r}")

with FileManager("test.txt", "w") as fm:
    fm.write("Hello World")

# Context manager for timing
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.6f}s")

with Timer() as t:
    total = sum(range(100_000))
print("Sum:", total)

# ==========================================================
# GROUP F: CALLABLE
# ==========================================================
print("\n=== GROUP F: CALLABLE ===")

class Multiplier:
    """Makes an instance callable like a function."""
    def __init__(self, factor):
        self.factor = factor
        self.call_count = 0

    def __call__(self, x):
        self.call_count += 1
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print("double(5):", double(5))     # 10 -- calls __call__
print("triple(4):", triple(4))     # 12
print("callable(double):", callable(double))  # True
print("Calls:", double.call_count)

# Memoization using __call__
class Memoize:
    def __init__(self, func):
        self.func  = func
        self.cache = {}

    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]

@Memoize
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

print("fib(10):", fib(10))   # 55
print("Cache:", fib.cache)

# ==========================================================
# GROUP G: ATTRIBUTE ACCESS
# ==========================================================
print("\n=== GROUP G: ATTRIBUTE ACCESS ===")

class DynamicAttrs:
    def __init__(self):
        self._store = {}

    def __getattr__(self, name):
        """Called when normal attribute lookup fails."""
        if name in self._store:
            return self._store[name]
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def __setattr__(self, name, value):
        """Called on EVERY attribute assignment."""
        if name.startswith('_'):
            super().__setattr__(name, value)   # normal for private
        else:
            self._store[name] = value          # store custom attrs

    def __delattr__(self, name):
        if name in self._store:
            del self._store[name]
        else:
            super().__delattr__(name)

    def __getattribute__(self, name):
        """Called on EVERY attribute access (even existing ones)."""
        # Can intercept all access -- use carefully!
        return super().__getattribute__(name)

d = DynamicAttrs()
d.x = 10          # calls __setattr__ -> stored in _store
d.y = 20
print("d.x:", d.x)
print("d.y:", d.y)
del d.x
try: print(d.x)
except AttributeError as e: print("Deleted:", e)

# ==========================================================
# GROUP I: COPY
# ==========================================================
print("\n=== GROUP I: COPY ===")

class Config:
    def __init__(self, settings):
        self.settings = settings
        self.metadata = {"created": "2024"}

    def __copy__(self):
        """Shallow copy -- shared nested objects."""
        new = Config(self.settings.copy())
        new.metadata = self.metadata   # shared reference!
        return new

    def __deepcopy__(self, memo):
        """Deep copy -- fully independent."""
        new = Config(copy.deepcopy(self.settings, memo))
        new.metadata = copy.deepcopy(self.metadata, memo)
        return new

original = Config({"theme": "dark", "lang": "en"})
shallow  = copy.copy(original)
deep     = copy.deepcopy(original)

original.settings["theme"] = "light"
original.metadata["version"] = "2"

print("Original settings:", original.settings)
print("Shallow settings:", shallow.settings)  # own copy
print("Shallow metadata:", shallow.metadata)  # shared -> sees 'version'!
print("Deep settings:", deep.settings)        # fully independent
print("Deep metadata:", deep.metadata)        # independent

print("\n[Y] Magic Methods done!")
