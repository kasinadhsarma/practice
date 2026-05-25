"""
tests/conftest.py
-----------------
Root pytest configuration.  Adds the project root to sys.path so every
test sub-package (basics/, oops/, dsa/) can do:

    from tests.utils import load_module, load_class
"""
import sys
import os

# Project root is one level above this file (tests/ -> project root)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
