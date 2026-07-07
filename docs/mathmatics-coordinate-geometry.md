# 📍 Mathematics — Coordinate Geometry

**Location:** [`mathmatics/coordinate_geometry/`](../mathmatics/coordinate_geometry/)

Geometry expressed algebraically — points as coordinate pairs, shapes as equations. The bridge between [Geometry](../mathmatics/geometry/)'s shape formulas and [Linear Algebra](./mathmatics-linearalgebra.md)'s vector treatment of the same 2D space. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `distance_formula.py` | `distance_formula` | $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ — Pythagoras applied to two points | $\mathcal{O}(1)$ |
| `midpoint_formula.py` | `midpoint_formula` | Averages both coordinates to find the point exactly between two others | $\mathcal{O}(1)$ |
| `slope_and_line_equation.py` | `slope_and_line_equation` | Slope $m = \frac{y_2-y_1}{x_2-x_1}$, then derives the full slope-intercept form $y=mx+b$ | $\mathcal{O}(1)$ |
| `circle_equation.py` | `circle_equation` | Standard form $(x-h)^2+(y-k)^2=r^2$ — classifies a point as on/inside/outside a circle | $\mathcal{O}(1)$ |

---

## How to Run

```bash
python ./mathmatics/coordinate_geometry/distance_formula.py
python ./mathmatics/coordinate_geometry/midpoint_formula.py
python ./mathmatics/coordinate_geometry/slope_and_line_equation.py
python ./mathmatics/coordinate_geometry/circle_equation.py
```
