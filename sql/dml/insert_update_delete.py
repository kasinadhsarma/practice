import sqlite3

class InsertUpdateDelete:
    """
    DML (Data Manipulation Language) — INSERT, UPDATE, DELETE.

    These are the three statements that change the ROWS in a table
    (as opposed to DDL, which changes the table's structure).

    INSERT — adds new rows. Can specify columns explicitly or supply
             values for every column in declared order; multiple rows
             can be inserted in one statement.
    UPDATE — modifies existing rows. ALWAYS pair with WHERE, or every
             row in the table gets updated.
    DELETE — removes rows. Also ALWAYS pair with WHERE, or the whole
             table is emptied.
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("""
            CREATE TABLE accounts (
                id      INTEGER PRIMARY KEY,
                name    TEXT NOT NULL,
                balance REAL NOT NULL DEFAULT 0
            )
        """)

    def insert_single(self, name: str, balance: float):
        self.conn.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))

    def insert_many(self, rows: list):
        self.conn.executemany("INSERT INTO accounts (name, balance) VALUES (?, ?)", rows)

    def update_balance(self, name: str, new_balance: float):
        self.conn.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, name))

    def apply_interest(self, rate: float):
        """Updates every row — demonstrates why WHERE matters (or doesn't, here)."""
        self.conn.execute("UPDATE accounts SET balance = balance * (1 + ?)", (rate,))

    def delete_by_name(self, name: str):
        self.conn.execute("DELETE FROM accounts WHERE name = ?", (name,))

    def delete_below_balance(self, threshold: float):
        self.conn.execute("DELETE FROM accounts WHERE balance < ?", (threshold,))

    def all_accounts(self) -> list:
        cur = self.conn.execute("SELECT name, balance FROM accounts ORDER BY id")
        return cur.fetchall()


iud = InsertUpdateDelete()
iud.insert_single("Alice", 100.0)
iud.insert_many([("Bob", 50.0), ("Carol", 200.0)])
print("After inserts:", iud.all_accounts())
iud.update_balance("Bob", 75.0)
print("After update:", iud.all_accounts())
iud.delete_by_name("Carol")
print("After delete:", iud.all_accounts())
