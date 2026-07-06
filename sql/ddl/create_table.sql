-- ============================================================
-- DDL: CREATE TABLE
-- ============================================================
-- Defines the shape of data: column names, types, and constraints.
--   PRIMARY KEY  — uniquely identifies each row, implies NOT NULL + UNIQUE
--   NOT NULL     — column may not be NULL
--   UNIQUE       — no two rows may share this value
--   DEFAULT      — value used when none is supplied on INSERT
--   CHECK        — arbitrary boolean condition every row must satisfy
--   FOREIGN KEY  — value must exist in the referenced table's column
-- ============================================================

PRAGMA foreign_keys = ON;

-- Basic table: primary key + required column
CREATE TABLE authors (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Table with a foreign key referencing authors(id)
CREATE TABLE books (
    id        INTEGER PRIMARY KEY,
    title     TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Table with UNIQUE, CHECK, and DEFAULT constraints
CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    sku      TEXT UNIQUE NOT NULL,
    price    REAL CHECK (price >= 0),
    quantity INTEGER DEFAULT 0
);

-- List every table in the database
SELECT name FROM sqlite_master WHERE type = 'table';

-- Inspect a table's column definitions
PRAGMA table_info(products);

-- This INSERT violates CHECK (price >= 0) and will be rejected:
-- INSERT INTO products (sku, price) VALUES ('BAD-1', -5);

-- This INSERT violates UNIQUE (sku) if run twice with the same sku:
INSERT INTO products (sku, price, quantity) VALUES ('SKU-001', 19.99, 100);
-- INSERT INTO products (sku, price, quantity) VALUES ('SKU-001', 25.00, 50);  -- would fail
