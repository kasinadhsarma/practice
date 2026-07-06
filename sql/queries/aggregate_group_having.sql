-- ============================================================
-- Aggregate functions, GROUP BY, and HAVING
-- ============================================================
-- Aggregate functions (COUNT, SUM, AVG, MIN, MAX) collapse many rows
-- into a single summary value. GROUP BY partitions rows into buckets
-- (one per distinct value of the grouped column) and applies the
-- aggregate WITHIN each bucket instead of across the whole table.
--
--   WHERE  filters individual rows BEFORE grouping happens.
--   HAVING filters GROUPS after aggregation — it can reference the
--          aggregate result itself, which WHERE cannot do.
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

-- Aggregate over the whole table
SELECT COUNT(*) AS total_employees FROM employees;
SELECT SUM(salary) AS total_salary FROM employees;
SELECT AVG(salary) AS average_salary FROM employees;
SELECT MIN(salary) AS lowest, MAX(salary) AS highest FROM employees;

-- GROUP BY: aggregate per department
SELECT department, COUNT(*) AS headcount
FROM employees
GROUP BY department
ORDER BY department;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY department;

-- HAVING: filter groups by their aggregate result (WHERE cannot do this)
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING avg_salary > 70000
ORDER BY department;

-- HAVING with COUNT: departments with more than one employee
SELECT department, COUNT(*) AS cnt
FROM employees
GROUP BY department
HAVING cnt > 1;
