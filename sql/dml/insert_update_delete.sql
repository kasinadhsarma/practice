-- ============================================================
-- DML: INSERT, UPDATE, DELETE
-- ============================================================
-- These are the three statements that change ROWS in a table (as
-- opposed to DDL, which changes the table's structure).
--   INSERT — adds new rows
--   UPDATE — modifies existing rows (ALWAYS pair with WHERE, or every
--            row in the table gets updated)
--   DELETE — removes rows (ALWAYS pair with WHERE, or the whole table
--            is emptied)
-- ============================================================

CREATE TABLE accounts (
    id      INTEGER PRIMARY KEY,
    name    TEXT NOT NULL,
    balance REAL NOT NULL DEFAULT 0
);

-- Insert a single row, columns named explicitly
INSERT INTO accounts (name, balance) VALUES ('Alice', 100.0);

-- Insert multiple rows in one statement
INSERT INTO accounts (name, balance) VALUES ('Bob', 50.0), ('Carol', 200.0);

SELECT name, balance FROM accounts ORDER BY id;

-- Update one row (the WHERE clause is what makes this targeted)
UPDATE accounts SET balance = 75.0 WHERE name = 'Bob';

SELECT name, balance FROM accounts ORDER BY id;

-- Update EVERY row — no WHERE clause, applies interest to all accounts
UPDATE accounts SET balance = balance * 1.10;

SELECT name, balance FROM accounts ORDER BY id;

-- Delete a specific row
DELETE FROM accounts WHERE name = 'Carol';

-- Delete every row below a threshold
DELETE FROM accounts WHERE balance < 50;

SELECT name, balance FROM accounts ORDER BY id;
