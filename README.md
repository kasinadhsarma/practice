# 📐 Python Programming Foundations & Practice

A highly structured, modular, and academic portfolio of Python programming exercises. The repository is organized into three major areas of study: **Basic Calculations**, **Data Structures & Algorithms (DSA) Basics**, and **Object-Oriented Programming (OOP) Geometry**.

---

## 📂 Repository Structure

```text
d:\pratice\
├── basiccalculations\       # 🧮 Simple procedural arithmetic
│   ├── addition.py
│   ├── substraction.py
│   ├── multiplication.py
│   └── division.py
├── dsa\                     # 🌲 Data Structures & Algorithms (DSA)
│   └── basics\
│       ├── logic\           # Logic, Digit Manipulation & Series (OOP-based)
│       │   ├── level1\      # Basic Conditions & Branching
│       │   ├── level2\      # Digit-by-Digit Extraction
│       │   └── level3\      # Series, Factors, & Divisor Search
│       ├── numbers\         # Centered, left, & right-aligned number pyramids
│       └── stars\           # Centered, left, & right-aligned star patterns
└── oops\                    # 🧱 Object-Oriented Programming (OOP)
    └── geometry\            # Geometric calculations using classes & objects
        ├── areas\           # 2D Surface Area Calculations
        ├── perimeter\       # 2D Boundary Perimeter Calculations
        ├── surface\         # Specific 3D Curved Surface Calculations
        ├── surfacearea\     # 3D Total Surface Area Calculations
        ├── volume\          # 3D Space Volume Calculations
        └── pythogorentherom.py
```

---

## 🧮 1. Basic Calculations
Located in [`basiccalculations/`](file:///d:/pratice/basiccalculations/).

These represent straightforward, top-to-bottom procedural executions. Each script takes two integers from user input, applies a standard arithmetic operator, and prints the result.

| Program | Operation | Input Fields |
| :--- | :--- | :--- |
| `addition.py` | Addition (`a + b`) | Value of `a`, Value of `b` |
| `substraction.py` | Subtraction (`a - b`) | First number, Second number |
| `multiplication.py` | Multiplication (`a * b`) | First number, Second number |
| `division.py` | Division (`a / b`) | First number, Second number |

---

## 🌲 2. DSA Basics: Logic Levels
Located in [`dsa/basics/logic/`](file:///d:/pratice/dsa/basics/logic/).

These logic exercises are structured into three progression levels, designed to master logic branching, number theory, loop controls, and mathematical search. All scripts are implemented using **OOP Classes** for clean encapsulation.

> [!NOTE]
> All algorithms in Level 1 and Level 2 operate in **$\mathcal{O}(1)$ Constant Space Complexity** as they perform all calculations without storing extra data structures in memory.

### 🟢 Level 1: Basic Conditions & Branching
Focuses on simple conditional statements (`if/else` checks) and basic modulo arithmetic.

* **Time Complexity**: $\mathcal{O}(1)$ Constant Time.
* **Problems**:
  * **`even_odd.py`**: Checks if a number is divisible by 2 using the modulo operator (`num % 2 == 0`).
  * **`leapyear.py`**: Determines if a given year is a leap year.

### 🟡 Level 2: Digit Extraction & Manipulation
Introduces extraction of digits from an integer using the modulo operator (`num % 10`) and updating the number using floor division (`num // 10`) in a loop.

* **Time Complexity**: $\mathcal{O}(\log_{10}(N))$ — The number of loop iterations is proportional to the number of digits in the integer $N$.
* **Problems**:
  * **`sum_of_digits.py`**: Iteratively sums every individual digit of an input integer.
  * **`reversenumber.py`**: Reverses the order of digits of an integer (e.g., `123` $\rightarrow$ `321`).
  * **`palindrome_number.py`**: Checks if an integer reads the same forward and backward.
  * **`armstrong_number.py`**: Checks if the sum of the cubes of each digit is equal to the number itself (e.g., $1^3 + 5^3 + 3^3 = 153$).
  * **`strong_number.py`**: Checks if the sum of the factorials of each digit is equal to the number itself (e.g., $1! + 4! + 5! = 145$).

### 🔴 Level 3: Series, Factors & Divisor Search
Covers iterative loop progressions, search space optimization (e.g., searching up to $\sqrt{N}$), and classic mathematical series.

* **Problems**:
  * **`prime_check.py`**: Checks if a number is prime (optimized search bounds).
  * **`perfectnumber.py`**: Finds all proper divisors of a number and checks if their sum equals the number (e.g., $1 + 2 + 3 = 6$).
  * **`fabonacci.py`**: Generates the Fibonacci sequence up to $N$ iterations.
  * **`factorial.py`**: Computes the factorial product of all positive integers up to $N$.
  * **`gcd.py`**: Calculates the Greatest Common Divisor of two integers using Euclid's logarithmic algorithm.

---

## 🌲 3. DSA Basics: Pattern Printing
Located in [`dsa/basics/`](file:///d:/pratice/dsa/basics/).

These programs teach loop bounds, horizontal/vertical coordination, and space calculation. 
* **Time Complexity**: $\mathcal{O}(N^2)$ (Quadratic time due to nested loops).
* **Space Complexity**: $\mathcal{O}(1)$ (Output is streamed directly).

### 🌟 Star Patterns (`stars/`)
* **`rightangletraingle.py`**: Standard left-aligned right triangle.
* **`leftangletriangle.py`**: Right-aligned right triangle using leading space offsets.
* **`middletraingle.py`**: Centered star pyramid.

### 🔢 Number Patterns (`numbers/`)
* **`rightangletraingle.py`**: Left-aligned incrementing number rows.
* **`leftangletriangle.py`**: Right-aligned incrementing number rows.
* **`middletriangle.py`**: Centered number pyramid.

---

## 🧱 4. Object-Oriented Geometry
Located in [`oops/geometry/`](file:///d:/pratice/oops/geometry/).

An advanced, comprehensive geometric toolkit representing shapes and calculations using **Classes, Encapsulated Attributes, and Methods**.

> [!TIP]
> All geometric calculations operate in **$\mathcal{O}(1)$ Constant Time** and **$\mathcal{O}(1)$ Constant Space**.

### Shape Class Specifications

| Class Directory | Class Name | Calculated Property | Mathematical Formula |
| :--- | :--- | :--- | :--- |
| **`areas/`** | `circle.py` | 2D Area | $\pi \times r^2$ |
| | `circlualarring.py` | 2D Ring Area | $\pi \times (R^2 - r^2)$ |
| | `cube.py` | 3D Face Area | $6 \times a^2$ |
| | `parallelogram.py` | 2D Area | $b \times h$ |
| | `rectangle.py` | 2D Area | $l \times b$ |
| | `square.py` | 2D Area | $s^2$ |
| | `trapezoid.py` | 2D Area | $h \times \frac{b1 + b2}{2}$ |
| | `triangle.py` | 2D Area | $0.5 \times b \times h$ |
| **`perimeter/`** | `square.py` | 2D Perimeter | $4 \times s$ |
| | `rectangle.py` | 2D Perimeter | $2 \times (l + w)$ |
| | `traingle.py` | 2D Perimeter | $a + b + c$ |
| | `parallelogram.py` | 2D Perimeter | $2 \times (a + b)$ |
| | `trapezoid.py` | 2D Perimeter | $a + b1 + b2 + c$ |
| **`surface/`** | `rightcircularcone.py` | Curved Surface Area | $\pi \times r \times \sqrt{r^2 + h^2}$ |
| **`surfacearea/`**| `cube.py` | Total Surface Area | $6 \times s^2$ |
| | `cylinder.py` | Total Surface Area | $2 \times \pi \times r \times (h + r)$ |
| | `rectanglularprism` | Total Surface Area | $2 \times (lw + lh + wh)$ |
| | `rightcircularcone` | Total Surface Area | $\pi \times r^2 + \pi \times r \times \sqrt{r^2 + h^2}$ |
| | `sphere.py` | Total Surface Area | $4 \times \pi \times r^2$ |
| **`volume/`** | `cube.py` | 3D Volume | $s^3$ |
| | `cylinder.py` | 3D Volume | $\pi \times r^2 \times h$ |
| | `rectanglularprism` | 3D Volume | $l \times w \times h$ |
| | `rightcircularcone`| 3D Volume | $\frac{1}{3} \times \pi \times r^2 \times h$ |
| | `sphere.py` | 3D Volume | $\frac{4}{3} \times \pi \times r^3$ |
| **Root** | `pythogorentherom.py`| Hypotenuse Square | $a^2 + b^2$ |

---

## 🚀 How to Run

Execute any file from the root directory using Python 3:

```bash
# Run a Level 2 Logic check
python ./dsa/basics/logic/level2/strong_number.py

# Run a Volume calculation
python ./oops/geometry/volume/cylinder.py
```
