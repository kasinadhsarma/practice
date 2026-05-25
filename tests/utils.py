"""
tests/utils.py
--------------
Shared helpers for importing source modules in this project.

Many source files are educational scripts that:
  (a) call input() at module level — use load_module() which mocks stdin
  (b) shadow the class name with an instance, e.g. ``cube = cube(s)``
      — use load_class() which extracts only the class definition via AST

Usage
-----
    from tests.utils import load_module, load_class

    # Module is importable and class name is NOT shadowed:
    mod = load_module('dsa/sorting/bubblesort.py', inputs=['1 2 3'])
    bs  = mod.BubbleSort([5, 2, 8])

    # Class name IS shadowed at module level (e.g. ``cube = cube(s)``):
    cube_cls = load_class('oops/geometry/volume/cube.py', 'cube')
    c = cube_cls(3)
    assert c.get_volume() == 27
"""

import ast
import os
import sys
import importlib.util
from unittest.mock import patch

# Absolute path to the project root (parent of tests/)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_module(rel_path: str, inputs: list, alias: str = None):
    """
    Load a Python source file as a module while feeding canned strings to
    every top-level  input()  call so the script-section runs without
    blocking on real stdin.

    Parameters
    ----------
    rel_path : str
        Forward-slash path relative to BASE_DIR,
        e.g. ``'oops/geometry/areas/rectangle.py'``
    inputs : list[str]
        Values fed to ``input()`` in order during module-level execution.
    alias : str, optional
        Name registered in ``sys.modules``.  Defaults to a slug derived
        from *rel_path*.

    Returns
    -------
    types.ModuleType
        The freshly loaded Python module.
    """
    full_path = os.path.join(BASE_DIR, *rel_path.split("/"))
    mod_name  = alias or ("_tm_" + rel_path.replace("/", "__").replace(".", "_"))

    # Evict any cached copy so each call starts fresh
    sys.modules.pop(mod_name, None)

    spec   = importlib.util.spec_from_file_location(mod_name, full_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = module

    with patch("builtins.input", side_effect=inputs):
        spec.loader.exec_module(module)

    return module


def load_class(rel_path: str, class_name: str):
    """
    Extract and return a single class from a source file **without** executing
    any module-level script code.

    This is the right tool when the source file shadows the class name at
    module level, e.g.::

        class cube:
            ...
        cube = cube(s)   # ← shadows the class; load_module() would lose it

    The function parses the file with :mod:`ast`, keeps only
    ``import``/``from import`` statements and class/function definitions,
    then compiles and executes that stripped tree in a fresh namespace.

    Parameters
    ----------
    rel_path : str
        Forward-slash path relative to BASE_DIR.
    class_name : str
        Name of the class to return.

    Returns
    -------
    type
        The class object extracted from the source file.
    """
    full_path = os.path.join(BASE_DIR, *rel_path.split("/"))
    with open(full_path, "r", encoding="utf-8") as fh:
        source = fh.read()

    tree = ast.parse(source, filename=full_path)

    # Keep only import statements + class / function definitions
    kept_nodes = [
        node for node in tree.body
        if isinstance(node, (ast.Import, ast.ImportFrom,
                             ast.ClassDef, ast.FunctionDef,
                             ast.AsyncFunctionDef))
    ]

    new_tree = ast.Module(body=kept_nodes, type_ignores=[])
    ast.fix_missing_locations(new_tree)
    code = compile(new_tree, full_path, "exec")

    namespace: dict = {}
    exec(code, namespace)           # noqa: S102  (intentional dynamic exec)
    return namespace[class_name]
