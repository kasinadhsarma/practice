"""
Longest Consecutive Sequence
-----------------------------
Technique : Hashing — set-based lookup to find run boundaries
Idea      : Given an unsorted array of integers, find the length of the
            longest run of consecutive integers (e.g. [100,4,200,1,3,2] has
            the run 1,2,3,4 → length 4), without sorting the whole array.

Formula / Property
    A number `n` is the START of a run only if `n - 1` is NOT in the set.
    Once a start is found, count forward (n+1, n+2, ...) while each value
    is present, to measure that run's length.

    Because every number is only ever counted forward from a true run
    start, each number is visited a total of O(1) amortised times overall.

Steps
    1. Put every number into a hashset for O(1) membership checks.
    2. For each number n in the set:
       a. Skip it if n - 1 is also in the set (n is not a run start).
       b. Otherwise, count forward while n, n+1, n+2, ... are in the set.
       c. Track the longest run length seen.
    3. Return the longest run length found.

Time  Complexity : O(N)  — every number is visited a constant number of times
Space Complexity : O(N)  — hashset holds every number once
"""

class LongestConsecutiveSequence:
    def __init__(self, nums: list):
        self.nums = nums

    def longest_run(self) -> int:
        num_set = set(self.nums)
        longest = 0

        for n in num_set:
            if n - 1 in num_set:
                continue  # not the start of a run

            length = 1
            current = n
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

        return longest


nums = list(map(int, input("enter numbers separated by space: ").split()))
print("longest consecutive run:", LongestConsecutiveSequence(nums).longest_run())
