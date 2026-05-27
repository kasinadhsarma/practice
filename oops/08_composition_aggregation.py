"""
==========================================================
  OOP IN PYTHON -- PART 8: COMPOSITION, AGGREGATION,
                            ASSOCIATION & DEPENDENCY
==========================================================
  Relationships between classes:
  1. Association   -- A uses B (loosest)
  2. Dependency    -- A uses B temporarily
  3. Aggregation   -- A HAS-A B (B can exist without A)
  4. Composition   -- A HAS-A B (B dies with A, owns it)
  5. Composition vs Inheritance -- when to use each
  6. Favour Composition over Inheritance (design principle)
"""

# ----------------------------------------------------------
# 1. ASSOCIATION -- A uses B, no ownership
# ----------------------------------------------------------
print("=== ASSOCIATION ===")

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, student):
        return f"{self.name} teaches {student.name}"

class Student:
    def __init__(self, name):
        self.name = name

    def learn_from(self, teacher):
        return f"{self.name} learns from {teacher.name}"

t = Teacher("Mr. Smith")
s = Student("Alice")
print(t.teach(s))
print(s.learn_from(t))

# ----------------------------------------------------------
# 2. DEPENDENCY -- A uses B only inside a method
# ----------------------------------------------------------
print("\n=== DEPENDENCY ===")

class Printer:
    def print_doc(self, document):     # Document is a dependency
        print(f"Printing: {document.content}")

class Document:
    def __init__(self, content):
        self.content = content

p = Printer()
doc = Document("Hello World")
p.print_doc(doc)          # Printer depends on Document only here

# ----------------------------------------------------------
# 3. AGGREGATION -- HAS-A but NOT owner
#    Department has Employees, but Employees can exist without Department
# ----------------------------------------------------------
print("\n=== AGGREGATION ===")

class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} ({self.role})"

class Department:
    def __init__(self, name):
        self.name      = name
        self.employees = []   # aggregation -- Employee exists independently

    def add_employee(self, emp):
        self.employees.append(emp)

    def remove_employee(self, emp):
        self.employees.remove(emp)

    def list_employees(self):
        return [str(e) for e in self.employees]

    def __str__(self):
        return f"Dept({self.name}, {len(self.employees)} employees)"

# Employees exist BEFORE and AFTER department
e1 = Employee("Alice", "Developer")
e2 = Employee("Bob",   "Designer")
e3 = Employee("Carol", "Manager")

dept = Department("Engineering")
dept.add_employee(e1)
dept.add_employee(e2)
print(dept)
print("Staff:", dept.list_employees())

# Employee can move to another department
dept2 = Department("Product")
dept.remove_employee(e2)
dept2.add_employee(e2)
dept2.add_employee(e3)
print("After transfer:", dept)
print("Product dept:", dept2)

# Employees still exist after departments are deleted
del dept, dept2
print("e1 still exists:", e1)
print("e2 still exists:", e2)

# ----------------------------------------------------------
# 4. COMPOSITION -- HAS-A and OWNS it
#    Car HAS-A Engine -- Engine is created & destroyed with Car
# ----------------------------------------------------------
print("\n=== COMPOSITION ===")

class Engine:
    def __init__(self, horsepower, fuel_type):
        self.hp        = horsepower
        self.fuel_type = fuel_type
        self.running   = False

    def start(self):
        self.running = True
        return f"Engine ({self.hp}hp, {self.fuel_type}) started"

    def stop(self):
        self.running = False
        return "Engine stopped"

    def __str__(self):
        status = "ON" if self.running else "OFF"
        return f"Engine[{self.hp}hp, {self.fuel_type}, {status}]"

class Transmission:
    def __init__(self, gear_type):
        self.gear_type   = gear_type
        self.current_gear = 0

    def shift(self, gear):
        self.current_gear = gear
        return f"Shifted to gear {gear}"

class Car:
    def __init__(self, make, model, hp, fuel, transmission):
        self.make  = make
        self.model = model
        # COMPOSITION -- Car creates and OWNS engine & transmission
        self.engine       = Engine(hp, fuel)
        self.transmission = Transmission(transmission)
        self.speed = 0

    def start(self):
        return self.engine.start()

    def shift(self, gear):
        return self.transmission.shift(gear)

    def stop(self):
        return self.engine.stop()

    def __str__(self):
        return (f"{self.make} {self.model} | "
                f"{self.engine} | "
                f"Trans: {self.transmission.gear_type}")

car = Car("Toyota", "Camry", 200, "Petrol", "Automatic")
print(car)
print(car.start())
print(car.shift(3))
print(car.stop())

# ----------------------------------------------------------
# 5. RICH COMPOSITION -- Computer example
# ----------------------------------------------------------
print("\n=== RICH COMPOSITION (Computer) ===")

class CPU:
    def __init__(self, model, cores, ghz):
        self.model = model
        self.cores = cores
        self.ghz   = ghz

    def __str__(self):
        return f"CPU({self.model}, {self.cores}c, {self.ghz}GHz)"

class RAM:
    def __init__(self, size_gb, speed_mhz):
        self.size  = size_gb
        self.speed = speed_mhz

    def __str__(self):
        return f"RAM({self.size}GB, {self.speed}MHz)"

class Storage:
    def __init__(self, size_gb, type_="SSD"):
        self.size = size_gb
        self.type = type_

    def __str__(self):
        return f"Storage({self.size}GB {self.type})"

class GPU:
    def __init__(self, model, vram_gb):
        self.model = model
        self.vram  = vram_gb

    def __str__(self):
        return f"GPU({self.model}, {self.vram}GB VRAM)"

class Computer:
    def __init__(self, brand, cpu: CPU, ram: RAM,
                 storage: Storage, gpu: GPU = None):
        self.brand   = brand
        self.cpu     = cpu
        self.ram     = ram
        self.storage = storage
        self.gpu     = gpu

    def specs(self):
        lines = [f"=== {self.brand} ===",
                 f"  {self.cpu}",
                 f"  {self.ram}",
                 f"  {self.storage}"]
        if self.gpu:
            lines.append(f"  {self.gpu}")
        return '\n'.join(lines)

    def upgrade_ram(self, new_ram: RAM):
        self.ram = new_ram

    def add_gpu(self, gpu: GPU):
        self.gpu = gpu

pc = Computer(
    "Gaming PC",
    cpu     = CPU("Ryzen 9 7950X", 16, 4.5),
    ram     = RAM(32, 6000),
    storage = Storage(2000, "NVMe"),
    gpu     = GPU("RTX 4090", 24)
)
print(pc.specs())

pc.upgrade_ram(RAM(64, 6000))
print("\nAfter RAM upgrade:")
print(pc.specs())

# ----------------------------------------------------------
# 6. COMPOSITION vs INHERITANCE -- decision guide
# ----------------------------------------------------------
print("""
=== WHEN TO USE INHERITANCE vs COMPOSITION ===

INHERITANCE (IS-A):
  - Dog IS-A Animal          --> Dog(Animal)
  - ElectricCar IS-A Car     --> ElectricCar(Car)
  - Use when relationship is truly IS-A
  - Use when you want to extend/override behaviour

COMPOSITION (HAS-A):
  - Car HAS-A Engine         --> self.engine = Engine()
  - Computer HAS-A CPU       --> self.cpu = CPU()
  - Use when object is made UP of other objects
  - Use when you want to reuse behaviour without IS-A

RULE: Prefer Composition over Inheritance!
  - More flexible (swap components at runtime)
  - Avoids deep inheritance hierarchies
  - Easier to test (mock components)
  - Avoids fragile base class problem
""")

# ----------------------------------------------------------
# 7. FAVOUR COMPOSITION -- swap behaviour at runtime
# ----------------------------------------------------------
print("=== FAVOUR COMPOSITION (Strategy-like) ===")

class SortStrategy:
    def sort(self, data): raise NotImplementedError

class BubbleSort(SortStrategy):
    def sort(self, data):
        a = data[:]
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j] > a[j+1]: a[j],a[j+1] = a[j+1],a[j]
        return a

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1: return data
        pivot = data[len(data)//2]
        left  = [x for x in data if x < pivot]
        mid   = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy   # COMPOSITION

    def set_strategy(self, strategy):
        self._strategy = strategy   # swap at RUNTIME

    def sort(self, data):
        return self._strategy.sort(data)

data = [5, 2, 8, 1, 9, 3]
sorter = Sorter(BubbleSort())
print("Bubble:", sorter.sort(data))

sorter.set_strategy(QuickSort())   # swap at runtime
print("Quick:", sorter.sort(data))

print("\n[Y] Composition & Aggregation done!")
