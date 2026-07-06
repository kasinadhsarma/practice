"""
tests/test_sql.py
==================
Tests for every SQL concept under sql/, using Python's built-in sqlite3
module (in-memory databases, no server required):

    DDL              — CreateTable, AlterDropTable
    DML              — InsertUpdateDelete
    Queries          — SelectWhereOrderBy, AggregateGroupHaving
    Joins            — AllJoins (inner/left/right/full/cross/self)
    Subqueries       — Subqueries (scalar/correlated/IN/EXISTS/derived table)
    Set Operations   — SetOperations (union/union all/intersect/except)
    Window Functions — WindowFunctions (row_number/rank/dense_rank/lag/lead/running total)
    Views & Indexes  — ViewsAndIndexes
    Transactions     — Transactions (commit/rollback)
"""

import pytest
from tests.utils import load_module


def _CreateTable():
    return load_module('sql/ddl/create_table.py', [], alias='sql_createtable').CreateTable

def _AlterDropTable():
    return load_module('sql/ddl/alter_drop_table.py', [], alias='sql_alterdrop').AlterDropTable

def _InsertUpdateDelete():
    return load_module('sql/dml/insert_update_delete.py', [], alias='sql_iud').InsertUpdateDelete

def _SelectWhereOrderBy():
    return load_module('sql/queries/select_where_orderby.py', [], alias='sql_swo').SelectWhereOrderBy

def _AggregateGroupHaving():
    return load_module('sql/queries/aggregate_group_having.py', [], alias='sql_agh').AggregateGroupHaving

def _AllJoins():
    return load_module('sql/joins/all_joins.py', [], alias='sql_joins').AllJoins

def _Subqueries():
    return load_module('sql/subqueries/subqueries.py', [], alias='sql_subq').Subqueries

def _SetOperations():
    return load_module('sql/set_operations/set_operations.py', [], alias='sql_setops').SetOperations

def _WindowFunctions():
    return load_module('sql/window_functions/window_functions.py', [], alias='sql_window').WindowFunctions

def _ViewsAndIndexes():
    return load_module('sql/views_and_indexes/views_and_indexes.py', [], alias='sql_views').ViewsAndIndexes

def _Transactions():
    return load_module('sql/transactions/transactions.py', [], alias='sql_tx').Transactions


# ═════════════════════════════════════════════════════════════════════════════
#  DDL
# ═════════════════════════════════════════════════════════════════════════════

class TestCreateTable:

    def test_basic_table_created(self):
        ct = _CreateTable()()
        ct.create_basic_table()
        assert "authors" in ct.list_tables()

    def test_foreign_key_creates_both_tables(self):
        ct = _CreateTable()()
        ct.create_table_with_foreign_key()
        assert set(ct.list_tables()) == {"authors", "books"}

    def test_constraints_table_schema(self):
        ct = _CreateTable()()
        ct.create_table_with_constraints()
        cols = {row[1]: row for row in ct.table_schema("products")}
        assert cols["sku"][3] == 1  # NOT NULL flag
        assert cols["quantity"][4] == "0"  # DEFAULT value

    def test_check_constraint_enforced(self):
        ct = _CreateTable()()
        ct.create_table_with_constraints()
        with pytest.raises(Exception):
            ct.conn.execute("INSERT INTO products (sku, price) VALUES ('A1', -5)")

    def test_unique_constraint_enforced(self):
        ct = _CreateTable()()
        ct.create_table_with_constraints()
        ct.conn.execute("INSERT INTO products (sku, price) VALUES ('A1', 10)")
        with pytest.raises(Exception):
            ct.conn.execute("INSERT INTO products (sku, price) VALUES ('A1', 20)")


class TestAlterDropTable:

    def test_add_column(self):
        adt = _AlterDropTable()()
        adt.add_column("department", "TEXT")
        assert "department" in adt.columns_of("employees")

    def test_rename_column(self):
        adt = _AlterDropTable()()
        adt.add_column("dept", "TEXT")
        adt.rename_column("dept", "department")
        cols = adt.columns_of("employees")
        assert "department" in cols and "dept" not in cols

    def test_rename_table(self):
        adt = _AlterDropTable()()
        adt.rename_table("staff")
        assert adt.table_exists("staff") is True
        assert adt.table_exists("employees") is False

    def test_drop_column(self):
        adt = _AlterDropTable()()
        adt.add_column("department", "TEXT")
        adt.drop_column("department")
        assert "department" not in adt.columns_of("employees")

    def test_drop_table(self):
        adt = _AlterDropTable()()
        adt.drop_table("employees")
        assert adt.table_exists("employees") is False


# ═════════════════════════════════════════════════════════════════════════════
#  DML
# ═════════════════════════════════════════════════════════════════════════════

class TestInsertUpdateDelete:

    def test_insert_single(self):
        iud = _InsertUpdateDelete()()
        iud.insert_single("Alice", 100.0)
        assert iud.all_accounts() == [("Alice", 100.0)]

    def test_insert_many(self):
        iud = _InsertUpdateDelete()()
        iud.insert_many([("Bob", 50.0), ("Carol", 200.0)])
        assert iud.all_accounts() == [("Bob", 50.0), ("Carol", 200.0)]

    def test_update_specific_row(self):
        iud = _InsertUpdateDelete()()
        iud.insert_many([("Alice", 100.0), ("Bob", 50.0)])
        iud.update_balance("Bob", 75.0)
        assert iud.all_accounts() == [("Alice", 100.0), ("Bob", 75.0)]

    def test_update_without_where_affects_all_rows(self):
        iud = _InsertUpdateDelete()()
        iud.insert_many([("Alice", 100.0), ("Bob", 50.0)])
        iud.apply_interest(0.1)
        rows = iud.all_accounts()
        assert [row[0] for row in rows] == ["Alice", "Bob"]
        assert [row[1] for row in rows] == pytest.approx([110.0, 55.0])

    def test_delete_by_name(self):
        iud = _InsertUpdateDelete()()
        iud.insert_many([("Alice", 100.0), ("Bob", 50.0)])
        iud.delete_by_name("Alice")
        assert iud.all_accounts() == [("Bob", 50.0)]

    def test_delete_below_threshold(self):
        iud = _InsertUpdateDelete()()
        iud.insert_many([("Alice", 100.0), ("Bob", 10.0), ("Carol", 5.0)])
        iud.delete_below_balance(50)
        assert iud.all_accounts() == [("Alice", 100.0)]


# ═════════════════════════════════════════════════════════════════════════════
#  Queries
# ═════════════════════════════════════════════════════════════════════════════

class TestSelectWhereOrderBy:

    def test_where_equals(self):
        swo = _SelectWhereOrderBy()()
        assert swo.where_equals("Engineering") == [("Alice",), ("Bob",)]

    def test_where_comparison(self):
        swo = _SelectWhereOrderBy()()
        assert swo.where_comparison(70000) == [("Alice",), ("Bob",), ("Eve",)]

    def test_where_between(self):
        swo = _SelectWhereOrderBy()()
        assert swo.where_between(25, 30) == [("Alice",), ("Dave",), ("Eve",)]

    def test_where_in(self):
        swo = _SelectWhereOrderBy()()
        result = {row[0] for row in swo.where_in(["Sales", "Marketing"])}
        assert result == {"Carol", "Dave", "Eve"}

    def test_where_like(self):
        swo = _SelectWhereOrderBy()()
        assert swo.where_like("A%") == [("Alice",)]

    def test_order_by_ascending(self):
        swo = _SelectWhereOrderBy()()
        result = swo.order_by_salary()
        salaries = [row[1] for row in result]
        assert salaries == sorted(salaries)

    def test_order_by_descending(self):
        swo = _SelectWhereOrderBy()()
        result = swo.order_by_salary(descending=True)
        salaries = [row[1] for row in result]
        assert salaries == sorted(salaries, reverse=True)

    def test_top_n(self):
        swo = _SelectWhereOrderBy()()
        assert swo.top_n_by_salary(2) == [("Alice", 95000.0), ("Bob", 85000.0)]

    def test_distinct(self):
        swo = _SelectWhereOrderBy()()
        assert set(swo.distinct_departments()) == {"Engineering", "Sales", "Marketing"}


class TestAggregateGroupHaving:

    def test_count_all(self):
        assert _AggregateGroupHaving()().count_all() == 5

    def test_total_salary(self):
        assert _AggregateGroupHaving()().total_salary() == 375000

    def test_average_salary(self):
        assert _AggregateGroupHaving()().average_salary() == 75000

    def test_salary_range(self):
        assert _AggregateGroupHaving()().salary_range() == (60000, 95000)

    def test_count_by_department(self):
        result = dict(_AggregateGroupHaving()().count_by_department())
        assert result == {"Engineering": 2, "Sales": 2, "Marketing": 1}

    def test_departments_above_average(self):
        result = _AggregateGroupHaving()().departments_above_average(70000)
        assert result == [("Engineering", 90000.0)]

    def test_departments_with_multiple_employees(self):
        result = {row[0] for row in _AggregateGroupHaving()().departments_with_multiple_employees()}
        assert result == {"Engineering", "Sales"}


# ═════════════════════════════════════════════════════════════════════════════
#  Joins
# ═════════════════════════════════════════════════════════════════════════════

class TestAllJoins:

    def test_inner_join_excludes_unmatched(self):
        result = _AllJoins()().inner_join()
        names = {row[0] for row in result}
        assert "Carol" not in names
        assert len(result) == 3

    def test_left_join_includes_unmatched_left(self):
        result = _AllJoins()().left_join()
        assert ("Carol", None) in result

    def test_right_join_includes_unmatched_right(self):
        result = _AllJoins()().right_join()
        assert (None, "Ghost Order") in result

    def test_full_outer_join_includes_both_sides(self):
        result = _AllJoins()().full_outer_join()
        assert ("Carol", None) in result
        assert (None, "Ghost Order") in result

    def test_cross_join_is_cartesian_product(self):
        result = _AllJoins()().cross_join()
        assert len(result) == 3 * 4  # 3 customers x 4 orders

    def test_self_join_pairs_same_department(self):
        result = _AllJoins()().self_join_same_department()
        assert result == [("Alice", "Bob")]


# ═════════════════════════════════════════════════════════════════════════════
#  Subqueries
# ═════════════════════════════════════════════════════════════════════════════

class TestSubqueries:

    def test_scalar_subquery_above_average(self):
        result = {row[0] for row in _Subqueries()().above_average_salary()}
        assert result == {"Alice", "Bob"}

    def test_in_subquery(self):
        result = {row[0] for row in _Subqueries()().in_top_departments(["Sales"])}
        assert result == {"Carol", "Dave"}

    def test_correlated_subquery_highest_per_department(self):
        result = _Subqueries()().highest_paid_per_department()
        names = {row[0] for row in result}
        assert names == {"Alice", "Eve", "Carol"}

    def test_exists_subquery(self):
        result = [row[0] for row in _Subqueries()().departments_with_any_employee_over(90000)]
        assert result == ["Engineering"]

    def test_subquery_in_from(self):
        result = _Subqueries()().department_averages_above(65000)
        depts = {row[0] for row in result}
        assert depts == {"Engineering", "Marketing"}


# ═════════════════════════════════════════════════════════════════════════════
#  Set Operations
# ═════════════════════════════════════════════════════════════════════════════

class TestSetOperations:

    def test_union_deduplicates(self):
        assert _SetOperations()().union() == ["Alice", "Bob", "Carol", "Dave"]

    def test_union_all_keeps_duplicates(self):
        result = _SetOperations()().union_all()
        assert len(result) == 6
        assert result.count("Bob") == 2

    def test_intersect(self):
        assert _SetOperations()().intersect() == ["Bob", "Carol"]

    def test_except_new_this_year(self):
        assert _SetOperations()().except_() == ["Alice"]

    def test_except_churned(self):
        assert _SetOperations()().churned() == ["Dave"]


# ═════════════════════════════════════════════════════════════════════════════
#  Window Functions
# ═════════════════════════════════════════════════════════════════════════════

class TestWindowFunctions:

    def test_row_number_no_ties(self):
        result = _WindowFunctions()().row_number_per_region()
        east_rns = [row[3] for row in result if row[0] == "East"]
        assert east_rns == [1, 2, 3]

    def test_rank_leaves_gap_after_tie(self):
        result = _WindowFunctions()().rank_per_region()
        east = [row for row in result if row[0] == "East"]
        # Alice and Bob tie at 500 -> both rank 1, Alice's 300 -> rank 3 (gap at 2)
        ranks = sorted(row[3] for row in east)
        assert ranks == [1, 1, 3]

    def test_dense_rank_no_gap_after_tie(self):
        result = _WindowFunctions()().dense_rank_per_region()
        east = [row for row in result if row[0] == "East"]
        ranks = sorted(row[3] for row in east)
        assert ranks == [1, 1, 2]

    def test_lag_lead(self):
        result = _WindowFunctions()().lag_lead_by_date()
        east = [row for row in result if row[0] == "East"]
        # first row has no prior (None), last row has no next (None)
        assert east[0][3] is None
        assert east[-1][4] is None

    def test_running_total_is_monotonic_increasing(self):
        result = _WindowFunctions()().running_total_by_region()
        east_totals = [row[3] for row in result if row[0] == "East"]
        assert east_totals == sorted(east_totals)
        assert east_totals[-1] == 1300.0


# ═════════════════════════════════════════════════════════════════════════════
#  Views & Indexes
# ═════════════════════════════════════════════════════════════════════════════

class TestViewsAndIndexes:

    def test_view_returns_filtered_rows(self):
        vai = _ViewsAndIndexes()()
        vai.create_view()
        assert vai.query_view() == [("Alice",), ("Bob",)]

    def test_view_reflects_new_data_live(self):
        vai = _ViewsAndIndexes()()
        vai.create_view()
        vai.view_reflects_new_data()
        assert vai.query_view() == [("Alice",), ("Bob",), ("Dave",)]

    def test_drop_view(self):
        vai = _ViewsAndIndexes()()
        vai.create_view()
        vai.drop_view()
        with pytest.raises(Exception):
            vai.query_view()

    def test_create_index(self):
        vai = _ViewsAndIndexes()()
        vai.create_index()
        assert "idx_department" in vai.list_indexes()

    def test_query_plan_uses_index_after_creation(self):
        vai = _ViewsAndIndexes()()
        plan_before = vai.uses_index_for_query("Sales")
        vai.create_index()
        plan_after = vai.uses_index_for_query("Sales")
        assert "SCAN" in plan_before
        assert "USING INDEX" in plan_after


# ═════════════════════════════════════════════════════════════════════════════
#  Transactions
# ═════════════════════════════════════════════════════════════════════════════

class TestTransactions:

    def test_committed_transfer_moves_money(self):
        tx = _Transactions()()
        tx.transfer_committed("Alice", "Bob", 30.0)
        assert tx.balance_of("Alice") == 70.0
        assert tx.balance_of("Bob") == 80.0

    def test_rolled_back_transfer_changes_nothing(self):
        tx = _Transactions()()
        before_alice, before_bob = tx.balance_of("Alice"), tx.balance_of("Bob")
        tx.transfer_rolled_back("Alice", "Bob", 1000.0)
        assert tx.balance_of("Alice") == before_alice
        assert tx.balance_of("Bob") == before_bob

    def test_committed_then_rolled_back_sequence(self):
        tx = _Transactions()()
        tx.transfer_committed("Alice", "Bob", 30.0)
        tx.transfer_rolled_back("Bob", "Alice", 500.0)
        assert tx.balance_of("Alice") == 70.0
        assert tx.balance_of("Bob") == 80.0
