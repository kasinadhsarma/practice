import sqlite3

class AlterDropTable:
    """
    DDL — ALTER TABLE and DROP TABLE.

    ALTER TABLE modifies an existing table's structure without losing
    its data. SQLite supports a subset of the standard ALTER TABLE
    operations: ADD COLUMN, RENAME COLUMN, RENAME TO (the table itself),
    and DROP COLUMN (added in SQLite 3.35). It does NOT support directly
    modifying a column's type or adding constraints after creation —
    that requires create-new-table-and-copy-data instead.

    DROP TABLE permanently deletes a table and all its data.
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.execute("INSERT INTO employees (name) VALUES ('Alice'), ('Bob')")

    def add_column(self, column_name: str, column_type: str):
        self.conn.execute(f"ALTER TABLE employees ADD COLUMN {column_name} {column_type}")

    def rename_column(self, old_name: str, new_name: str):
        self.conn.execute(f"ALTER TABLE employees RENAME COLUMN {old_name} TO {new_name}")

    def rename_table(self, new_name: str):
        self.conn.execute(f"ALTER TABLE employees RENAME TO {new_name}")

    def drop_column(self, column_name: str):
        self.conn.execute(f"ALTER TABLE employees DROP COLUMN {column_name}")

    def drop_table(self, table_name: str):
        self.conn.execute(f"DROP TABLE IF EXISTS {table_name}")

    def columns_of(self, table_name: str) -> list:
        cur = self.conn.execute(f"PRAGMA table_info({table_name})")
        return [row[1] for row in cur.fetchall()]

    def table_exists(self, table_name: str) -> bool:
        cur = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
        )
        return cur.fetchone() is not None


adt = AlterDropTable()
adt.add_column("department", "TEXT")
print("Columns after ADD COLUMN:", adt.columns_of("employees"))
adt.rename_column("department", "dept")
print("Columns after RENAME COLUMN:", adt.columns_of("employees"))
adt.drop_table("employees")
print("employees exists after DROP TABLE:", adt.table_exists("employees"))
