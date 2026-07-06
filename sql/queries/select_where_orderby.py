import sqlite3

class SelectWhereOrderBy:
    """
    DQL (Data Query Language) basics — SELECT, WHERE, ORDER BY, LIMIT,
    DISTINCT, and the common WHERE-clause operators.

    SELECT   — chooses which columns to return (or * for all)
    WHERE    — filters rows BEFORE any grouping happens
    ORDER BY — sorts the result set (ASC default, or DESC)
    LIMIT    — caps the number of rows returned
    DISTINCT — removes duplicate rows from the result
    LIKE     — pattern match ('%' = any sequence, '_' = any single char)
    BETWEEN  — inclusive range check
    IN       — value is one of a given set
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("""
            CREATE TABLE employees (
                id INTEGER PRIMARY KEY, name TEXT, department TEXT,
                salary REAL, age INTEGER
            )
        """)
        self.conn.executemany(
            "INSERT INTO employees (name, department, salary, age) VALUES (?, ?, ?, ?)",
            [
                ("Alice", "Engineering", 95000, 29),
                ("Bob",   "Engineering", 85000, 34),
                ("Carol", "Sales",       65000, 41),
                ("Dave",  "Sales",       60000, 25),
                ("Eve",   "Marketing",   70000, 30),
            ],
        )

    def select_all(self) -> list:
        return self.conn.execute("SELECT name, department FROM employees").fetchall()

    def where_equals(self, department: str) -> list:
        return self.conn.execute(
            "SELECT name FROM employees WHERE department = ?", (department,)
        ).fetchall()

    def where_comparison(self, min_salary: float) -> list:
        return self.conn.execute(
            "SELECT name FROM employees WHERE salary >= ?", (min_salary,)
        ).fetchall()

    def where_between(self, lo: int, hi: int) -> list:
        return self.conn.execute(
            "SELECT name FROM employees WHERE age BETWEEN ? AND ?", (lo, hi)
        ).fetchall()

    def where_in(self, departments: list) -> list:
        placeholders = ",".join("?" for _ in departments)
        return self.conn.execute(
            f"SELECT name FROM employees WHERE department IN ({placeholders})", departments
        ).fetchall()

    def where_like(self, pattern: str) -> list:
        return self.conn.execute(
            "SELECT name FROM employees WHERE name LIKE ?", (pattern,)
        ).fetchall()

    def order_by_salary(self, descending: bool = False) -> list:
        direction = "DESC" if descending else "ASC"
        return self.conn.execute(
            f"SELECT name, salary FROM employees ORDER BY salary {direction}"
        ).fetchall()

    def top_n_by_salary(self, n: int) -> list:
        return self.conn.execute(
            "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT ?", (n,)
        ).fetchall()

    def distinct_departments(self) -> list:
        return [row[0] for row in self.conn.execute("SELECT DISTINCT department FROM employees").fetchall()]


swo = SelectWhereOrderBy()
print("Engineering:", swo.where_equals("Engineering"))
print("Salary >= 70000:", swo.where_comparison(70000))
print("Age between 25 and 30:", swo.where_between(25, 30))
print("Top 2 salaries:", swo.top_n_by_salary(2))
print("Distinct departments:", swo.distinct_departments())
