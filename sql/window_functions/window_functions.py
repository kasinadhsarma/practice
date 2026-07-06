import sqlite3

class WindowFunctions:
    """
    Window functions compute a value across a set of rows ("the window")
    related to the current row, WITHOUT collapsing those rows into one
    (unlike GROUP BY aggregates). The OVER clause defines the window:
    PARTITION BY splits rows into groups (like GROUP BY, but rows stay
    separate), and ORDER BY within OVER defines the row sequence used
    by ranking/offset functions.

    ROW_NUMBER() — sequential number per partition, no ties (1,2,3,4...)
    RANK()       — same rank for ties, but leaves gaps afterward (1,2,2,4)
    DENSE_RANK() — same rank for ties, no gaps afterward (1,2,2,3)
    LAG(col, n)  — value from n rows BEFORE the current row
    LEAD(col, n) — value from n rows AFTER the current row
    SUM() OVER   — running total when ordered, without collapsing rows
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("""
            CREATE TABLE sales (
                id INTEGER PRIMARY KEY, region TEXT, salesperson TEXT,
                amount REAL, sale_date TEXT
            )
        """)
        self.conn.executemany(
            "INSERT INTO sales (region, salesperson, amount, sale_date) VALUES (?, ?, ?, ?)",
            [
                ("East", "Alice", 500, "2024-01-01"),
                ("East", "Bob",   500, "2024-01-02"),
                ("East", "Alice", 300, "2024-01-03"),
                ("West", "Carol", 700, "2024-01-01"),
                ("West", "Dave",  400, "2024-01-02"),
            ],
        )

    def row_number_per_region(self) -> list:
        return self.conn.execute("""
            SELECT region, salesperson, amount,
                   ROW_NUMBER() OVER (PARTITION BY region ORDER BY amount DESC) AS rn
            FROM sales ORDER BY region, rn
        """).fetchall()

    def rank_per_region(self) -> list:
        return self.conn.execute("""
            SELECT region, salesperson, amount,
                   RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS rnk
            FROM sales ORDER BY region, rnk
        """).fetchall()

    def dense_rank_per_region(self) -> list:
        return self.conn.execute("""
            SELECT region, salesperson, amount,
                   DENSE_RANK() OVER (PARTITION BY region ORDER BY amount DESC) AS drnk
            FROM sales ORDER BY region, drnk
        """).fetchall()

    def lag_lead_by_date(self) -> list:
        return self.conn.execute("""
            SELECT region, sale_date, amount,
                   LAG(amount, 1) OVER (PARTITION BY region ORDER BY sale_date) AS prev_amount,
                   LEAD(amount, 1) OVER (PARTITION BY region ORDER BY sale_date) AS next_amount
            FROM sales ORDER BY region, sale_date
        """).fetchall()

    def running_total_by_region(self) -> list:
        return self.conn.execute("""
            SELECT region, sale_date, amount,
                   SUM(amount) OVER (PARTITION BY region ORDER BY sale_date
                                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
            FROM sales ORDER BY region, sale_date
        """).fetchall()


wf = WindowFunctions()
print("ROW_NUMBER per region:", wf.row_number_per_region())
print("RANK per region:", wf.rank_per_region())
print("DENSE_RANK per region:", wf.dense_rank_per_region())
print("Running total by region:", wf.running_total_by_region())
