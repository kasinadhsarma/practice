"""
==========================================================
  OOP IN PYTHON -- PART 7: CLASS METHODS, STATIC METHODS, PROPERTIES
==========================================================
  1. Instance methods  -- operate on instance (self)
  2. Class methods     -- operate on class (cls)
  3. Static methods    -- utility, no self/cls
  4. @property         -- computed attribute
  5. @setter / @deleter
  6. Alternative constructors using @classmethod
  7. Factory pattern with @classmethod
  8. Class method vs Static method -- when to use which
  9. @cached_property  -- computed once, cached
"""

from functools import cached_property
import datetime
import math

# ----------------------------------------------------------
# 1. ALL THREE METHOD TYPES ON ONE CLASS
# ----------------------------------------------------------
print("=== THREE METHOD TYPES ===")

class Employee:
    # Class variable -- shared by all instances
    _company   = "TechCorp"
    _raise_pct = 1.05
    _count     = 0

    def __init__(self, name, salary, dept):
        self.name   = name
        self._salary = salary
        self.dept   = dept
        Employee._count += 1

    # ── INSTANCE METHOD ──────────────────────────────────
    # Receives 'self' -- works on the specific instance
    def raise_salary(self):
        self._salary *= Employee._raise_pct
        return self._salary

    def info(self):
        return (f"Employee: {self.name} | Dept: {self.dept} "
                f"| Salary: ${self._salary:.2f}")

    # ── CLASS METHOD ─────────────────────────────────────
    # Receives 'cls' -- works on the class itself
    @classmethod
    def get_company(cls):
        return cls._company

    @classmethod
    def set_raise(cls, pct):
        cls._raise_pct = pct

    @classmethod
    def get_count(cls):
        return cls._count

    # Alternative constructors (factory methods)
    @classmethod
    def from_string(cls, emp_str):
        """Create from 'name-salary-dept' string."""
        name, salary, dept = emp_str.split('-')
        return cls(name, float(salary), dept)

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['salary'], d['dept'])

    # ── STATIC METHOD ────────────────────────────────────
    # Receives neither self nor cls -- pure utility
    @staticmethod
    def is_workday(day: datetime.date) -> bool:
        return day.weekday() < 5   # Mon-Fri

    @staticmethod
    def annual_to_monthly(annual):
        return annual / 12

    @staticmethod
    def validate_salary(salary):
        return isinstance(salary, (int, float)) and salary > 0

    def __str__(self):
        return self.info()

# Instance methods
e1 = Employee("Alice", 60000, "Engineering")
e2 = Employee("Bob",   50000, "Marketing")
print(e1.info())
e1.raise_salary()
print("After raise:", e1.info())

# Class methods
print("\nCompany:", Employee.get_company())
print("Count:", Employee.get_count())

e3 = Employee.from_string("Carol-55000-Finance")
print("From string:", e3.info())

e4 = Employee.from_dict({"name": "Dan", "salary": 70000, "dept": "HR"})
print("From dict:", e4.info())

# Static methods (callable on class or instance)
today = datetime.date.today()
print("\nIs today a workday?", Employee.is_workday(today))
print("Monthly from 60000:", Employee.annual_to_monthly(60000))
print("Valid salary 50000:", Employee.validate_salary(50000))
print("Valid salary -100:", Employee.validate_salary(-100))

# Set class variable via class method
Employee.set_raise(1.10)
print("New raise:", Employee._raise_pct)

# ----------------------------------------------------------
# 2. ADVANCED @property USE CASES
# ----------------------------------------------------------
print("\n=== ADVANCED @property ===")

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius    # backing field

    # Getter
    @property
    def celsius(self):
        return self._celsius

    # Setter with validation
    @celsius.setter
    def celsius(self, val):
        if val < -273.15:
            raise ValueError(f"Below absolute zero: {val}")
        self._celsius = val

    # Deleter
    @celsius.deleter
    def celsius(self):
        del self._celsius

    # Computed properties -- derived from celsius
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, val):
        self.celsius = (val - 32) * 5/9    # validates via celsius setter

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, val):
        self.celsius = val - 273.15

    def __str__(self):
        return f"{self.celsius}C / {self.fahrenheit}F / {self.kelvin}K"

t = Temperature(25)
print(t)

t.fahrenheit = 212           # set via fahrenheit
print("Set 212F ->", t)      # 100C / 212F / 373.15K

t.kelvin = 0                 # absolute zero
print("Set 0K ->", t)

try:
    t.celsius = -300
except ValueError as e:
    print("Error:", e)

# ----------------------------------------------------------
# 3. @cached_property -- computed once then cached
# ----------------------------------------------------------
print("\n=== @cached_property ===")

class DataSet:
    def __init__(self, data):
        self.data = data

    @cached_property
    def mean(self):
        print("  Computing mean...")
        return sum(self.data) / len(self.data)

    @cached_property
    def variance(self):
        print("  Computing variance...")
        m = self.mean
        return sum((x - m)**2 for x in self.data) / len(self.data)

    @cached_property
    def std_dev(self):
        print("  Computing std_dev...")
        return self.variance ** 0.5

ds = DataSet([2, 4, 4, 4, 5, 5, 7, 9])
print("First call mean:", ds.mean)    # computes
print("Second call mean:", ds.mean)  # cached -- no print
print("std_dev:", round(ds.std_dev, 4))

# ----------------------------------------------------------
# 4. CLASS vs STATIC vs INSTANCE -- decision guide
# ----------------------------------------------------------
print("""
Method Type | Receives   | Use When
------------+------------+---------------------------------------
Instance    | self       | Needs to access/modify instance state
Class       | cls        | Needs to access/modify class state;
            |            |   alternative constructors; factory
Static      | nothing    | Pure utility related to the class;
            |            |   doesn't need any state
""")

# ----------------------------------------------------------
# 5. PRACTICAL EXAMPLE -- Date with all three types
# ----------------------------------------------------------
print("=== DATE CLASS EXAMPLE ===")

class Date:
    _format = "%Y-%m-%d"     # class variable

    def __init__(self, year, month, day):
        self._year  = year
        self._month = month
        self._day   = day

    # Instance method
    def is_leap_year(self):
        y = self._year
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def days_until(self, other):
        d1 = datetime.date(self._year, self._month, self._day)
        d2 = datetime.date(other._year, other._month, other._day)
        return abs((d2 - d1).days)

    # Class methods -- alternative constructors
    @classmethod
    def today(cls):
        t = datetime.date.today()
        return cls(t.year, t.month, t.day)

    @classmethod
    def from_iso(cls, iso_str):
        y, m, d = map(int, iso_str.split('-'))
        return cls(y, m, d)

    @classmethod
    def set_format(cls, fmt):
        cls._format = fmt

    # Static methods -- utilities
    @staticmethod
    def is_valid(year, month, day):
        try:
            datetime.date(year, month, day)
            return True
        except ValueError:
            return False

    @staticmethod
    def days_in_month(year, month):
        import calendar
        return calendar.monthrange(year, month)[1]

    @property
    def year(self):  return self._year

    @property
    def month(self): return self._month

    @property
    def day(self):   return self._day

    def __str__(self):
        return f"{self._year}-{self._month:02d}-{self._day:02d}"

    def __repr__(self):
        return f"Date({self._year}, {self._month}, {self._day})"

d1 = Date.today()
d2 = Date.from_iso("2025-12-31")
print("Today:", d1)
print("From ISO:", d2)
print("Days between:", d1.days_until(d2))
print("Is 2024 leap?", Date(2024,1,1).is_leap_year())
print("Is valid 2024-02-29?", Date.is_valid(2024,2,29))
print("Days in Feb 2024:", Date.days_in_month(2024, 2))

print("\n[Y] Class/Static Methods & Properties done!")
