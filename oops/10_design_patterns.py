"""
==========================================================
  OOP IN PYTHON -- PART 10: DESIGN PATTERNS
==========================================================
  Creational Patterns:
    1.  Singleton
    2.  Factory Method
    3.  Abstract Factory
    4.  Builder
    5.  Prototype

  Structural Patterns:
    6.  Adapter
    7.  Decorator
    8.  Facade
    9.  Proxy
    10. Composite

  Behavioural Patterns:
    11. Observer / Event System
    12. Strategy
    13. Template Method
    14. Command
    15. Iterator
"""

import copy
from abc import ABC, abstractmethod

# ==========================================================
# CREATIONAL PATTERNS
# ==========================================================

# ----------------------------------------------------------
# 1. SINGLETON -- only one instance ever exists
# ----------------------------------------------------------
print("=== 1. SINGLETON ===")

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._logs = []
        return cls._instance

    def log(self, msg):
        self._logs.append(msg)
        print(f"[LOG] {msg}")

    def get_logs(self):
        return self._logs[:]

l1 = Logger(); l1.log("System started")
l2 = Logger(); l2.log("User logged in")
print("Same?", l1 is l2)       # True
print("Logs:", l1.get_logs())  # both logs visible via l1

# ----------------------------------------------------------
# 2. FACTORY METHOD -- subclass decides which object to create
# ----------------------------------------------------------
print("\n=== 2. FACTORY METHOD ===")

class Notification(ABC):
    @abstractmethod
    def send(self, msg): pass

class EmailNotification(Notification):
    def __init__(self, email): self.email = email
    def send(self, msg): return f"Email to {self.email}: {msg}"

class SMSNotification(Notification):
    def __init__(self, phone): self.phone = phone
    def send(self, msg): return f"SMS to {self.phone}: {msg}"

class PushNotification(Notification):
    def __init__(self, token): self.token = token
    def send(self, msg): return f"Push [{self.token}]: {msg}"

class NotificationFactory:
    @staticmethod
    def create(type_: str, target: str) -> Notification:
        mapping = {
            'email': EmailNotification,
            'sms':   SMSNotification,
            'push':  PushNotification,
        }
        if type_ not in mapping:
            raise ValueError(f"Unknown type: {type_}")
        return mapping[type_](target)

for t, tgt in [("email","alice@x.com"), ("sms","555-1234"), ("push","tok123")]:
    n = NotificationFactory.create(t, tgt)
    print(n.send("Hello!"))

# ----------------------------------------------------------
# 3. ABSTRACT FACTORY -- family of related objects
# ----------------------------------------------------------
print("\n=== 3. ABSTRACT FACTORY ===")

class Button(ABC):
    @abstractmethod
    def render(self): pass

class TextBox(ABC):
    @abstractmethod
    def render(self): pass

class WindowsButton(Button):
    def render(self): return "[Windows Button]"

class MacButton(Button):
    def render(self): return "(Mac Button)"

class WindowsTextBox(TextBox):
    def render(self): return "[Windows TextBox_____]"

class MacTextBox(TextBox):
    def render(self): return "(Mac TextBox ~~~~~)"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: pass

    @abstractmethod
    def create_textbox(self) -> TextBox: pass

class WindowsFactory(GUIFactory):
    def create_button(self):  return WindowsButton()
    def create_textbox(self): return WindowsTextBox()

class MacFactory(GUIFactory):
    def create_button(self):  return MacButton()
    def create_textbox(self): return MacTextBox()

def render_ui(factory: GUIFactory):
    btn = factory.create_button()
    tb  = factory.create_textbox()
    print(f"  {btn.render()}")
    print(f"  {tb.render()}")

print("Windows UI:")
render_ui(WindowsFactory())
print("Mac UI:")
render_ui(MacFactory())

# ----------------------------------------------------------
# 4. BUILDER -- step-by-step complex object creation
# ----------------------------------------------------------
print("\n=== 4. BUILDER ===")

class Pizza:
    def __init__(self):
        self.size    = None
        self.crust   = None
        self.sauce   = None
        self.toppings = []

    def __str__(self):
        return (f"Pizza({self.size}, {self.crust} crust, "
                f"{self.sauce} sauce, toppings={self.toppings})")

class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def size(self, size):
        self._pizza.size = size
        return self       # fluent interface

    def crust(self, crust):
        self._pizza.crust = crust
        return self

    def sauce(self, sauce):
        self._pizza.sauce = sauce
        return self

    def topping(self, *toppings):
        self._pizza.toppings.extend(toppings)
        return self

    def build(self):
        return self._pizza

p = (PizzaBuilder()
     .size("Large")
     .crust("Thin")
     .sauce("Tomato")
     .topping("Pepperoni", "Mushrooms", "Olives")
     .build())
print(p)

# ----------------------------------------------------------
# 5. PROTOTYPE -- clone existing objects
# ----------------------------------------------------------
print("\n=== 5. PROTOTYPE ===")

class ConfigPrototype:
    def __init__(self, host, port, settings):
        self.host     = host
        self.port     = port
        self.settings = settings.copy()

    def clone(self, **overrides):
        obj = copy.deepcopy(self)
        for k, v in overrides.items():
            setattr(obj, k, v)
        return obj

    def __str__(self):
        return f"Config({self.host}:{self.port}, {self.settings})"

base = ConfigPrototype("localhost", 8080, {"debug": False, "timeout": 30})
dev  = base.clone(host="dev.server.com", port=3000)
prod = base.clone(host="prod.server.com", port=443)
dev.settings['debug'] = True

print("Base:", base)
print("Dev:", dev)
print("Prod:", prod)

# ==========================================================
# STRUCTURAL PATTERNS
# ==========================================================

# ----------------------------------------------------------
# 6. ADAPTER -- make incompatible interfaces work together
# ----------------------------------------------------------
print("\n=== 6. ADAPTER ===")

class EuropeanSocket:         # existing (adaptee)
    def provide_220v(self): return "220V power"

class USASocket:              # target interface
    def provide_110v(self): raise NotImplementedError

class SocketAdapter(USASocket):   # adapter
    def __init__(self, euro_socket: EuropeanSocket):
        self._euro = euro_socket

    def provide_110v(self):
        power = self._euro.provide_220v()
        return f"Converted {power} -> 110V"

adapter = SocketAdapter(EuropeanSocket())
print(adapter.provide_110v())

# ----------------------------------------------------------
# 7. DECORATOR PATTERN -- add behaviour dynamically
# ----------------------------------------------------------
print("\n=== 7. DECORATOR PATTERN ===")

class Coffee(ABC):
    @abstractmethod
    def cost(self): pass

    @abstractmethod
    def description(self): pass

class SimpleCoffee(Coffee):
    def cost(self): return 1.0
    def description(self): return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self): return self._coffee.cost()
    def description(self): return self._coffee.description()

class Milk(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.25
    def description(self): return self._coffee.description() + ", Milk"

class Sugar(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.10
    def description(self): return self._coffee.description() + ", Sugar"

class Vanilla(CoffeeDecorator):
    def cost(self): return self._coffee.cost() + 0.50
    def description(self): return self._coffee.description() + ", Vanilla"

c = SimpleCoffee()
c = Milk(c)
c = Sugar(c)
c = Vanilla(c)
print(c.description())
print(f"Total: ${c.cost():.2f}")

# ----------------------------------------------------------
# 8. FACADE -- simple interface to complex subsystem
# ----------------------------------------------------------
print("\n=== 8. FACADE ===")

class CPU2:
    def freeze(self): return "CPU frozen"
    def jump(self, addr): return f"CPU jump to {addr}"
    def execute(self): return "CPU executing"

class Memory:
    def load(self, addr, data): return f"Memory: loaded {data!r} at {addr}"

class HardDrive:
    def read(self, sector, size): return f"HDD: read {size}bytes from sector {sector}"

class ComputerFacade:   # simplifies boot sequence
    def __init__(self):
        self.cpu    = CPU2()
        self.memory = Memory()
        self.hdd    = HardDrive()

    def start(self):
        steps = [
            self.cpu.freeze(),
            self.memory.load(0x00, self.hdd.read(0, 1024)),
            self.cpu.jump(0x00),
            self.cpu.execute()
        ]
        return "Boot complete:\n" + "\n".join(f"  {s}" for s in steps)

fc = ComputerFacade()
print(fc.start())

# ----------------------------------------------------------
# 9. PROXY -- control access to an object
# ----------------------------------------------------------
print("\n=== 9. PROXY ===")

class RealDatabase:
    def query(self, sql):
        return f"DB result for: {sql}"

class DatabaseProxy:
    def __init__(self, user_role):
        self._db   = RealDatabase()
        self._role = user_role
        self._cache = {}

    def query(self, sql):
        # Access control
        if self._role == "guest" and "DROP" in sql.upper():
            return "Access denied: guests cannot DROP tables"
        # Caching
        if sql in self._cache:
            return f"[CACHED] {self._cache[sql]}"
        result = self._db.query(sql)
        self._cache[sql] = result
        return result

proxy_admin = DatabaseProxy("admin")
proxy_guest = DatabaseProxy("guest")

print(proxy_admin.query("SELECT * FROM users"))
print(proxy_admin.query("SELECT * FROM users"))  # cached
print(proxy_guest.query("DROP TABLE users"))     # denied

# ----------------------------------------------------------
# 10. COMPOSITE -- tree structures
# ----------------------------------------------------------
print("\n=== 10. COMPOSITE ===")

class FileSystemItem(ABC):
    @abstractmethod
    def size(self): pass
    @abstractmethod
    def display(self, indent=0): pass

class File(FileSystemItem):
    def __init__(self, name, size_kb):
        self.name = name; self._size = size_kb

    def size(self): return self._size

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self._size}KB)")

class Folder(FileSystemItem):
    def __init__(self, name):
        self.name     = name
        self.children = []

    def add(self, item): self.children.append(item); return self

    def size(self): return sum(c.size() for c in self.children)

    def display(self, indent=0):
        print(" " * indent + f"Folder: {self.name}/ [{self.size()}KB]")
        for c in self.children:
            c.display(indent + 2)

root = Folder("root")
docs = Folder("Documents")
imgs = Folder("Images")

docs.add(File("resume.pdf", 200)).add(File("notes.txt", 5))
imgs.add(File("photo.jpg", 3000)).add(File("icon.png", 50))
root.add(docs).add(imgs).add(File("config.yml", 2))

root.display()

# ==========================================================
# BEHAVIOURAL PATTERNS
# ==========================================================

# ----------------------------------------------------------
# 11. OBSERVER -- publish / subscribe event system
# ----------------------------------------------------------
print("\n=== 11. OBSERVER ===")

class EventSystem:
    def __init__(self):
        self._listeners = {}

    def subscribe(self, event, listener):
        self._listeners.setdefault(event, []).append(listener)

    def unsubscribe(self, event, listener):
        if event in self._listeners:
            self._listeners[event].remove(listener)

    def notify(self, event, data=None):
        for listener in self._listeners.get(event, []):
            listener(data)

class Store:
    def __init__(self, name):
        self.name   = name
        self.events = EventSystem()

    def new_item(self, item, price):
        print(f"\n  Store: new item '{item}' at ${price}")
        self.events.notify("new_item", {"item": item, "price": price})

    def price_change(self, item, old, new):
        print(f"\n  Store: '{item}' price ${old} -> ${new}")
        self.events.notify("price_change", {"item":item,"old":old,"new":new})

def email_customer(data):
    print(f"  [Email] Dear customer: {data}")

def log_event(data):
    print(f"  [Log] Event recorded: {data}")

store = Store("TechShop")
store.events.subscribe("new_item", email_customer)
store.events.subscribe("new_item", log_event)
store.events.subscribe("price_change", email_customer)

store.new_item("Laptop", 999)
store.price_change("Laptop", 999, 899)

# ----------------------------------------------------------
# 12. STRATEGY -- swappable algorithms
# ----------------------------------------------------------
print("\n=== 12. STRATEGY ===")

class Compressor(ABC):
    @abstractmethod
    def compress(self, data: str) -> str: pass

class ZipCompressor(Compressor):
    def compress(self, data):
        return f"ZIP({len(data)} bytes -> {len(data)//2} bytes)"

class GzipCompressor(Compressor):
    def compress(self, data):
        return f"GZIP({len(data)} bytes -> {len(data)//3} bytes)"

class FileCompressor:
    def __init__(self, strategy: Compressor):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def compress(self, data):
        return self._strategy.compress(data)

fc2 = FileCompressor(ZipCompressor())
print(fc2.compress("A" * 1000))
fc2.set_strategy(GzipCompressor())
print(fc2.compress("A" * 1000))

# ----------------------------------------------------------
# 13. TEMPLATE METHOD -- skeleton algorithm in base class
# ----------------------------------------------------------
print("\n=== 13. TEMPLATE METHOD ===")

class DataMiner(ABC):
    def mine(self, path):       # TEMPLATE METHOD
        raw  = self.extract(path)
        data = self.parse(raw)
        result = self.analyze(data)
        self.report(result)

    @abstractmethod
    def extract(self, path): pass

    @abstractmethod
    def parse(self, raw): pass

    def analyze(self, data):    # default implementation
        return f"analysis of {len(data)} items"

    def report(self, result):   # hook -- can be overridden
        print(f"  Report: {result}")

class CSVMiner(DataMiner):
    def extract(self, path): return f"raw CSV from {path}"
    def parse(self, raw):    return raw.split(',')

class JSONMiner(DataMiner):
    def extract(self, path): return f'{{"data": [1,2,3]}}'
    def parse(self, raw):    return [1, 2, 3]
    def report(self, result): print(f"  [JSON Report] {result}")

CSVMiner().mine("data.csv")
JSONMiner().mine("data.json")

# ----------------------------------------------------------
# 14. COMMAND -- encapsulate actions as objects
# ----------------------------------------------------------
print("\n=== 14. COMMAND ===")

class Command(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass

class TextEditor:
    def __init__(self): self.text = ""
    def __str__(self): return repr(self.text)

class TypeCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text   = text

    def execute(self):
        self.editor.text += self.text

    def undo(self):
        self.editor.text = self.editor.text[:-len(self.text)]

class DeleteCommand(Command):
    def __init__(self, editor, n):
        self.editor  = editor
        self.n       = n
        self._deleted = ""

    def execute(self):
        self._deleted = self.editor.text[-self.n:]
        self.editor.text = self.editor.text[:-self.n]

    def undo(self):
        self.editor.text += self._deleted

class CommandHistory:
    def __init__(self): self._history = []

    def execute(self, cmd):
        cmd.execute()
        self._history.append(cmd)

    def undo(self):
        if self._history:
            self._history.pop().undo()

ed = TextEditor()
hist = CommandHistory()
hist.execute(TypeCommand(ed, "Hello"))
hist.execute(TypeCommand(ed, ", World"))
print("After typing:", ed)
hist.execute(DeleteCommand(ed, 6))
print("After delete:", ed)
hist.undo()
print("After undo:", ed)
hist.undo()
print("After undo:", ed)

# ----------------------------------------------------------
# 15. ITERATOR PATTERN
# ----------------------------------------------------------
print("\n=== 15. ITERATOR ===")

class TreeNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None

class InOrderIterator:
    def __init__(self, root):
        self._stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self._stack.append(node)
            node = node.left

    def __iter__(self): return self

    def __next__(self):
        if not self._stack:
            raise StopIteration
        node = self._stack.pop()
        self._push_left(node.right)
        return node.val

# Build tree:   4
#              / \
#             2   6
#            / \ / \
#           1  3 5  7
root = TreeNode(4)
root.left       = TreeNode(2)
root.right      = TreeNode(6)
root.left.left  = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right= TreeNode(7)

print("In-order traversal:", list(InOrderIterator(root)))  # [1,2,3,4,5,6,7]

print("\n[Y] Design Patterns done!")
