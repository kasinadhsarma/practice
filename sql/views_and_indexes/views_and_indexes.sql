-- ============================================================
-- Views and Indexes
-- ============================================================
-- VIEW  — a saved SELECT query that behaves like a virtual, read-through
--         table. It doesn't store data itself; querying it re-runs the
--         underlying SELECT every time.
-- INDEX — a separate on-disk structure (typically a B-tree) that lets
--         the database find matching rows without scanning the whole
--         table, at the cost of extra storage and slower writes.
-- ============================================================

CREATE TABLE employees (
    id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary REAL
);

INSERT INTO employees (name, department, salary) VALUES
    ('Alice', 'Engineering', 95000),
    ('Bob',   'Engineering', 85000),
    ('Carol', 'Sales',       65000);

-- Create a view: hides the WHERE clause behind a simple name
CREATE VIEW high_earners AS
SELECT name, department, salary FROM employees WHERE salary > 70000;

SELECT name FROM high_earners ORDER BY name;

-- Views are NOT snapshots — inserting a row makes it show up immediately
INSERT INTO employees (name, department, salary) VALUES ('Dave', 'Sales', 90000);

SELECT name FROM high_earners ORDER BY name;  -- Dave now appears

DROP VIEW IF EXISTS high_earners;

-- Before creating an index, this query does a full table scan
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE department = 'Sales';

CREATE INDEX idx_department ON employees(department);

-- After the index, the same query can use it instead of scanning every row
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE department = 'Sales';

-- List indexes defined on a table
SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = 'employees';
