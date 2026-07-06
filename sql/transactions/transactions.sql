-- ============================================================
-- Transactions: BEGIN, COMMIT, ROLLBACK
-- ============================================================
-- A transaction groups multiple statements into one all-or-nothing
-- unit of work. Classic example: a bank transfer, where debiting one
-- account and crediting another must either BOTH happen or NEITHER.
-- This demonstrates the "Atomicity" and "Consistency" of ACID
-- (Atomicity, Consistency, Isolation, Durability).
-- ============================================================

CREATE TABLE accounts (name TEXT PRIMARY KEY, balance REAL);
INSERT INTO accounts VALUES ('Alice', 100.0), ('Bob', 50.0);

SELECT * FROM accounts;

-- A committed transfer: both updates become permanent together
BEGIN;
UPDATE accounts SET balance = balance - 30.0 WHERE name = 'Alice';
UPDATE accounts SET balance = balance + 30.0 WHERE name = 'Bob';
COMMIT;

SELECT * FROM accounts;  -- Alice: 70.0, Bob: 80.0

-- A rolled-back transfer: imagine an error is detected partway through —
-- ROLLBACK undoes every change since BEGIN, as if it never happened
BEGIN;
UPDATE accounts SET balance = balance - 1000.0 WHERE name = 'Alice';
-- ... error detected here, before crediting anyone ...
ROLLBACK;

SELECT * FROM accounts;  -- unchanged: Alice: 70.0, Bob: 80.0
