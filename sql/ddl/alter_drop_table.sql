-- ============================================================
-- DDL: ALTER TABLE and DROP TABLE
-- ============================================================
-- ALTER TABLE modifies an existing table's structure without losing
-- its data. SQLite supports ADD COLUMN, RENAME COLUMN, RENAME TO, and
-- DROP COLUMN (added in SQLite 3.35). It does NOT support directly
-- changing a column's type or adding constraints after creation.
--
-- DROP TABLE permanently deletes a table and all its data.
-- ============================================================

CREATE TABLE employees (
    id   INTEGER PRIMARY KEY,
    name TEXT
);

INSERT INTO employees (name) VALUES ('Alice'), ('Bob');

-- Add a new column
ALTER TABLE employees ADD COLUMN department TEXT;

-- Rename a column
ALTER TABLE employees RENAME COLUMN department TO dept;

-- Rename the table itself
ALTER TABLE employees RENAME TO staff;

-- Drop a column (SQLite 3.35+)
ALTER TABLE staff DROP COLUMN dept;

-- Inspect the resulting schema
PRAGMA table_info(staff);

-- Permanently delete the table (IF EXISTS avoids an error if it's already gone)
DROP TABLE IF EXISTS staff;

-- Confirm it's gone
SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'staff';
