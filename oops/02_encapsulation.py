"""
==========================================================
  OOP IN PYTHON -- PART 2: ENCAPSULATION
==========================================================
  1. Public, Protected, Private access modifiers
  2. Name mangling
  3. Getters & Setters (manual)
  4. @property, @setter, @deleter
  5. Read-only, Write-only, Computed properties
  6. Data hiding -- why and how
  7. Practical Bank Account example
"""

# ----------------------------------------------------------
# 1. ACCESS MODIFIERS
# ----------------------------------------------------------
print("=== ACCESS MODIFIERS ===")

class Person:
    def __init__(self, name, age, ssn):
        self.name    = name      # PUBLIC    -- accessible everywhere
        self._age    = age       # PROTECTED -- convention: internal use
        self.__ssn   = ssn       # PRIVATE   -- name-mangled by Python

    def get_info(self):
        # all three accessible INSIDE the class
        return f"{self.name}, {self._age}, SSN=***{self.__ssn[-4:]}"

p = Person("Alice", 30, "123-45-6789")

print(p.name)               # OK -- public
print(p._age)               # OK but warned (protected by convention)
# print(p.__ssn)            # AttributeError -- name mangled!

# Name mangling: __attr becomes _ClassName__attr
print(p._Person__ssn)       # works but should never do this
print(p.get_info())

# ----------------------------------------------------------
# 2. MANUAL GETTERS & SETTERS
# ----------------------------------------------------------
print("\n=== MANUAL GETTERS & SETTERS ===")

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius   # private

    # Getter
    def get_celsius(self):
        return self.__celsius

    # Setter with validation
    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self.__celsius = value

    # Derived getter (no corresponding private variable)
    def get_fahrenheit(self):
        return self.__celsius * 9/5 + 32

t = Temperature(25)
print("Celsius:", t.get_celsius())
print("Fahrenheit:", t.get_fahrenheit())
t.set_celsius(100)
print("After set:", t.get_celsius())

try:
    t.set_celsius(-300)
except ValueError as e:
    print("Error:", e)

# ----------------------------------------------------------
# 3. @property -- PYTHONIC WAY (same effect, cleaner syntax)
# ----------------------------------------------------------
print("\n=== @property ===")

class Circle:
    def __init__(self, radius):
        self._radius = radius     # protected backing field

    # Read property (getter)
    @property
    def radius(self):
        return self._radius

    # Write property (setter)
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Delete property (deleter)
    @radius.deleter
    def radius(self):
        print("Deleting radius")
        del self._radius

    # Computed / derived property (read-only)
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        return self._radius * 2

    # area has no setter -- read-only!

c = Circle(5)
print("radius:", c.radius)     # calls getter
print("area:", round(c.area, 4))
print("diameter:", c.diameter)

c.radius = 10                  # calls setter
print("new radius:", c.radius)

try:
    c.radius = -1
except ValueError as e:
    print("Error:", e)

try:
    c.area = 100               # no setter defined!
except AttributeError as e:
    print("Cannot set area:", e)

del c.radius                   # calls deleter

# ----------------------------------------------------------
# 4. READ-ONLY & WRITE-ONLY PROPERTIES
# ----------------------------------------------------------
print("\n=== READ-ONLY / WRITE-ONLY ===")

class Passport:
    def __init__(self, number, holder):
        self.__number = number
        self.__holder = holder
        self.__stamp_count = 0

    @property
    def number(self):
        """Read-only -- no setter defined."""
        return self.__number

    @property
    def holder(self):
        return self.__holder

    # Write-only (setter only, no getter)
    def _set_secret(self, val):
        self.__secret = val
    secret = property(fset=_set_secret)

    def add_stamp(self):
        self.__stamp_count += 1

    @property
    def stamps(self):
        return self.__stamp_count

pp = Passport("A1234567", "Alice")
print("Number:", pp.number)
print("Holder:", pp.holder)
pp.add_stamp(); pp.add_stamp()
print("Stamps:", pp.stamps)

try:
    pp.number = "B9999999"   # read-only!
except AttributeError as e:
    print("Cannot change passport number:", e)

# ----------------------------------------------------------
# 5. FULL BANK ACCOUNT -- Encapsulation in practice
# ----------------------------------------------------------
print("\n=== BANK ACCOUNT (Encapsulation) ===")

class BankAccount:
    _interest_rate = 0.03      # protected class variable

    def __init__(self, owner, initial_balance=0):
        self.__owner   = owner
        self.__balance = 0.0
        self.__history = []
        if initial_balance > 0:
            self.deposit(initial_balance)

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return round(self.__balance, 2)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.__history.append(f"+ {amount:.2f}")
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__history.append(f"- {amount:.2f}")
        return self

    def apply_interest(self):
        interest = self.__balance * BankAccount._interest_rate
        self.__balance += interest
        self.__history.append(f"+ {interest:.2f} (interest)")

    @property
    def history(self):
        return self.__history[:]   # return copy -- not original!

    @classmethod
    def set_interest_rate(cls, rate):
        if not 0 <= rate <= 1:
            raise ValueError("Rate must be between 0 and 1")
        cls._interest_rate = rate

    def __str__(self):
        return f"Account[{self.__owner}] Balance: ${self.balance:.2f}"

acc = BankAccount("Bob", 1000)
acc.deposit(500).deposit(200)   # method chaining
acc.withdraw(300)
acc.apply_interest()
print(acc)
print("History:", acc.history)

try:
    acc.withdraw(5000)
except ValueError as e:
    print("Error:", e)

BankAccount.set_interest_rate(0.05)
print("New rate:", BankAccount._interest_rate)

print("\n[Y] Encapsulation done!")
