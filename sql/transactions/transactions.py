import sqlite3

class Transactions:
    """
    A transaction groups multiple statements into one all-or-nothing
    unit of work — the classic use case is a bank transfer, where
    debiting one account and crediting another must either BOTH happen
    or NEITHER happen.

    BEGIN    — starts a transaction
    COMMIT   — makes every change since BEGIN permanent
    ROLLBACK — undoes every change since BEGIN, as if it never happened

    This demonstrates the "Atomicity" and "Consistency" letters of ACID
    (Atomicity, Consistency, Isolation, Durability): a failed transfer
    never leaves money debited from one account without being credited
    to the other.

    Note: isolation_level=None puts Python's sqlite3 driver in autocommit
    mode, so BEGIN/COMMIT/ROLLBACK behave exactly like raw SQL instead of
    being wrapped by Python's own implicit transaction handling.
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:', isolation_level=None)
        self.conn.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance REAL)")
        self.conn.executemany("INSERT INTO accounts VALUES (?, ?)", [
            ("Alice", 100.0), ("Bob", 50.0),
        ])

    def balance_of(self, name: str) -> float:
        return self.conn.execute("SELECT balance FROM accounts WHERE name = ?", (name,)).fetchone()[0]

    def transfer_committed(self, sender: str, receiver: str, amount: float):
        self.conn.execute("BEGIN")
        self.conn.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
        self.conn.execute("UPDATE accounts SET balance = balance + ? WHERE name = ?", (amount, receiver))
        self.conn.execute("COMMIT")

    def transfer_rolled_back(self, sender: str, receiver: str, amount: float):
        """Simulates a failure partway through the transfer (e.g. a
        constraint violation or application error) and rolls back —
        neither balance should change."""
        self.conn.execute("BEGIN")
        self.conn.execute("UPDATE accounts SET balance = balance - ? WHERE name = ?", (amount, sender))
        # ... imagine an error is detected here before the credit happens ...
        self.conn.execute("ROLLBACK")


tx = Transactions()
print("Before transfer - Alice:", tx.balance_of("Alice"), "Bob:", tx.balance_of("Bob"))
tx.transfer_committed("Alice", "Bob", 30.0)
print("After committed transfer - Alice:", tx.balance_of("Alice"), "Bob:", tx.balance_of("Bob"))
tx.transfer_rolled_back("Alice", "Bob", 1000.0)
print("After rolled-back transfer - Alice:", tx.balance_of("Alice"), "Bob:", tx.balance_of("Bob"))
