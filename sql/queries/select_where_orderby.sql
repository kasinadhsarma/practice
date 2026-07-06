-- ============================================================
-- DQL basics: SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
-- ============================================================
--   SELECT   — chooses which columns to return (or * for all)
--   WHERE    — filters rows BEFORE any grouping happens
--   ORDER BY — sorts the result set (ASC default, or DESC)
--   LIMIT    — caps the number of rows returned
--   DISTINCT — removes duplicate rows from the result
--   LIKE     — pattern match ('%' = any sequence, '_' = any single char)
--   BETWEEN  — inclusive range check
--   IN       — value is one of a given set
-- ============================================================

CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT, department TEXT,
    salary REAL, age INTEGER
);

INSERT INTO employees (name, department, salary, age) VALUES
    ('Alice', 'Engineering', 95000, 29),
    ('Bob',   'Engineering', 85000, 34),
    ('Carol', 'Sales',       65000, 41),
    ('Dave',  'Sales',       60000, 25),
    ('Eve',   'Marketing',   70000, 30);

-- SELECT specific columns
SELECT name, department FROM employees;

-- WHERE: exact match
SELECT name FROM employees WHERE department = 'Engineering';

-- WHERE: comparison operator
SELECT name FROM employees WHERE salary >= 70000;

-- WHERE: BETWEEN (inclusive range)
SELECT name FROM employees WHERE age BETWEEN 25 AND 30;

-- WHERE: IN (matches any value in the list)
SELECT name FROM employees WHERE department IN ('Sales', 'Marketing');

-- WHERE: LIKE (pattern match — names starting with 'A')
SELECT name FROM employees WHERE name LIKE 'A%';

-- ORDER BY ascending (default) and descending
SELECT name, salary FROM employees ORDER BY salary ASC;
SELECT name, salary FROM employees ORDER BY salary DESC;

-- LIMIT: top 2 highest salaries
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2;

-- DISTINCT: unique department names only
SELECT DISTINCT department FROM employees;
