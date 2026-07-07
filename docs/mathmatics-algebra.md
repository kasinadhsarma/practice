# ➗ Mathematics — Basic Algebra

**Location:** [`mathmatics/algebra/basicalgebra/`](../mathmatics/algebra/basicalgebra/)

Solving equations and manipulating expressions — the layer below [Linear Algebra](./mathmatics-linearalgebra.md), which extends these same ideas (systems of equations, unknowns) into vector/matrix form. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `linear_equation.py` | `linear_equation` | Solves $ax + b = 0$ for a single unknown | $\mathcal{O}(1)$ |
| `quadratic_equation.py` | `quadratic_equation` | Quadratic formula $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ — returns complex roots when the discriminant is negative | $\mathcal{O}(1)$ |
| `polynomial_operations.py` | `polynomial_operations` | Add, multiply, and evaluate polynomials given as coefficient lists | $\mathcal{O}(N)$ add, $\mathcal{O}(N \times M)$ multiply |
| `exponents_roots.py` | `exponents_roots` | Arbitrary-exponent powers and $n$th roots (including negative bases for odd roots) | $\mathcal{O}(1)$ |

---

## How to Run

```bash
python ./mathmatics/algebra/basicalgebra/linear_equation.py
python ./mathmatics/algebra/basicalgebra/quadratic_equation.py
python ./mathmatics/algebra/basicalgebra/polynomial_operations.py
python ./mathmatics/algebra/basicalgebra/exponents_roots.py
```
