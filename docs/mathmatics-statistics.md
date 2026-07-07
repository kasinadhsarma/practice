# 📊 Mathematics — Statistics

**Location:** [`mathmatics/statistics/`](../mathmatics/statistics/)

Descriptive statistics — summarizing a dataset with a handful of numbers: where it's centered, how spread out it is, and how two variables relate. Each file is a standalone, self-contained class (no cross-file imports) with a runnable demo.

---

## Operations

| File | Class | Description | Time Complexity |
| :--- | :--- | :--- | :--- |
| `mean.py` | `mean` | Arithmetic average: $\bar{x} = \frac{\sum x_i}{N}$ | $\mathcal{O}(N)$ |
| `median.py` | `median` | Middle value of sorted data (average of two middles if $N$ is even) | $\mathcal{O}(N \log N)$ |
| `mode.py` | `mode` | Most frequently occurring value(s) — handles multimodal data | $\mathcal{O}(N)$ |
| `data_range.py` | `data_range` | $\max(x) - \min(x)$ | $\mathcal{O}(N)$ |
| `variance.py` | `variance` | Average squared deviation from the mean — population ($\div N$) or sample ($\div N-1$) | $\mathcal{O}(N)$ |
| `standard_deviation.py` | `standard_deviation` | $\sqrt{\text{variance}}$ — spread in the data's own units | $\mathcal{O}(N)$ |
| `quartiles_iqr.py` | `quartiles_iqr` | $Q_1$, $Q_2$, $Q_3$, and $\text{IQR} = Q_3 - Q_1$ | $\mathcal{O}(N \log N)$ |
| `covariance.py` | `covariance` | How two variables move together | $\mathcal{O}(N)$ |
| `correlation.py` | `correlation` | Pearson's $r$ — covariance normalized into $[-1, 1]$ | $\mathcal{O}(N)$ |
| `z_score.py` | `z_score` | $z = \frac{x - \mu}{\sigma}$ — how many std-devs from the mean | $\mathcal{O}(1)$ |

**Why sample variance divides by $N-1$:** the sample mean $\bar{x}$ is itself computed from the data, using up one degree of freedom — dividing by $N-1$ (Bessel's correction) corrects the resulting slight underestimate of the true population variance.

---

## How to Run

```bash
python ./mathmatics/statistics/mean.py
python ./mathmatics/statistics/median.py
python ./mathmatics/statistics/mode.py
python ./mathmatics/statistics/data_range.py
python ./mathmatics/statistics/variance.py
python ./mathmatics/statistics/standard_deviation.py
python ./mathmatics/statistics/quartiles_iqr.py
python ./mathmatics/statistics/covariance.py
python ./mathmatics/statistics/correlation.py
python ./mathmatics/statistics/z_score.py
```
