# 🎲 Mathematics — Probability

**Location:** [`mathmatics/probability/`](../mathmatics/probability/)

Quantifying uncertainty — from the basic favorable/total ratio through conditional probability, Bayes' theorem, combinatorics, and the two most common distributions. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Core Rules

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `probability_of_event.py` | `probability_of_event` | $P(A) = \frac{\text{favorable}}{\text{total}}$ | $\mathcal{O}(1)$ |
| `complement_rule.py` | `complement_rule` | $P(\text{not } A) = 1 - P(A)$ | $\mathcal{O}(1)$ |
| `addition_rule.py` | `addition_rule` | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | $\mathcal{O}(1)$ |
| `conditional_probability.py` | `conditional_probability` | $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ | $\mathcal{O}(1)$ |
| `bayes_theorem.py` | `bayes_theorem` | $P(H \mid E) = \frac{P(E \mid H)\,P(H)}{P(E)}$ — updates a prior belief with evidence | $\mathcal{O}(K)$ hypotheses |

## Combinatorics

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `permutations.py` | `permutations` | $_nP_r = \frac{n!}{(n-r)!}$ — ordered arrangements | $\mathcal{O}(N)$ |
| `combinations.py` | `combinations` | $_nC_r = \frac{n!}{r!(n-r)!}$ — unordered selections | $\mathcal{O}(N)$ |

## Distributions

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `binomial_distribution.py` | `binomial_distribution` | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ — successes in $n$ independent trials | $\mathcal{O}(N)$ per call |
| `expected_value_variance.py` | `expected_value_variance` | $E[X] = \sum x\,P(x)$, $\text{Var}[X] = \sum (x-E[X])^2 P(x)$ | $\mathcal{O}(N)$ |
| `normal_distribution.py` | `normal_distribution` | Bell-curve PDF and CDF (via the error function) for continuous $X$ | $\mathcal{O}(1)$ |

---

## How to Run

```bash
python ./mathmatics/probability/probability_of_event.py
python ./mathmatics/probability/complement_rule.py
python ./mathmatics/probability/addition_rule.py
python ./mathmatics/probability/conditional_probability.py
python ./mathmatics/probability/bayes_theorem.py
python ./mathmatics/probability/permutations.py
python ./mathmatics/probability/combinations.py
python ./mathmatics/probability/binomial_distribution.py
python ./mathmatics/probability/expected_value_variance.py
python ./mathmatics/probability/normal_distribution.py
```
