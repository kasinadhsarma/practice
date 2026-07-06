class MutualRecursion:
    """
    Demonstrates mutual recursion: two functions that call each other
    instead of calling themselves directly. is_even(n) is defined in
    terms of is_odd(n-1), and vice versa, each peeling off one from n
    until reaching the base cases 0 and 1.

    is_even() -> True if n is even, via is_odd(n-1)
    is_odd()  -> True if n is odd,  via is_even(n-1)
    Base cases : is_even(0) = True,  is_odd(0) = False
    Time Complexity  : O(N) — N total calls split across both methods
    Space Complexity : O(N) — recursion call stack
    """

    def is_even(self, n: int) -> bool:
        if n == 0:
            return True
        return self.is_odd(n - 1)

    def is_odd(self, n: int) -> bool:
        if n == 0:
            return False
        return self.is_even(n - 1)


n = int(input("Enter n: "))
mr = MutualRecursion()
print(f"{n} is even:", mr.is_even(n))
print(f"{n} is odd:", mr.is_odd(n))
