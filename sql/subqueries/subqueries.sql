-- ============================================================
-- Subqueries: scalar, IN, correlated, EXISTS, subquery-in-FROM
-- ============================================================
--   Scalar subquery      — returns a single value, used like an expression
--   Subquery with IN     — returns a set of values, checked with IN
--   Correlated subquery  — references a column from the OUTER query, so
--                          it re-runs once per outer row
--   EXISTS               — checks only whether the subquery returns ANY
--                          row at all
--   Subquery in FROM      — a subquery treated as a temporary/derived table
-- ============================================================

CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL
);

INSERT INTO employees (name, department, salary) VALUES
    ('Alice', 'Engineering', 95000),
    ('Bob',   'Engineering', 85000),
    ('Carol', 'Sales',       65000),
    ('Dave',  'Sales',       60000),
    ('Eve',   'Marketing',   70000);

-- Scalar subquery: compare each row against a single computed value
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
ORDER BY name;

-- Subquery with IN
SELECT name FROM employees
WHERE department IN ('Sales', 'Marketing')
ORDER BY name;

-- Correlated subquery: inner query references the outer row's department,
-- so it re-evaluates for every outer row
SELECT e.name, e.department, e.salary
FROM employees e
WHERE e.salary = (
    SELECT MAX(e2.salary) FROM employees e2 WHERE e2.department = e.department
)
ORDER BY e.department;

-- EXISTS: true if the correlated subquery returns at least one row
SELECT DISTINCT department FROM employees e
WHERE EXISTS (
    SELECT 1 FROM employees e2
    WHERE e2.department = e.department AND e2.salary > 90000
)
ORDER BY department;

-- Subquery in FROM (a "derived table"): query an aggregate result further
SELECT department, avg_salary FROM (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees GROUP BY department
)
WHERE avg_salary > 65000
ORDER BY department;
