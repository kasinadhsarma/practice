-- ============================================================
-- Every SQL join type
-- ============================================================
--   INNER JOIN      — only rows with a match on BOTH sides
--   LEFT JOIN       — every row from the left table, NULL where
--                      there's no match on the right
--   RIGHT JOIN      — mirror of LEFT JOIN — every row from the right
--   FULL OUTER JOIN — every row from BOTH sides, NULLs where unmatched
--   CROSS JOIN      — full Cartesian product (every row x every row)
--   SELF JOIN       — a table joined to itself
--
-- Note: RIGHT JOIN and FULL OUTER JOIN require SQLite 3.39+ (2022).
-- ============================================================

CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER, item TEXT);

INSERT INTO customers (id, name) VALUES
    (1, 'Alice'), (2, 'Bob'), (3, 'Carol');  -- Carol has no orders

INSERT INTO orders (customer_id, item) VALUES
    (1, 'Book'), (1, 'Pen'), (2, 'Laptop'), (99, 'Ghost Order');  -- 99 matches no customer

-- INNER JOIN: only customers who have orders, and only orders with a real customer
SELECT customers.name, orders.item
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
ORDER BY customers.name, orders.item;

-- LEFT JOIN: every customer, even Carol (with NULL for her missing order)
SELECT customers.name, orders.item
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
ORDER BY customers.name, orders.item;

-- RIGHT JOIN: every order, even the ghost order (with NULL for its missing customer)
SELECT customers.name, orders.item
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id
ORDER BY orders.item;

-- FULL OUTER JOIN: everything from both sides
SELECT customers.name, orders.item
FROM customers
FULL OUTER JOIN orders ON customers.id = orders.customer_id
ORDER BY customers.name, orders.item;

-- CROSS JOIN: Cartesian product — every customer paired with every order
SELECT customers.name, orders.item
FROM customers
CROSS JOIN orders
ORDER BY customers.name, orders.item;

-- SELF JOIN: find pairs of employees who share the same department
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, department TEXT);
INSERT INTO employees (name, department) VALUES
    ('Alice', 'Engineering'), ('Bob', 'Engineering'), ('Carol', 'Sales');

SELECT a.name, b.name
FROM employees a
JOIN employees b ON a.department = b.department AND a.id < b.id
ORDER BY a.name;
