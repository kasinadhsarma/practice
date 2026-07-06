# 🔢 Mathematics — Matrices

**Location:** [`mathmatics/matrices/`](../mathmatics/matrices/)

Every fundamental matrix operation, each as a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `addition.py` | `addition` | Element-wise sum of two same-shaped matrices | $\mathcal{O}(N \times M)$ |
| `subtraction.py` | `subtraction` | Element-wise difference of two same-shaped matrices | $\mathcal{O}(N \times M)$ |
| `multiplication.py` | `multiplication` | Standard matrix product $A \times B$ | $\mathcal{O}(N \times M \times P)$ |
| `scalar_multiplication.py` | `scalar_multiplication` | Scales every element by a constant | $\mathcal{O}(N \times M)$ |
| `transpose.py` | `transpose` | Flips rows and columns ($A^T$) | $\mathcal{O}(N \times M)$ |
| `determinant.py` | `determinant` | Recursive cofactor expansion, works for any $N \times N$ | $\mathcal{O}(N!)$ |
| `identity.py` | `identity` | Builds the $N \times N$ identity matrix | $\mathcal{O}(N)$ |
| `trace.py` | `trace` | Sum of the diagonal elements | $\mathcal{O}(N)$ |
| `is_symmetric.py` | `is_symmetric` | Checks $A = A^T$ | $\mathcal{O}(N^2)$ |
| `rotate90.py` | `rotate90` | Rotates the matrix 90° clockwise | $\mathcal{O}(N \times M)$ |
| `rank.py` | `rank` | Row-echelon reduction (Gaussian elimination) to count independent rows | $\mathcal{O}(N^3)$ |
| `inverse.py` | `inverse` | Adjugate / cofactor method: $A^{-1} = \frac{1}{\det(A)}\text{adj}(A)$ | $\mathcal{O}(N!)$ |
| `power.py` | `power` | Repeated squaring-free matrix exponentiation $A^n$ | $\mathcal{O}(N^3 \times n)$ |

---

## How to Run

```bash
python ./mathmatics/matrices/addition.py
python ./mathmatics/matrices/subtraction.py
python ./mathmatics/matrices/multiplication.py
python ./mathmatics/matrices/scalar_multiplication.py
python ./mathmatics/matrices/transpose.py
python ./mathmatics/matrices/determinant.py
python ./mathmatics/matrices/identity.py
python ./mathmatics/matrices/trace.py
python ./mathmatics/matrices/is_symmetric.py
python ./mathmatics/matrices/rotate90.py
python ./mathmatics/matrices/rank.py
python ./mathmatics/matrices/inverse.py
python ./mathmatics/matrices/power.py
```
