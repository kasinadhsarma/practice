# 🔢 Mathematics — Number Theory

**Location:** [`mathmatics/number_theory/`](../mathmatics/number_theory/)

The properties of integers themselves — divisibility, primes, and factorization. Complements [Discrete Math](./mathmatics-discrete.md)'s `modular_arithmetic.py`, which builds on the `gcd_lcm.py` idea here. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `gcd_lcm.py` | `gcd_lcm` | Euclidean algorithm for $\gcd$, then $\text{lcm}(a,b) = \frac{ab}{\gcd(a,b)}$ | $\mathcal{O}(\log(\min(a,b)))$ |
| `prime_sieve.py` | `prime_sieve` | Sieve of Eratosthenes — every prime up to $N$ in one pass | $\mathcal{O}(N \log \log N)$ |
| `prime_factorization.py` | `prime_factorization` | Trial division down to $\sqrt{N}$ to find $N$'s full prime factorization | $\mathcal{O}(\sqrt{N})$ |
| `euler_totient.py` | `euler_totient` | $\phi(n)$ — count of integers in $[1,n]$ coprime to $n$, via the product formula over distinct prime factors | $\mathcal{O}(\sqrt{N})$ |

---

## How to Run

```bash
python ./mathmatics/number_theory/gcd_lcm.py
python ./mathmatics/number_theory/prime_sieve.py
python ./mathmatics/number_theory/prime_factorization.py
python ./mathmatics/number_theory/euler_totient.py
```
