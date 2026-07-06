-- ============================================================
-- Window functions
-- ============================================================
-- Compute a value across a set of related rows ("the window") WITHOUT
-- collapsing those rows into one (unlike GROUP BY). PARTITION BY splits
-- rows into groups (rows stay separate); ORDER BY inside OVER defines
-- the row sequence used by ranking/offset functions.
--
--   ROW_NUMBER() — sequential number per partition, no ties (1,2,3,4)
--   RANK()       — same rank for ties, gaps afterward (1,2,2,4)
--   DENSE_RANK() — same rank for ties, no gaps afterward (1,2,2,3)
--   LAG/LEAD     — value from n rows before/after the current row
--   SUM() OVER   — running total when ordered, without collapsing rows
-- ============================================================

CREATE TABLE sales (
    id INTEGER PRIMARY KEY, region TEXT, salesperson TEXT,
    amount REAL, sale_date TEXT
);

INSERT INTO sales (region, salesperson, amount, sale_date) VALUES
    ('East', 'Alice', 500, '2024-01-01'),
    ('East', 'Bob',   500, '2024-01-02'),
    ('East', 'Alice', 300, '2024-01-03'),
    ('West', 'Carol', 700, '2024-01-01'),
    ('West', 'Dave',  400, '2024-01-02');

-- ROW_NUMBER: unique sequence per region, ordered by amount descending
SELECT region, salesperson, amount,
       ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn
FROM sales ORDER BY region, rn;

-- RANK: ties share a rank, but the next rank leaves a gap
SELECT region, salesperson, amount,
       RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rnk
FROM sales ORDER BY region, rnk;

-- DENSE_RANK: ties share a rank, no gap afterward
SELECT region, salesperson, amount,
       DENSE_RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS drnk
FROM sales ORDER BY region, drnk;

-- LAG / LEAD: look at the previous/next row within the same partition
SELECT region, sale_date, amount,
       LAG(amount, 1) OVER (PARTITION BY region ORDER BY sale_date) AS prev_amount,
       LEAD(amount, 1) OVER (PARTITION BY region ORDER BY sale_date) AS next_amount
FROM sales ORDER BY region, sale_date;

-- Running total per region, ordered by date
SELECT region, sale_date, amount,
       SUM(amount) OVER (PARTITION BY region ORDER BY sale_date
                          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM sales ORDER BY region, sale_date;
