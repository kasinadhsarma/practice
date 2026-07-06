import sqlite3

class AggregateGroupHaving:
    """
    Aggregate functions, GROUP BY, and HAVING.

    Aggregate functions (COUNT, SUM, AVG, MIN, MAX) collapse many rows
    into a single summary value. GROUP BY partitions rows into buckets
    (one per distinct value of the grouped column) and applies the
    aggregate WITHIN each bucket instead of across the whole table.

    WHERE  filters individual rows BEFORE grouping happens.
    HAVING filters GROUPS after aggregation — it can reference the
           aggregate result itself (e.g. "only departments with
           average salary above X"), which WHERE cannot do.
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
                ("Dave",  "Sales",       60000),
                ("Eve",   "Marketing",   70000),
            ],
        )

    def count_all(self) -> int:
        return self.conn.execute("SELECT COUNT(*) FROM employees").fetchone()[0]

    def total_salary(self) -> float:
        return self.conn.execute("SELECT SUM(salary) FROM employees").fetchone()[0]

    def average_salary(self) -> float:
        return self.conn.execute("SELECT AVG(salary) FROM employees").fetchone()[0]

    def salary_range(self) -> tuple:
        return self.conn.execute("SELECT MIN(salary), MAX(salary) FROM employees").fetchone()

    def count_by_department(self) -> list:
        return self.conn.execute(
            "SELECT department, COUNT(*) FROM employees GROUP BY department ORDER BY department"
        ).fetchall()

    def average_salary_by_department(self) -> list:
        return self.conn.execute(
            "SELECT department, AVG(salary) FROM employees GROUP BY department ORDER BY department"
        ).fetchall()

    def departments_above_average(self, threshold: float) -> list:
        return self.conn.execute(
            "SELECT department, AVG(salary) as avg_salary FROM employees "
            "GROUP BY department HAVING avg_salary > ? ORDER BY department",
            (threshold,),
        ).fetchall()

    def departments_with_multiple_employees(self) -> list:
        return self.conn.execute(
            "SELECT department, COUNT(*) as cnt FROM employees "
            "GROUP BY department HAVING cnt > 1"
        ).fetchall()


agh = AggregateGroupHaving()
print("Total employees:", agh.count_all())
print("Average salary:", agh.average_salary())
print("Count by department:", agh.count_by_department())
print("Departments with avg salary > 70000:", agh.departments_above_average(70000))
