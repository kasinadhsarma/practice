"""
Subarray Sum Equals K
----------------------
Technique : Hashing — prefix-sum frequency map
Idea      : Count how many contiguous subarrays sum to exactly k. Instead of
            checking every subarray (O(n^2)), track running prefix sums and
            how often each prefix sum value has occurred so far.

Formula / Property
    prefix[i] = sum of the first i elements (prefix[0] = 0)
    A subarray (j+1 .. i) sums to k  iff  prefix[i] - prefix[j] == k
                                     iff  prefix[j] == prefix[i] - k

    So at each index i, the number of valid subarrays ending at i equals
    how many times (prefix[i] - k) has already occurred as a prefix sum.

Steps
    1. Initialise a hashmap with {0: 1} (the empty prefix occurs once).
    2. Track a running prefix sum as you scan the array left to right.
    3. At each element, look up (running_sum - k) in the hashmap and add
       its count to the running total of valid subarrays.
    4. Increment the hashmap count for the current running_sum.
    5. Return the total count.

Time  Complexity : O(N)  — single pass, O(1) average hashmap operations
Space Complexity : O(N)  — hashmap holds up to N distinct prefix sums
"""

class SubarraySumEqualsK:
    def __init__(self, nums: list):
        self.nums = nums

    def count_subarrays(self, k: int) -> int:
        prefix_counts = {0: 1}
        running_sum = 0
        total = 0

        for num in self.nums:
            running_sum += num
            total += prefix_counts.get(running_sum - k, 0)
            prefix_counts[running_sum] = prefix_counts.get(running_sum, 0) + 1

        return total


nums = list(map(int, input("enter numbers separated by space: ").split()))
k = int(input("enter target sum k: "))
print("subarrays summing to k:", SubarraySumEqualsK(nums).count_subarrays(k))
