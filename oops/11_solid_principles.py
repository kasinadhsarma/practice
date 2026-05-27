"""
==========================================================
  OOP IN PYTHON -- PART 11: SOLID PRINCIPLES
==========================================================
  S -- Single Responsibility Principle
  O -- Open / Closed Principle
  L -- Liskov Substitution Principle
  I -- Interface Segregation Principle
  D -- Dependency Inversion Principle
"""

from abc import ABC, abstractmethod

# ==========================================================
# S -- SINGLE RESPONSIBILITY PRINCIPLE (SRP)
#      A class should have only ONE reason to change
# ==========================================================
print("=== S: SINGLE RESPONSIBILITY ===")

# BAD -- one class does too many things
class BadEmployee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

    def calculate_tax(self):            # tax logic -- should be elsewhere
        return self.salary * 0.3

    def save_to_db(self):               # DB logic -- should be elsewhere
        print(f"Saving {self.name} to DB")

    def generate_report(self):          # reporting -- should be elsewhere
        return f"Report for {self.name}"


# GOOD -- each class has one job
class Employee:
    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary

class TaxCalculator:
    def calculate(self, employee: Employee) -> float:
        return employee.salary * 0.3

class EmployeeRepository:
    def save(self, employee: Employee):
        print(f"Saving {employee.name} to DB")

    def load(self, name: str) -> Employee:
        return Employee(name, 50000)  # simulated

class ReportGenerator:
    def generate(self, employee: Employee) -> str:
        return f"Report: {employee.name}, salary={employee.salary}"

e = Employee("Alice", 60000)
print(TaxCalculator().calculate(e))
print(ReportGenerator().generate(e))
EmployeeRepository().save(e)

# ==========================================================
# O -- OPEN / CLOSED PRINCIPLE (OCP)
#      Open for EXTENSION, closed for MODIFICATION
# ==========================================================
print("\n=== O: OPEN / CLOSED ===")

# BAD -- must modify existing code to add new discount
class BadDiscountCalc:
    def discount(self, customer_type, price):
        if customer_type == "regular":
            return price
        elif customer_type == "premium":
            return price * 0.9
        elif customer_type == "vip":
            return price * 0.8
        # adding new type requires modifying this file!


# GOOD -- extend by adding new class, never modify existing
class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: pass

class NoDiscount(Discount):
    def apply(self, price): return price

class PremiumDiscount(Discount):
    def apply(self, price): return price * 0.9

class VIPDiscount(Discount):
    def apply(self, price): return price * 0.8

# New type -- just ADD a class, don't modify existing code
class StaffDiscount(Discount):
    def apply(self, price): return price * 0.5

class PriceCalculator:
    def __init__(self, discount: Discount):
        self._discount = discount

    def final_price(self, price: float) -> float:
        return self._discount.apply(price)

base_price = 100.0
for dtype, disc in [("Regular", NoDiscount()), ("Premium", PremiumDiscount()),
                    ("VIP", VIPDiscount()), ("Staff", StaffDiscount())]:
    calc = PriceCalculator(disc)
    print(f"{dtype}: ${calc.final_price(base_price):.2f}")

# ==========================================================
# L -- LISKOV SUBSTITUTION PRINCIPLE (LSP)
#      Subtypes must be substitutable for their base types
#      without altering program correctness
# ==========================================================
print("\n=== L: LISKOV SUBSTITUTION ===")

# BAD -- Square violates LSP when inheriting from Rectangle
class BadRectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def set_width(self, w):  self.w = w
    def set_height(self, h): self.h = h
    def area(self): return self.w * self.h

class BadSquare(BadRectangle):
    def set_width(self, w):  self.w = self.h = w   # BREAKS LSP!
    def set_height(self, h): self.w = self.h = h   # unexpected behaviour

# A function that works on Rectangle breaks with Square
def process_rectangle(rect: BadRectangle):
    rect.set_width(4)
    rect.set_height(5)
    assert rect.area() == 20, f"Expected 20, got {rect.area()}"

process_rectangle(BadRectangle(2, 3))   # OK
try:
    process_rectangle(BadSquare(2, 2))  # FAILS!
except AssertionError as e:
    print("LSP violated:", e)


# GOOD -- separate hierarchy, no false IS-A
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

# Both are Shapes -- substitutable safely
shapes = [Rectangle(4, 5), Square(4)]
for s in shapes:
    print(f"{type(s).__name__} area: {s.area()}")

# ==========================================================
# I -- INTERFACE SEGREGATION PRINCIPLE (ISP)
#      Clients should not be forced to implement interfaces
#      they don't use. Prefer many small interfaces.
# ==========================================================
print("\n=== I: INTERFACE SEGREGATION ===")

# BAD -- one fat interface forces all implementations
class BadMachine(ABC):
    @abstractmethod
    def print(self): pass

    @abstractmethod
    def scan(self): pass

    @abstractmethod
    def fax(self): pass

class OldPrinter(BadMachine):
    def print(self): return "Printing"
    def scan(self): raise NotImplementedError("Old printer can't scan")
    def fax(self):  raise NotImplementedError("Old printer can't fax")
    # forced to implement methods it doesn't support!


# GOOD -- small, focused interfaces
class Printable(ABC):
    @abstractmethod
    def print(self) -> str: pass

class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str: pass

class Faxable(ABC):
    @abstractmethod
    def fax(self) -> str: pass

class SimplePrinter(Printable):          # only what it needs
    def print(self): return "Printing..."

class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print(self): return "Printing..."
    def scan(self):  return "Scanning..."
    def fax(self):   return "Faxing..."

class Scanner(Scannable):               # only scanning
    def scan(self): return "Scanning..."

sp = SimplePrinter()
mfp = MultiFunctionPrinter()
sc = Scanner()

print(sp.print())
print(mfp.print(), mfp.scan(), mfp.fax())
print(sc.scan())

# ==========================================================
# D -- DEPENDENCY INVERSION PRINCIPLE (DIP)
#      High-level modules should NOT depend on low-level.
#      Both should depend on abstractions.
# ==========================================================
print("\n=== D: DEPENDENCY INVERSION ===")

# BAD -- high-level OrderProcessor depends on concrete MySQLDB
class BadMySQLDB:
    def save(self, data): print(f"MySQL: saving {data}")

class BadOrderProcessor:
    def __init__(self):
        self.db = BadMySQLDB()   # tightly coupled!

    def process(self, order):
        self.db.save(order)


# GOOD -- depend on abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data): pass

    @abstractmethod
    def find(self, id_): pass

class MySQLDB(Database):
    def save(self, data): print(f"[MySQL] Saving: {data}")
    def find(self, id_):  return f"MySQL row #{id_}"

class MongoDB(Database):
    def save(self, data): print(f"[MongoDB] Inserting: {data}")
    def find(self, id_):  return f"MongoDB doc #{id_}"

class InMemoryDB(Database):
    def __init__(self): self._store = {}
    def save(self, data):
        self._store[id(data)] = data
        print(f"[InMemory] Stored: {data}")
    def find(self, id_): return self._store.get(id_, None)

class OrderProcessor:             # high-level module
    def __init__(self, db: Database):   # injected abstraction
        self._db = db

    def process(self, order):
        print(f"Processing order: {order}")
        self._db.save(order)

    def find_order(self, id_):
        return self._db.find(id_)

# Swap DB without changing OrderProcessor
for db in [MySQLDB(), MongoDB(), InMemoryDB()]:
    proc = OrderProcessor(db)
    proc.process({"id": 1, "item": "Laptop"})

print("\n=== SOLID SUMMARY ===")
print("""
S -- SRP: One class, one reason to change
     Split Employee + TaxCalc + Repository + Reporter

O -- OCP: Extend behaviour by adding new classes
     Add StaffDiscount without touching PriceCalculator

L -- LSP: Subtypes must honour base class contracts
     Square should NOT inherit Rectangle (violates contract)

I -- ISP: Small focused interfaces > one fat interface
     Printable + Scannable + Faxable (not one big Machine)

D -- DIP: Depend on abstractions, inject concrete
     OrderProcessor(Database) -- not OrderProcessor(MySQL)
""")

print("[Y] SOLID Principles done!")
