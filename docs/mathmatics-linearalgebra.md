# 📐 Mathematics — Linear Algebra

**Location:** [`mathmatics/algebra/linearalgebra/`](../mathmatics/algebra/linearalgebra/)

Vector algebra and solving linear systems — the layer above raw matrix mechanics (see [Matrices](./mathmatics-matrices.md) for the matrix-only operations these build on top of). Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Vector Arithmetic & Geometry

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `vector_addition.py` | `vector_addition` | Element-wise sum of two same-length vectors | $\mathcal{O}(N)$ |
| `vector_subtraction.py` | `vector_subtraction` | Element-wise difference of two same-length vectors | $\mathcal{O}(N)$ |
| `scalar_vector_multiplication.py` | `scalar_vector_multiplication` | Scales every component by a constant | $\mathcal{O}(N)$ |
| `dot_product.py` | `dot_product` | $\sum a_i b_i$ — scalar (inner) product | $\mathcal{O}(N)$ |
| `cross_product.py` | `cross_product` | 3D vector product, perpendicular to both inputs | $\mathcal{O}(1)$ |
| `vector_magnitude.py` | `vector_magnitude` | Euclidean norm $\lVert v \rVert = \sqrt{\sum v_i^2}$ | $\mathcal{O}(N)$ |
| `vector_normalization.py` | `vector_normalization` | Scales a vector to unit length | $\mathcal{O}(N)$ |
| `angle_between_vectors.py` | `angle_between_vectors` | $\theta = \arccos\left(\frac{a \cdot b}{\lVert a \rVert \lVert b \rVert}\right)$ | $\mathcal{O}(N)$ |
| `vector_projection.py` | `vector_projection` | Projects vector $a$ onto vector $b$ | $\mathcal{O}(N)$ |
| `linear_independence.py` | `linear_independence` | Gaussian-elimination rank check across a set of vectors | $\mathcal{O}(N^3)$ |

## Solving Linear Systems

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `solve_linear_system.py` | `solve_linear_system` | Gaussian elimination + back substitution for $Ax = b$ | $\mathcal{O}(N^3)$ |
| `cramers_rule.py` | `cramers_rule` | Solves $Ax = b$ via determinant ratios | $\mathcal{O}(N \times N!)$ |

---

## How to Run

```bash
python ./mathmatics/algebra/linearalgebra/vector_addition.py
python ./mathmatics/algebra/linearalgebra/vector_subtraction.py
python ./mathmatics/algebra/linearalgebra/scalar_vector_multiplication.py
python ./mathmatics/algebra/linearalgebra/dot_product.py
python ./mathmatics/algebra/linearalgebra/cross_product.py
python ./mathmatics/algebra/linearalgebra/vector_magnitude.py
python ./mathmatics/algebra/linearalgebra/vector_normalization.py
python ./mathmatics/algebra/linearalgebra/angle_between_vectors.py
python ./mathmatics/algebra/linearalgebra/vector_projection.py
python ./mathmatics/algebra/linearalgebra/linear_independence.py
python ./mathmatics/algebra/linearalgebra/solve_linear_system.py
python ./mathmatics/algebra/linearalgebra/cramers_rule.py
```
