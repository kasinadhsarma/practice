# 🧱 OOP — Geometry

**Location:** [`mathmatics/geometry/`](../mathmatics/geometry/)

A comprehensive geometric toolkit built with **Object-Oriented Programming** — each shape is a **class** with encapsulated attributes and methods. Covers 2D areas, 2D perimeters, 3D surface areas, 3D volumes, and vector/theorem utilities.

> **Complexity (all):** $\mathcal{O}(1)$ Time and Space — each method applies a single formula.

---

## 📐 2D Areas — `areas/`

| File | Class | Formula | Parameters |
|:---|:---|:---|:---|
| `rectangle.py` | `Rectangle` | $l \times b$ | length, breadth |
| `square.py` | `Square` | $s^2$ | side |
| `triangle.py` | `Triangle` | $\frac{1}{2} \times b \times h$ | base, height |
| `parallelogram.py` | `Parallelogram` | $b \times h$ | base, height |
| `trapezoid.py` | `Trapezoid` | $h \times \frac{b_1 + b_2}{2}$ | height, base1, base2 |
| `circle.py` | `Circle` | $\pi \times r^2$ | radius |
| `circlualarring.py` | `CircularRing` | $\pi \times (R^2 - r^2)$ | outer radius, inner radius |
| `cube.py` | `Cube` | $6 \times a^2$ | side (face area) |

---

## 📏 2D Perimeters — `perimeter/`

| File | Class | Formula | Parameters |
|:---|:---|:---|:---|
| `square.py` | `Square` | $4 \times s$ | side |
| `rectangle.py` | `Rectangle` | $2 \times (l + w)$ | length, width |
| `traingle.py` | `Triangle` | $a + b + c$ | three sides |
| `parallelogram.py` | `Parallelogram` | $2 \times (a + b)$ | side a, side b |
| `trapezoid.py` | `Trapezoid` | $a + b_1 + b_2 + c$ | all four sides |

---

## 🌐 3D Surface Areas — `surfacearea/`

| File | Class | Formula | Parameters |
|:---|:---|:---|:---|
| `cube.py` | `Cube` | $6 \times s^2$ | side |
| `cylinder.py` | `Cylinder` | $2 \pi r (h + r)$ | radius, height |
| `sphere.py` | `Sphere` | $4 \pi r^2$ | radius |
| `rectanglularprism.py` | `RectangularPrism` | $2(lw + lh + wh)$ | length, width, height |
| `rightcircularcone.py` | `RightCircularCone` | $\pi r^2 + \pi r \sqrt{r^2 + h^2}$ | radius, height |

---

## 🔵 3D Curved Surface — `surface/`

| File | Class | Formula | Parameters |
|:---|:---|:---|:---|
| `rightcircularcone.py` | `RightCircularCone` | $\pi r \sqrt{r^2 + h^2}$ | radius, height |

---

## 📦 3D Volumes — `volume/`

| File | Class | Formula | Parameters |
|:---|:---|:---|:---|
| `cube.py` | `Cube` | $s^3$ | side |
| `cylinder.py` | `Cylinder` | $\pi r^2 h$ | radius, height |
| `sphere.py` | `Sphere` | $\frac{4}{3} \pi r^3$ | radius |
| `rectanglularprism.py` | `RectangularPrism` | $l \times w \times h$ | length, width, height |
| `rightcircularcone.py` | `RightCircularCone` | $\frac{1}{3} \pi r^2 h$ | radius, height |

---

## 📐 Root-Level Utilities

| File | Description | Formula |
|:---|:---|:---|
| `pythogorentherom.py` | Pythagorean Theorem — finds hypotenuse squared | $c^2 = a^2 + b^2$ |
| `vector.py` | Vector operations | Magnitude, dot product, etc. |

---

## OOP Design Pattern

All geometry classes follow this pattern:

```python
class Shape:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def calculate(self):
        return formula(self.param1, self.param2)

# Usage
shape = Shape(val1, val2)
print(shape.calculate())
```

**Benefits:**
- ✅ **Encapsulation** — data and behaviour are bundled together
- ✅ **Reusability** — create multiple instances with different dimensions
- ✅ **Readability** — class name clearly describes the shape
- ✅ **Extensibility** — add new methods (e.g., `perimeter`, `volume`) without changing callers

---

## How to Run

```bash
# 2D Area
python ./oops/geometry/areas/circle.py
python ./oops/geometry/areas/rectangle.py

# 2D Perimeter
python ./oops/geometry/perimeter/trapezoid.py

# 3D Surface Area
python ./oops/geometry/surfacearea/cylinder.py
python ./oops/geometry/surfacearea/sphere.py

# 3D Volume
python ./oops/geometry/volume/rightcircularcone.py

# Utilities
python ./oops/geometry/pythogorentherom.py
```
