# 🗄️ SQL — Databases

**Location:** [`sql/`](../sql/)

Every core SQL concept, in two forms per topic:

- **A raw `.sql` file** — plain SQL you can open in any editor, run through `sqlite3` (or DB Browser for SQLite, or paste into any SQL client), and read top-to-bottom like a script.
- **A matching `.py` file** — the identical schema and queries wrapped in a class using Python's built-in `sqlite3` module against an in-memory database, so the whole chapter is testable with `pytest` like everything else in this repo (no server install required either way).

Read the `.sql` file first — it's the actual SQL with nothing else in the way. The `.py` file exists so this repo can verify the SQL is correct automatically.

> SQLite doesn't support everything every database does (no stored procedures, limited `ALTER TABLE`), but `RIGHT JOIN` and `FULL OUTER JOIN` both work here since they were added in SQLite 3.39 (2022) — this repo assumes that version or newer.

---

## Chapters

Each row is one topic — `.sql` (read this first) and `.py` (the tested twin) side by side.

| `.sql` | `.py` / Class | Covers |
| :--- | :--- | :--- |
| `ddl/create_table.sql` | `create_table.py` / `CreateTable` | `CREATE TABLE`, `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `DEFAULT`, `CHECK`, `FOREIGN KEY` |
| `ddl/alter_drop_table.sql` | `alter_drop_table.py` / `AlterDropTable` | `ALTER TABLE` (add/rename/drop column, rename table), `DROP TABLE` |
| `dml/insert_update_delete.sql` | `insert_update_delete.py` / `InsertUpdateDelete` | `INSERT` (single & multi-row), `UPDATE`, `DELETE`, why `WHERE` matters |
| `queries/select_where_orderby.sql` | `select_where_orderby.py` / `SelectWhereOrderBy` | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, `LIKE`, `BETWEEN`, `IN` |
| `queries/aggregate_group_having.sql` | `aggregate_group_having.py` / `AggregateGroupHaving` | `COUNT`/`SUM`/`AVG`/`MIN`/`MAX`, `GROUP BY`, `HAVING` vs `WHERE` |
| `joins/all_joins.sql` | `all_joins.py` / `AllJoins` | `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, `CROSS`, and self joins |
| `subqueries/subqueries.sql` | `subqueries.py` / `Subqueries` | Scalar subquery, `IN`, correlated subquery, `EXISTS`, subquery in `FROM` |
| `set_operations/set_operations.sql` | `set_operations.py` / `SetOperations` | `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT` |
| `window_functions/window_functions.sql` | `window_functions.py` / `WindowFunctions` | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LAG`, `LEAD`, running totals via `SUM() OVER` |
| `views_and_indexes/views_and_indexes.sql` | `views_and_indexes.py` / `ViewsAndIndexes` | `CREATE VIEW` (live, not a snapshot), `CREATE INDEX`, reading `EXPLAIN QUERY PLAN` |
| `transactions/transactions.sql` | `transactions.py` / `Transactions` | `BEGIN`/`COMMIT`/`ROLLBACK`, atomicity via a bank-transfer example |

---

## How to Run

**Raw SQL** (via the `sqlite3` CLI, if installed — or paste into DB Browser for SQLite / any SQL client):

```bash
sqlite3 :memory: < ./sql/ddl/create_table.sql
sqlite3 :memory: < ./sql/joins/all_joins.sql
sqlite3 :memory: < ./sql/window_functions/window_functions.sql
# ...and so on for every .sql file above
```

**Python versions** (same queries, run and printed via `sqlite3` stdlib):

```bash
python ./sql/ddl/create_table.py
python ./sql/ddl/alter_drop_table.py
python ./sql/dml/insert_update_delete.py
python ./sql/queries/select_where_orderby.py
python ./sql/queries/aggregate_group_having.py
python ./sql/joins/all_joins.py
python ./sql/subqueries/subqueries.py
python ./sql/set_operations/set_operations.py
python ./sql/window_functions/window_functions.py
python ./sql/views_and_indexes/views_and_indexes.py
python ./sql/transactions/transactions.py
```
