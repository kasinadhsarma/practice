# 📐 Python Programming Foundations & Practice

A structured repository containing essential Python practice programs. The codebase is organized into modular directories representing core concepts: **Basic Arithmetic**, **Data Structures & Algorithms (DSA) Foundations**, and **Object-Oriented Programming (OOP) Geometry**.

---

## 📂 Repository Structure

```text
d:\pratice\
├── basiccalculations\       # 🧮 Basic sequential arithmetic operations
│   ├── addition.py
│   ├── substraction.py
│   ├── multiplication.py
│   └── division.py
├── dsa\                     # 🌲 Data Structures & Algorithms (DSA)
│   └── basics\
│       ├── numbers\         # Centered, left, & right-aligned number pyramids
│       └── stars\           # Centered, left, & right-aligned star patterns
├── oops\                    # 🧱 Object-Oriented Programming (OOP)
│   └── geometry\
│       └── areas\           # Geometric area calculations via Classes/Objects
│           ├── circle.py
│           ├── circlualarring.py
│           ├── cube.py
│           ├── parallelogram.py
│           ├── rectangle.py
│           ├── square.py
│           └── triangle.py
└── README.md
```

---

## 🧮 1. Basic Calculations
Located in [`basiccalculations/`](file:///d:/pratice/basiccalculations/).

These are beginner-friendly, procedural scripts representing sequential execution flows. Each script takes user input, applies simple arithmetic operations, and displays the result.

| Program | Operation | Input Fields |
| :--- | :--- | :--- |
| `addition.py` | Addition (`a + b`) | Value of `a`, Value of `b` |
| `substraction.py` | Subtraction (`a - b`) | First number, Second number |
| `multiplication.py` | Multiplication (`a * b`) | First number, Second number |
| `division.py` | Division (`a / b`) | First number, Second number |

---

## 🌲 2. DSA Basics: Pattern Printing
Located in [`dsa/basics/`](file:///d:/pratice/dsa/basics/).

These programs represent fundamental loop structures and logic. They practice **nested loop flows**, **boundary controls**, and **quadratic complexity analysis**.

### Complexity Analysis
* **Time Complexity**: $\mathcal{O}(N^2)$ — Two nested loops traversing the horizontal and vertical bounds.
* **Space Complexity**: $\mathcal{O}(1)$ — Characters are printed directly to the output stream without memory storage.

### 🌟 Star Patterns (`stars/`)
1. **Right-Angled Triangle (`rightangletraingle.py`)**
   ```text
   *
   **
   ***
   ****
   *****
   ```
2. **Left-Angled (Right-Aligned) Triangle (`leftangletriangle.py`)**
   ```text
   *
  **
 ***
****
   ```
3. **Centered Pyramid / Middle Triangle (`middletraingle.py`)**
   ```text
       * 
      * * 
     * * * 
    * * * * 
   * * * * * 
   ```

### 🔢 Number Patterns (`numbers/`)
1. **Right-Angled Triangle (`rightangletraingle.py`)**
   ```text
   1 
   1 2 
   1 2 3 
   1 2 3 4 
   1 2 3 4 5 
   ```
2. **Left-Angled (Right-Aligned) Triangle (`leftangletriangle.py`)**
   ```text
           1 
         1 2 
       1 2 3 
     1 2 3 4 
   1 2 3 4 5 
   ```
3. **Centered Pyramid / Middle Triangle (`middletriangle.py`)**
   ```text
       1 
      1 2 
     1 2 3 
    1 2 3 4 
   1 2 3 4 5 
   ```

---

## 🧱 3. Object-Oriented Geometry
Located in [`oops/geometry/areas/`](file:///d:/pratice/oops/geometry/areas/).

These programs introduce Object-Oriented Programming (OOP) principles by representing geometric shapes as classes. Data is encapsulated within object attributes and behavior is implemented via methods.

> [!NOTE]
> All geometric area calculation scripts operate in **$\mathcal{O}(1)$ Constant Time** and **$\mathcal{O}(1)$ Constant Space** complexity.

### Shape Class Specifications

| Shape / Class | File Name | Formula Used | Parameters Encapsulated |
| :--- | :--- | :--- | :--- |
| `areaofcircle` | `circle.py` | $\pi \times r^2$ | `radius` |
| `circularring` | `circlualarring.py` | $\pi \times (R^2 - r^2)$ | Outer Radius `R`, Inner Radius `r` |
| `cube` | `cube.py` | $6 \times a^2$ | Side length `a` |
| `areaofparallelogram` | `parallelogram.py` | $b \times h$ | Base `base`, Height `height` |
| `Rectangle` | `rectangle.py` | $l \times b$ | Length `length`, Breadth `breadth` |
| `Square` | `square.py` | $s^2$ | Side length `side` |
| `triangle` | `triangle.py` | $0.5 \times b \times h$ | Base `base`, Height `height` |

---

## 🚀 Getting Started

To run any of the files, execute them using Python 3:

```bash
# Run a basic calculation script
python ./basiccalculations/addition.py

# Run a DSA pattern printing script
python ./dsa/basics/numbers/middletriangle.py

# Run an OOP geometry calculation script
python ./oops/geometry/areas/circle.py
```
