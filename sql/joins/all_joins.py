import sqlite3

class AllJoins:
    """
    Every SQL join type, demonstrated on two small tables: customers and
    orders, where not every customer has an order and not every order's
    customer_id matches an existing customer (to make LEFT/RIGHT/FULL
    actually show a difference from INNER).

    INNER JOIN      — only rows with a match on BOTH sides
    LEFT JOIN       — every row from the left table, matched columns
                       NULL where there's no match on the right
    RIGHT JOIN      — mirror of LEFT JOIN — every row from the right table
    FULL OUTER JOIN — every row from BOTH sides, NULLs where unmatched
    CROSS JOIN      — the full Cartesian product (every row x every row)
    SELF JOIN       — a table joined to itself, e.g. to compare rows
                       against other rows in the same table

    Note: RIGHT JOIN and FULL OUTER JOIN require SQLite 3.39+ (2022).
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, item TEXT)")
        self.conn.executemany("INSERT INTO customers (id, name) VALUES (?, ?)", [
            (1, "Alice"), (2, "Bob"), (3, "Carol"),   # Carol has no orders
        ])
        self.conn.executemany("INSERT INTO orders (customer_id, item) VALUES (?, ?)", [
            (1, "Book"), (1, "Pen"), (2, "Laptop"), (99, "Ghost Order"),  # 99 matches no customer
        ])

    def inner_join(self) -> list:
        return self.conn.execute("""
            SELECT customers.name, orders.item
            FROM customers
            INNER JOIN orders ON customers.id = orders.customer_id
            ORDER BY customers.name, orders.item
        """).fetchall()

    def left_join(self) -> list:
        return self.conn.execute("""
            SELECT customers.name, orders.item
            FROM customers
            LEFT JOIN orders ON customers.id = orders.customer_id
            ORDER BY customers.name, orders.item
        """).fetchall()

    def right_join(self) -> list:
        return self.conn.execute("""
            SELECT customers.name, orders.item
            FROM customers
            RIGHT JOIN orders ON customers.id = orders.customer_id
            ORDER BY orders.item
        """).fetchall()

    def full_outer_join(self) -> list:
        return self.conn.execute("""
            SELECT customers.name, orders.item
            FROM customers
            FULL OUTER JOIN orders ON customers.id = orders.customer_id
            ORDER BY customers.name, orders.item
        """).fetchall()

    def cross_join(self) -> list:
        return self.conn.execute("""
            SELECT customers.name, orders.item
            FROM customers
            CROSS JOIN orders
            ORDER BY customers.name, orders.item
        """).fetchall()

    def self_join_same_department(self) -> list:
        """Find pairs of employees who share the same department (self join)."""
        self.conn.execute("""
            CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT)
        """)
        self.conn.executemany("INSERT INTO employees (name, department) VALUES (?, ?)", [
            ("Alice", "Engineering"), ("Bob", "Engineering"), ("Carol", "Sales"),
        ])
        return self.conn.execute("""
            SELECT a.name, b.name
            FROM employees a
            JOIN employees b ON a.department = b.department AND a.id < b.id
            ORDER BY a.name
        """).fetchall()


joins = AllJoins()
print("INNER JOIN:", joins.inner_join())
print("LEFT JOIN:", joins.left_join())
print("RIGHT JOIN:", joins.right_join())
print("FULL OUTER JOIN:", joins.full_outer_join())
print("SELF JOIN (same department):", joins.self_join_same_department())
