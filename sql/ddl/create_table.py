import sqlite3

class CreateTable:
    """
    DDL (Data Definition Language) — CREATE TABLE.

    Defines the shape of data: column names, types, and constraints.
    SQLite is dynamically typed (a column's declared type is a "type
    affinity", not strictly enforced) but constraints ARE enforced:
        PRIMARY KEY — uniquely identifies each row, implies NOT NULL + UNIQUE
        NOT NULL    — column may not be NULL
        UNIQUE      — no two rows may share this value
        DEFAULT     — value used when none is supplied on INSERT
        CHECK       — arbitrary boolean condition every row must satisfy
        FOREIGN KEY — value must exist in the referenced table's column
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("PRAGMA foreign_keys = ON")

    def create_basic_table(self):
        self.conn.execute("""
            CREATE TABLE authors (
                id   INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)

    def create_table_with_constraints(self):
        self.conn.execute("""
            CREATE TABLE products (
                id       INTEGER PRIMARY KEY,
                sku      TEXT UNIQUE NOT NULL,
                price    REAL CHECK (price >= 0),
                quantity INTEGER DEFAULT 0
            )
        """)

    def create_table_with_foreign_key(self):
        self.create_basic_table()
        self.conn.execute("""
            CREATE TABLE books (
                id        INTEGER PRIMARY KEY,
                title     TEXT NOT NULL,
                author_id INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        """)

    def list_tables(self) -> list:
        cur = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [row[0] for row in cur.fetchall()]

    def table_schema(self, table_name: str) -> list:
        """Each row: (col_index, name, type, notnull, default_value, is_pk)"""
        cur = self.conn.execute(f"PRAGMA table_info({table_name})")
        return cur.fetchall()


ct = CreateTable()
ct.create_table_with_foreign_key()
ct.create_table_with_constraints()
print("Tables:", ct.list_tables())
print("products schema:", ct.table_schema("products"))
