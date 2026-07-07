"""
tests/dsa/test_dsa_stack.py
============================
Tests for all classes under dsa/stack/:
    Stack · ValidParentheses · MinStack · EvaluatePostfix
"""

import pytest
from tests.utils import load_module


def _Stack():
    return load_module('dsa/stack/stack_array.py', ['1 2 3'], alias='dsa_stack').Stack

def _ValidParentheses():
    return load_module('dsa/stack/valid_parentheses.py', ['()'], alias='dsa_valid_parens').ValidParentheses

def _MinStack():
    return load_module('dsa/stack/min_stack.py', ['3 1 2'], alias='dsa_min_stack').MinStack

def _EvaluatePostfix():
    return load_module('dsa/stack/evaluate_postfix.py', ['3 4 +'], alias='dsa_eval_postfix').EvaluatePostfix


# ═════════════════════════════════════════════════════════════════════════════

class TestStack:

    def test_push_pop_order(self):
        s = _Stack()()
        s.push(1); s.push(2); s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.pop() == 1

    def test_peek_does_not_remove(self):
        s = _Stack()()
        s.push(10); s.push(20)
        assert s.peek() == 20
        assert s.size() == 2

    def test_empty_stack(self):
        s = _Stack()()
        assert s.is_empty()
        assert s.pop() is None
        assert s.peek() is None

    def test_size_tracks_pushes_and_pops(self):
        s = _Stack()()
        for v in [1, 2, 3, 4]: s.push(v)
        assert s.size() == 4
        s.pop()
        assert s.size() == 3


class TestValidParentheses:

    @pytest.mark.parametrize("s, expected", [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((()))", True),
        ("([{}])", True),
    ])
    def test_is_valid(self, s, expected):
        assert _ValidParentheses()(s).is_valid() == expected


class TestMinStack:

    def test_get_min_after_pushes(self):
        ms = _MinStack()()
        for v in [3, 1, 4, 1, 5]: ms.push(v)
        assert ms.get_min() == 1

    def test_min_updates_after_pop(self):
        ms = _MinStack()()
        for v in [3, 1, 4]: ms.push(v)
        assert ms.get_min() == 1
        ms.pop()  # removes 4
        assert ms.get_min() == 1
        ms.pop()  # removes 1
        assert ms.get_min() == 3

    def test_top(self):
        ms = _MinStack()()
        ms.push(5); ms.push(9)
        assert ms.top() == 9

    def test_empty(self):
        ms = _MinStack()()
        assert ms.get_min() is None
        assert ms.top() is None
        assert ms.pop() is None

    def test_negative_values(self):
        ms = _MinStack()()
        for v in [-2, -5, -1]: ms.push(v)
        assert ms.get_min() == -5


class TestEvaluatePostfix:

    @pytest.mark.parametrize("expr, expected", [
        ("3 4 +", 7.0),
        ("3 4 + 2 *", 14.0),
        ("5 1 2 + 4 * + 3 -", 14.0),
        ("10 2 /", 5.0),
        ("4 2 -", 2.0),
    ])
    def test_evaluate(self, expr, expected):
        assert _EvaluatePostfix()(expr).evaluate() == expected

    def test_single_number(self):
        assert _EvaluatePostfix()("42").evaluate() == 42.0
