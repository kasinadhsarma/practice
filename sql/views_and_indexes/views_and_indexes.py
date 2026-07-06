import sqlite3

class ViewsAndIndexes:
    """
    VIEW  — a saved SELECT query that behaves like a virtual, read-through
            table. It doesn't store data itself; querying it re-runs the
            underlying SELECT. Useful for hiding complexity (joins,
            aggregates) behind a simple name.

    INDEX — a separate on-disk structure (typically a B-tree) that lets
            the database find matching rows without scanning the whole
            table. Speeds up WHERE/JOIN/ORDER BY on the indexed column(s)
            at the cost of extra storage and slower writes (every INSERT/
            UPDATE must also update the index).
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("""
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL
            )
        """)
        self.conn.executemany(
            "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
            [
                ("Alice", "Engineering", 95000),
                ("Bob",   "Engineering", 85000),
                ("Carol", "Sales",       65000),
            ],
        )

    def create_view(self):
        self.conn.execute("""
            CREATE VIEW high_earners AS
            SELECT name, department, salary FROM employees WHERE salary > 70000
        """)

    def query_view(self) -> list:
        return self.conn.execute("SELECT name FROM high_earners ORDER BY name").fetchall()

    def view_reflects_new_data(self):
        """Views are NOT snapshots — inserting a row makes it show up immediately."""
        self.conn.execute(
            "INSERT INTO employees (name, department, salary) VALUES ('Dave', 'Sales', 90000)"
        )

    def drop_view(self):
        self.conn.execute("DROP VIEW IF EXISTS high_earners")

    def create_index(self):
        self.conn.execute("CREATE INDEX idx_department ON employees(department)")

    def list_indexes(self) -> list:
        cur = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='employees'"
        )
        return [row[0] for row in cur.fetchall()]

    def uses_index_for_query(self, department: str) -> str:
        """Returns SQLite's query plan text — shows whether it used the
        index ('SEARCH ... USING INDEX') or scanned the whole table
        ('SCAN')."""
        plan = self.conn.execute(
            f"EXPLAIN QUERY PLAN SELECT * FROM employees WHERE department = '{department}'"
        ).fetchall()
        return " | ".join(row[-1] for row in plan)


vai = ViewsAndIndexes()
vai.create_view()
print("High earners (view):", vai.query_view())
vai.view_reflects_new_data()
print("High earners after insert (view updates live):", vai.query_view())

print("\nQuery plan before index:", vai.uses_index_for_query("Sales"))
vai.create_index()
print("Indexes on employees:", vai.list_indexes())
print("Query plan after index:", vai.uses_index_for_query("Sales"))
