# 🔲 DSA Basics — Pattern Printing

**Location:** [`dsa/basics/`](../dsa/basics/)

Programs that teach nested loop bounds, horizontal/vertical coordination, and space-offset calculations by printing visual patterns using **stars** or **numbers**.  
All scripts use **OOP classes** with formula comments, time/space complexity, and a runnable `input()`-driven demo.

> **Complexity (all patterns):**
> - **Time:** $\mathcal{O}(N^2)$ — quadratic due to nested loops
> - **Space:** $\mathcal{O}(1)$ — output is streamed directly, no arrays stored

---

## 🌟 Star Patterns

**Location:** [`dsa/basics/stars/`](../dsa/basics/stars/)

### 🟢 Level 1 — Simple Triangles & Square

**Location:** [`dsa/basics/stars/level1/`](../dsa/basics/stars/level1/)

| File | Class | Pattern | Technique |
| :--- | :--- | :--- | :--- |
| `right_triangle.py` | `RightTriangle` | Left-aligned growing triangle | `"*" * i` per row |
| `left_triangle.py` | `LeftTriangle` | Right-aligned growing triangle | `" " * (n-i) + "*" * i` |
| `inverted_triangle.py` | `InvertedTriangle` | Left-aligned shrinking triangle | Loop `n → 1` |
| `square.py` | `Square` | $n \times n$ solid square | Repeat full row $n$ times |

```
right_triangle (n=5)    left_triangle (n=5)    inverted_triangle (n=5)    square (n=4)
*                           *                  *****                      ****
**                         **                  ****                       ****
***                       ***                  ***                        ****
****                     ****                  **                         ****
*****                   *****                  *
```

---

### 🟡 Level 2 — Pyramids & Hollow Shapes

**Location:** [`dsa/basics/stars/level2/`](../dsa/basics/stars/level2/)

| File | Class | Pattern | Technique |
| :--- | :--- | :--- | :--- |
| `pyramid.py` | `Pyramid` | Centered upward pyramid | Spaces = `n-i`, stars = `2i-1` |
| `inverted_pyramid.py` | `InvertedPyramid` | Centered downward pyramid | Loop `n → 1` with same formula |
| `hollow_square.py` | `HollowSquare` | Border-only square | `*` only on first/last row or column |
| `hollow_triangle.py` | `HollowTriangle` | Border-only right triangle | `*` only on first col, diagonal, or last row |

```
pyramid (n=5)      inverted_pyramid (n=5)    hollow_square (n=5)    hollow_triangle (n=5)
    *              *********                 *****                  *
   ***              *******                 *   *                  **
  *****              *****                  *   *                  * *
 *******              ***                   *   *                  *  *
*********              *                    *****                  *****
```

---

### 🔴 Level 3 — Advanced Symmetric Patterns

**Location:** [`dsa/basics/stars/level3/`](../dsa/basics/stars/level3/)

| File | Class | Pattern | Technique |
| :--- | :--- | :--- | :--- |
| `diamond.py` | `Diamond` | Full vertical diamond | Pyramid (rows 1→n) + inverted (rows n-1→1) |
| `butterfly.py` | `Butterfly` | Symmetric wings | Left stars + gap (`2*(n-i)`) + right stars, mirrored |
| `hourglass.py` | `Hourglass` | Top-down then bottom-up pyramid | Inverted pyramid then pyramid (skip tip) |

```
diamond (n=5)          butterfly (n=4)         hourglass (n=5)
    *                  *      *               *********
   ***                 **    **                *******
  *****                ***  ***                *****
 *******               ********                 ***
*********              ********                  *
 *******               ***  ***                 ***
  *****                **    **                *****
   ***                 *      *               *******
    *                                        *********
```

---

## 🔢 Number Patterns

**Location:** [`dsa/basics/numbers/`](../dsa/basics/numbers/)

### 🟢 Level 1 — Simple Number Triangles & Square

**Location:** [`dsa/basics/numbers/level1/`](../dsa/basics/numbers/level1/)

| File | Class | Pattern | Technique |
| :--- | :--- | :--- | :--- |
| `right_triangle.py` | `RightTriangle` | Left-aligned `1..i` per row | `range(1, i+1)` joined by spaces |
| `left_triangle.py` | `LeftTriangle` | Right-aligned `1..i` per row | `(n-i)*2` leading spaces |
| `inverted_triangle.py` | `InvertedTriangle` | Shrinking number rows from `n` down | Loop `n → 1` |
| `square.py` | `Square` | Every row prints `1 2 3 … n` | Repeat same row string $n$ times |

```
right_triangle (n=5)    left_triangle (n=5)       inverted (n=5)     square (n=3)
1                               1                 1 2 3 4 5          1 2 3
1 2                           1 2                 1 2 3 4            1 2 3
1 2 3                       1 2 3                 1 2 3              1 2 3
1 2 3 4                   1 2 3 4                 1 2
1 2 3 4 5               1 2 3 4 5                 1
```

---

### 🟡 Level 2 — Pyramid, Floyd & Middle

**Location:** [`dsa/basics/numbers/level2/`](../dsa/basics/numbers/level2/)

| File | Class | Pattern | Technique |
| :--- | :--- | :--- | :--- |
| `pyramid.py` | `NumberPyramid` | Palindrome rows `1..i..1` centered | Ascending + descending joined, with padding |
| `floyd_triangle.py` | `FloydTriangle` | Consecutive integers fill each row | Single counter increments across all rows |
| `middle_triangle.py` | `MiddleTriangle` | Center-aligned `1..i` per row | Space prefix = `n-i` |

```
pyramid (n=5)               floyd_triangle (n=5)     middle_triangle (n=5)
        1                   1                            1
      1 2 1                 2  3                        1 2
    1 2 3 2 1               4  5  6                    1 2 3
  1 2 3 4 3 2 1             7  8  9  10               1 2 3 4
1 2 3 4 5 4 3 2 1           11 12 13 14 15            1 2 3 4 5
```

---

### 🔴 Level 3 — Diamond, Pascal & Butterfly

**Location:** [`dsa/basics/numbers/level3/`](../dsa/basics/numbers/level3/)

| File | Class | Pattern | Key Formula / Technique |
| :--- | :--- | :--- | :--- |
| `diamond.py` | `NumberDiamond` | Palindrome-row diamond | Pyramid rows 1→n then n-1→1 |
| `pascal_triangle.py` | `PascalTriangle` | Pascal's triangle with binomial coefficients | $C(n,k) = C(n-1,k-1) + C(n-1,k)$ |
| `butterfly.py` | `NumberButterfly` | Mirrored number wings | `1..i` + gap + `1..i`, mirrored vertically |

```
number_diamond (n=4)        pascal_triangle (n=5)         number_butterfly (n=4)
      1                             1                     1          1
    1 2 1                         1   1                   1 2      1 2
  1 2 3 2 1                     1   2   1                 1 2 3  1 2 3
1 2 3 4 3 2 1                 1   3   3   1               1 2 3 41 2 3 4
  1 2 3 2 1                 1   4   6   4   1             1 2 3  1 2 3
    1 2 1                                                 1 2      1 2
      1                                                   1          1
```

---

## Complexity Quick-Reference

| Level | Patterns Covered | Core Challenge |
| :---: | :--- | :--- |
| 1 | Right / Left / Inverted triangle, Square | Controlling loop bounds (`i` vs `n-i`) |
| 2 | Pyramid, Hollow shapes, Floyd, Middle | Space offsets + multi-part rows |
| 3 | Diamond, Hourglass, Butterfly, Pascal | Two-phase loops + mathematical formulas |

---

## How to Run

```bash
# Stars — Level 1
python ./dsa/basics/stars/level1/right_triangle.py
python ./dsa/basics/stars/level1/left_triangle.py
python ./dsa/basics/stars/level1/inverted_triangle.py
python ./dsa/basics/stars/level1/square.py

# Stars — Level 2
python ./dsa/basics/stars/level2/pyramid.py
python ./dsa/basics/stars/level2/inverted_pyramid.py
python ./dsa/basics/stars/level2/hollow_square.py
python ./dsa/basics/stars/level2/hollow_triangle.py

# Stars — Level 3
python ./dsa/basics/stars/level3/diamond.py
python ./dsa/basics/stars/level3/butterfly.py
python ./dsa/basics/stars/level3/hourglass.py

# Numbers — Level 1
python ./dsa/basics/numbers/level1/right_triangle.py
python ./dsa/basics/numbers/level1/left_triangle.py
python ./dsa/basics/numbers/level1/inverted_triangle.py
python ./dsa/basics/numbers/level1/square.py

# Numbers — Level 2
python ./dsa/basics/numbers/level2/pyramid.py
python ./dsa/basics/numbers/level2/floyd_triangle.py
python ./dsa/basics/numbers/level2/middle_triangle.py

# Numbers — Level 3
python ./dsa/basics/numbers/level3/diamond.py
python ./dsa/basics/numbers/level3/pascal_triangle.py
python ./dsa/basics/numbers/level3/butterfly.py
```
