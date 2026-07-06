"""
Two Sum
-------
Technique : Hashing — single-pass complement lookup
Idea      : Given an array of numbers and a target, find the indices of the
            two numbers that add up to the target. Instead of checking every
            pair (O(n^2)), remember every number seen so far in a hashmap and
            check whether its complement (target - num) has already appeared.

Formula / Property
    For index i with value num:
        complement = target - num
        if complement in seen_map:  seen_map[complement] is the partner index

Steps
    1. Create an empty hashmap (value -> index).
    2. For each index i, value num in the array:
       a. complement = target - num
       b. If complement is already in the map, return (map[complement], i).
       c. Otherwise store map[num] = i and continue.
    3. If no pair is found, return None.

Time  Complexity : O(N)  — single pass, O(1) average hashmap lookups
Space Complexity : O(N)  — hashmap holds up to N entries
"""

class TwoSum:
    def __init__(self, nums: list):
        self.nums = nums

    def find_indices(self, target: int):
        seen = {}
        for i, num in enumerate(self.nums):
            complement = target - num
            if complement in seen:
                return (seen[complement], i)
            seen[num] = i
        return None


nums = list(map(int, input("enter numbers separated by space: ").split()))
target = int(input("enter target sum: "))
result = TwoSum(nums).find_indices(target)
print("indices:", result)
