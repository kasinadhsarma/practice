# 🔑 DSA — Hashing Algorithms

**Location:** [`dsa/hashing/`](../dsa/hashing/)

Seven algorithms built around hashmaps (or fixed-size arrays used as hash tables) for O(1) average-time lookups — string mapping, frequency counting, and prefix-sum tricks. Each implemented as an OOP class with detailed complexity analysis.

---

## Algorithms

### 🔤 Isomorphic Strings — `isomorphic_strings.py`

Checks whether two strings can be mapped character-for-character onto each other via a consistent, bijective (two-way) mapping — e.g. `"egg" ~ "add"`.

| Property | Detail |
|:---|:---|
| **Approach** | Two hashmaps enforcing a 1:1 mapping in both directions |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(1)$ — bounded alphabet size |

---

### 🔡 Character Frequency Deficit — `char_frequency_deficit.py`

Given strings S and R, finds the minimum number of characters in S that must be replaced so every letter S needs is available in R's supply.

| Property | Detail |
|:---|:---|
| **Approach** | Two 26-slot frequency arrays (fixed-size hash table) |
| **Time Complexity** | $\mathcal{O}(N + M)$ |
| **Space Complexity** | $\mathcal{O}(1)$ |

---

### ➕ Two Sum — `two_sum.py`

Finds the indices of two numbers in an array that add up to a target, in a single pass using a complement lookup.

| Property | Detail |
|:---|:---|
| **Approach** | Hashmap of value → index, checking for `target - num` |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(N)$ |

---

### 🔠 Group Anagrams — `group_anagrams.py`

Groups words that are anagrams of each other, using each word's sorted-letters form as a canonical hashmap key.

| Property | Detail |
|:---|:---|
| **Approach** | Hashmap keyed on sorted letters |
| **Time Complexity** | $\mathcal{O}(N \times K \log K)$ |
| **Space Complexity** | $\mathcal{O}(N \times K)$ |

---

### 📈 Longest Consecutive Sequence — `longest_consecutive_sequence.py`

Finds the length of the longest run of consecutive integers in an unsorted array, without sorting.

| Property | Detail |
|:---|:---|
| **Approach** | Hashset membership + only counting forward from true run starts |
| **Time Complexity** | $\mathcal{O}(N)$ — amortised, every number visited a constant number of times |
| **Space Complexity** | $\mathcal{O}(N)$ |

---

### 🔍 First Unique Character — `first_unique_character.py`

Finds the index of the first character in a string that appears exactly once.

| Property | Detail |
|:---|:---|
| **Approach** | Frequency hashmap, then a second pass to find the first count-1 character |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(1)$ — bounded alphabet size |

---

### ∑ Subarray Sum Equals K — `subarray_sum_equals_k.py`

Counts how many contiguous subarrays sum to exactly `k`, using running prefix sums and a hashmap of how often each prefix sum has occurred.

| Property | Detail |
|:---|:---|
| **Approach** | Prefix-sum frequency hashmap: `prefix[j] == prefix[i] - k` |
| **Time Complexity** | $\mathcal{O}(N)$ |
| **Space Complexity** | $\mathcal{O}(N)$ |

---

## How to Run

```bash
python ./dsa/hashing/isomorphic_strings.py
python ./dsa/hashing/char_frequency_deficit.py
python ./dsa/hashing/two_sum.py
python ./dsa/hashing/group_anagrams.py
python ./dsa/hashing/longest_consecutive_sequence.py
python ./dsa/hashing/first_unique_character.py
python ./dsa/hashing/subarray_sum_equals_k.py
```
