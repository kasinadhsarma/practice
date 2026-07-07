# ∫ Mathematics — Calculus

**Location:** [`mathmatics/calculus/`](../mathmatics/calculus/)

Rates of change and accumulation — derivatives, integrals, and the limits underneath both. Approached two ways: numerically (approximating via small steps, works for *any* function) and symbolically (exact, for polynomials specifically). Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `limit_numerical.py` | `limit_numerical` | Approximates $\lim_{x \to a} f(x)$ by evaluating just to either side of $a$ | $\mathcal{O}(1)$ |
| `derivative_numerical.py` | `derivative_numerical` | Central difference approximation $f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$ — works for any function | $\mathcal{O}(1)$ |
| `power_rule_derivative.py` | `power_rule_derivative` | Exact symbolic derivative of a polynomial via the power rule $\frac{d}{dx}(c x^n) = cn\,x^{n-1}$ | $\mathcal{O}(N)$ |
| `integral_numerical.py` | `integral_numerical` | Trapezoidal-rule approximation of $\int_a^b f(x)\,dx$ | $\mathcal{O}(N)$ steps |

**Why numerical AND symbolic:** the numerical derivative/limit work on *any* Python function (including ones with no closed form), while the power-rule derivative is exact but only applies to polynomials — the two approaches complement each other.

---

## How to Run

```bash
python ./mathmatics/calculus/limit_numerical.py
python ./mathmatics/calculus/derivative_numerical.py
python ./mathmatics/calculus/power_rule_derivative.py
python ./mathmatics/calculus/integral_numerical.py
```
