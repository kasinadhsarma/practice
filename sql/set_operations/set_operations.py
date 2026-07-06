import sqlite3

class SetOperations:
    """
    Combine the results of two SELECT statements as if they were sets.
    Both sides must return the same number of columns with compatible
    types.

    UNION      — rows from either query, DUPLICATES REMOVED
    UNION ALL  — rows from either query, duplicates KEPT (faster — no
                 dedup pass required)
    INTERSECT  — only rows that appear in BOTH queries
    EXCEPT     — rows from the first query that do NOT appear in the second
                 (also called set difference; some databases call this MINUS)
    """

    def __init__(self):
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute("CREATE TABLE this_year (name TEXT)")
        self.conn.execute("CREATE TABLE last_year (name TEXT)")
        self.conn.executemany("INSERT INTO this_year (name) VALUES (?)",
                               [("Alice",), ("Bob",), ("Carol",)])
        self.conn.executemany("INSERT INTO last_year (name) VALUES (?)",
                               [("Bob",), ("Carol",), ("Dave",)])

    def union(self) -> list:
        """Everyone active in either year, no duplicates."""
        return sorted(row[0] for row in self.conn.execute("""
            SELECT name FROM this_year UNION SELECT name FROM last_year
        """).fetchall())

    def union_all(self) -> list:
        """Same as union(), but Bob and Carol appear twice (once per table)."""
        return sorted(row[0] for row in self.conn.execute("""
            SELECT name FROM this_year UNION ALL SELECT name FROM last_year
        """).fetchall())

    def intersect(self) -> list:
        """Active in BOTH years."""
        return sorted(row[0] for row in self.conn.execute("""
            SELECT name FROM this_year INTERSECT SELECT name FROM last_year
        """).fetchall())

    def except_(self) -> list:
        """New this year — active this year but NOT last year."""
        return sorted(row[0] for row in self.conn.execute("""
            SELECT name FROM this_year EXCEPT SELECT name FROM last_year
        """).fetchall())

    def churned(self) -> list:
        """Active last year but NOT this year (EXCEPT the other direction)."""
        return sorted(row[0] for row in self.conn.execute("""
            SELECT name FROM last_year EXCEPT SELECT name FROM this_year
        """).fetchall())


so = SetOperations()
print("UNION:", so.union())
print("UNION ALL:", so.union_all())
print("INTERSECT:", so.intersect())
print("EXCEPT (new this year):", so.except_())
print("EXCEPT (churned):", so.churned())
