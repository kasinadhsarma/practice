import math

class StrongNumber:
    # A number is STRONG if the sum of factorials of its digits equals the number.
    # Formula: N == (d1)! + (d2)! + ... + (dk)!
    # Example: 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145  ✓
    # Time Complexity:  O(d) where d = number of digits (at most 7 for reasonable inputs)
    # Space Complexity: O(1)

    def __init__(self, N: int):
        self.N = N

    def is_strong(self) -> bool:
        temp = self.N
        factorial_sum = 0
        while temp > 0:
            digit = temp % 10
            factorial_sum += math.factorial(digit)
            temp //= 10
        return factorial_sum == self.N

    def find_strong_numbers(self, limit: int) -> list:
        """Return all strong numbers up to `limit`."""
        result = []
        for num in range(1, limit + 1):
            temp, s = num, 0
            while temp > 0:
                s += math.factorial(temp % 10)
                temp //= 10
            if s == num:
                result.append(num)
        return result


N = int(input("Enter the number: "))
sn = StrongNumber(N)
print(f"{N} is {'a Strong Number' if sn.is_strong() else 'NOT a Strong Number'}")

limit = int(input("Find all strong numbers up to: "))
print(f"Strong numbers up to {limit}: {sn.find_strong_numbers(limit)}")
