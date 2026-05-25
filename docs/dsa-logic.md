# 🧠 DSA Basics — Logic Levels

**Location:** [`dsa/basics/logic/`](../dsa/basics/logic/)


Logic exercises structured into **three progressive levels**, covering conditional branching, digit extraction, number theory, and mathematical series.  
All scripts use **OOP classes** for clean encapsulation and include formula comments, time/space complexity, and a runnable demo.

> **Note:** Level 1 and Level 2 algorithms run in $\mathcal{O}(1)$ constant space — no extra data structures stored.

---

## 🟢 Level 1 — Basic Conditions & Branching

**Location:** [`dsa/basics/logic/level1/`](../dsa/basics/logic/level1/)

Focuses on simple `if/else` checks and basic modulo arithmetic.

- **Time Complexity:** $\mathcal{O}(1)$ — constant time  
- **Space Complexity:** $\mathcal{O}(1)$

| File | Class | Description | Key Logic |
| :--- | :--- | :--- | :--- |
| `even_odd.py` | `EvenOdd` | Checks if a number is even or odd | `num % 2 == 0` |
| `leapyear.py` | `LeapYear` | Determines if a year is a leap year | Divisibility by 4, 100, 400 |

---

## 🟡 Level 2 — Digit Extraction & Manipulation

**Location:** [`dsa/basics/logic/level2/`](../dsa/basics/logic/level2/)

Introduces extracting digits using `num % 10` and reducing the number with `num // 10` in a loop.

- **Time Complexity:** $\mathcal{O}(\log_{10} N)$ — one iteration per digit  
- **Space Complexity:** $\mathcal{O}(1)$

| File | Class | Description | Bonus Feature |
| :--- | :--- | :--- | :--- |
| `sum_of_digits.py` | `SumOfDigits` | Iteratively sums every digit of $N$ | `get_digital_root()` — reduces to single digit |
| `reversenumber.py` | `reverseInteger` | Reverses digit order (`123 → 321`) | 32-bit overflow guard |
| `palindrome_number.py` | `palindrome` | Checks if a number reads same forwards & backwards | Returns `"palindrome"` / `"not a palindrome"` |
| `armstrong_number.py` | `armstrong` | $N = d_1^k + d_2^k + \cdots + d_k^k$ | Handles any digit length $k$ |
| `strong_number.py` | `StrongNumber` | $N = d_1! + d_2! + \cdots + d_k!$ (e.g. $145 = 1!+4!+5!$) | `find_strong_numbers(limit)` enumerates all |

---

## 🔴 Level 3 — Series, Factors & Divisor Search

**Location:** [`dsa/basics/logic/level3/`](../dsa/basics/logic/level3/)

Covers iterative / recursive series generation, divisor search, and loop optimisation (searching only up to $\sqrt{N}$).

| File | Class | Description | Time Complexity | Bonus Features |
| :--- | :--- | :--- | :--- | :--- |
| `factorial.py` | `Factorial` | $N! = N \times (N-1) \times \cdots \times 1$ | $\mathcal{O}(N)$ | Iterative + recursive; trailing-zero count |
| `fabonacci.py` | `Fibonacci` | $F(n) = F(n-1) + F(n-2)$ | $\mathcal{O}(N)$ | Iterative + memoised DP; series generator; `is_fibonacci()` |
| `prime_check.py` | `PrimeCheck` | No divisor in $[2,\ \sqrt{N}]$ | $\mathcal{O}(\sqrt{N})$ | Prime factors; Sieve of Eratosthenes; next prime |
| `perfectnumber.py` | `PerfectNumber` | $\sigma(N) - N = N$ (e.g. $1+2+3=6$) | $\mathcal{O}(\sqrt{N})$ | Abundant / Deficient / Perfect classifier |
| `gcd.py` | `GCD` | Euclid: $\gcd(a,b) = \gcd(b,\ a \bmod b)$ | $\mathcal{O}(\log \min(a,b))$ | LCM; Extended GCD (Bézout coefficients); GCD of list |
| `direction_tracker.py` | `DirectionTracker` | 2D grid movement tracker (N/E/S/W) | $\mathcal{O}(N)$ | Turn left / right; `get_position()` |

---

## Complexity Quick-Reference

| Level | Typical Time | Typical Space | Core Technique |
| :---: | :---: | :---: | :--- |
| 1 | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | Conditional / modulo |
| 2 | $\mathcal{O}(\log N)$ | $\mathcal{O}(1)$ | Digit-by-digit loop |
| 3 | $\mathcal{O}(\sqrt{N})$ – $\mathcal{O}(N)$ | $\mathcal{O}(1)$ – $\mathcal{O}(N)$ | Divisor search, Euclidean algorithm, memoisation |

---

## How to Run

```bash
# Level 1
python ./dsa/basics/logic/level1/even_odd.py
python ./dsa/basics/logic/level1/leapyear.py

# Level 2
python ./dsa/basics/logic/level2/sum_of_digits.py
python ./dsa/basics/logic/level2/strong_number.py
python ./dsa/basics/logic/level2/armstrong_number.py
python ./dsa/basics/logic/level2/palindrome_number.py
python ./dsa/basics/logic/level2/reversenumber.py

# Level 3
python ./dsa/basics/logic/level3/factorial.py
python ./dsa/basics/logic/level3/fabonacci.py
python ./dsa/basics/logic/level3/prime_check.py
python ./dsa/basics/logic/level3/perfectnumber.py
python ./dsa/basics/logic/level3/gcd.py
python ./dsa/basics/logic/level3/direction_tracker.py
```
