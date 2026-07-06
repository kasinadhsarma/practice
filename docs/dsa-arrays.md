# 📦 DSA — Arrays

**Location:** [`dsa/Arrays/`](../dsa/Arrays/)

The most comprehensive chapter in the repo — 11 files, ~144 functions/classes covering essentially every standard array topic: basics & memory layout, searching (7 algorithms + 6 binary-search variants), sorting (11 algorithms), two-pointer & sliding window (14 problems), prefix sum & difference arrays, rotation & rearrangement, classic interview problems, advanced data structures (Segment Tree, Fenwick Tree, Sparse Table, monotonic stack/deque), 2D matrix operations, special array types, and remaining topics (LIS, median of two sorted arrays, merge-k-sorted, max-sum-rectangle, cycle sort, pancake sort, and more).

See [dsa/Arrays/README.md](../dsa/Arrays/README.md) for the full topic map, complexity reference table, and per-file breakdown — this page only covers what that one doesn't: test coverage and known limitations.

---

## Test Coverage

All 144 functions/classes are covered by [tests/dsa/test_dsa_arrays.py](../tests/dsa/test_dsa_arrays.py) (485 test cases). Since this chapter is function-based (not class-based like the rest of `dsa/`), tests call functions directly after loading each file as a module.

### Bugs found and fixed during test-writing

Two real correctness bugs in `02_searching.py` were found and fixed while writing exhaustive tests (not present in any other file):

- **`exponential_search`** returned an index relative to the internal array *slice* it binary-searches, instead of the absolute index in the original array — fixed by adding the missing offset.
- **`fibonacci_search`** infinite-looped for certain targets (e.g. searching for the smallest element) due to a tuple-assignment bug: `fib, fib1, fib2 = fib2, fib1 - fib2, fib - fib1` evaluates all three expressions against the *old* values simultaneously, but the correct Fibonacci-search recurrence requires the third expression to use the *already-updated* `fib`/`fib1` (sequential, not simultaneous, assignment). Rewritten as three sequential statements. A related out-of-bounds read (`arr[offset + 1]` when the target exceeds every element) was also guarded.

### Known limitations (documented via `pytest.raises`, not changed)

A few functions have pre-existing edge-case gaps that are narrow enough (degenerate inputs, not common usage) to document rather than patch:

- `jump_search`, `exponential_search` — raise `IndexError` on an empty array (no guard before the first index access).
- `interpolation_search` — raises `ZeroDivisionError` on a constant-valued array with more than one element (the probe-position formula divides by `arr[hi] - arr[lo]`).

### Stale comments corrected in tests, not in source

A few inline `# expected value` comments throughout the `Arrays/` files turned out to be arithmetically wrong (the code itself was already correct). Rather than edit narrative comments across files, the test suite documents the verified-correct value directly:

- `04_two_pointer_sliding_window.py`: `max_ones_with_k_flips([1,1,0,0,1,1,1,0,1,1], 2)` is **7**, not the commented 9.
- `07_classic_problems.py`: `max_profit_II([3,3,5,0,0,3,1,4])` is **8**, not the commented 6.
- `11_remaining_topics.py`: `max_sum_rectangle(...)` on the sample 4×4 matrix is **25** at `(top=1,left=1,bottom=2,right=2)`, not the commented 29 — verified by brute force over every sub-rectangle.

---

## How to Run

```bash
python ./dsa/Arrays/01_basics.py
python ./dsa/Arrays/02_searching.py
python ./dsa/Arrays/03_sorting.py
python ./dsa/Arrays/04_two_pointer_sliding_window.py
python ./dsa/Arrays/05_prefix_sum_difference_array.py
python ./dsa/Arrays/06_array_rotation.py
python ./dsa/Arrays/07_classic_problems.py
python ./dsa/Arrays/08_advanced_techniques.py
python ./dsa/Arrays/09_2d_matrix.py
python ./dsa/Arrays/10_special_arrays.py
python ./dsa/Arrays/11_remaining_topics.py
```
