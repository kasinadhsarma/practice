import sqlite3

class Subqueries:
    """
    A subquery is a SELECT nested inside another SQL statement. Forms
    demonstrated here:

    Scalar subquery      — returns a single value, usable anywhere an
                            expression is expected (e.g. compared with =)
    Subquery with IN     — returns a set of values, checked with IN
    Correlated subquery  — references a column from the OUTER query, so
                            it re-runs once per outer row (unlike a plain
                            subquery, which runs once total)
    EXISTS               — checks only whether the subquery returns ANY
                            row at all, often faster than IN for large sets
    Subquery in FROM      — a subquery treated as a temporary table to
                            query further (sometimes called a "derived table")
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

    def above_average_salary(self) -> list:
        """Scalar subquery: compare each row against a single computed value."""
        return self.conn.execute("""
            SELECT name, salary FROM employees
            WHERE salary > (SELECT AVG(salary) FROM employees)
            ORDER BY name
        """).fetchall()

    def in_top_departments(self, departments: list) -> list:
        """Subquery with IN, built from a second table conceptually — here
        just a literal list, but the pattern generalises to any subquery
        that returns a column of values."""
        placeholders = ",".join("?" for _ in departments)
        return self.conn.execute(f"""
            SELECT name FROM employees
            WHERE department IN ({placeholders})
            ORDER BY name
        """, departments).fetchall()

    def highest_paid_per_department(self) -> list:
        """Correlated subquery: the inner query references the outer row's
        department, so it re-evaluates for every outer row."""
        return self.conn.execute("""
            SELECT e.name, e.department, e.salary
            FROM employees e
            WHERE e.salary = (
                SELECT MAX(e2.salary) FROM employees e2 WHERE e2.department = e.department
            )
            ORDER BY e.department
        """).fetchall()

    def departments_with_any_employee_over(self, threshold: float) -> list:
        """EXISTS: true if the correlated subquery returns at least one row."""
        return self.conn.execute("""
            SELECT DISTINCT department FROM employees e
            WHERE EXISTS (
                SELECT 1 FROM employees e2
                WHERE e2.department = e.department AND e2.salary > ?
            )
            ORDER BY department
        """, (threshold,)).fetchall()

    def department_averages_above(self, threshold: float) -> list:
        """Subquery in FROM: query a derived table built from an aggregate."""
        return self.conn.execute("""
            SELECT department, avg_salary FROM (
                SELECT department, AVG(salary) AS avg_salary
                FROM employees GROUP BY department
            )
            WHERE avg_salary > ?
            ORDER BY department
        """, (threshold,)).fetchall()


sq = Subqueries()
print("Above average salary:", sq.above_average_salary())
print("Highest paid per department:", sq.highest_paid_per_department())
print("Departments with anyone over 90000:", sq.departments_with_any_employee_over(90000))
print("Department averages above 65000:", sq.department_averages_above(65000))
