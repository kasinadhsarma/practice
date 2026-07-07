# 📐 Mathematics — Trigonometry

**Location:** [`mathmatics/trigonometry/`](../mathmatics/trigonometry/)

Angles, triangles, and the ratios that connect them — starting from right-triangle ratios and extending to any triangle (Law of Sines/Cosines) and any angle (unit circle). Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `trig_ratios.py` | `trig_ratios` | $\sin$, $\cos$, $\tan$ from right-triangle side lengths, plus recovering the angle | $\mathcal{O}(1)$ |
| `pythagorean_identity.py` | `pythagorean_identity` | Verifies $\sin^2\theta + \cos^2\theta = 1$ for any angle | $\mathcal{O}(1)$ |
| `law_of_sines.py` | `law_of_sines` | $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}$ — solves for a missing side in any triangle | $\mathcal{O}(1)$ |
| `law_of_cosines.py` | `law_of_cosines` | $c^2 = a^2 + b^2 - 2ab\cos C$ — generalizes Pythagoras to non-right triangles; solves for a side or an angle | $\mathcal{O}(1)$ |
| `unit_circle.py` | `unit_circle` | Maps any angle to $(\cos\theta, \sin\theta)$ on the unit circle | $\mathcal{O}(1)$ |

---

## How to Run

```bash
python ./mathmatics/trigonometry/trig_ratios.py
python ./mathmatics/trigonometry/pythagorean_identity.py
python ./mathmatics/trigonometry/law_of_sines.py
python ./mathmatics/trigonometry/law_of_cosines.py
python ./mathmatics/trigonometry/unit_circle.py
```
