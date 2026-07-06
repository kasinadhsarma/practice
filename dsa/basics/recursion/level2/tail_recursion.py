class TailRecursion:
    """
    Contrasts a non-tail-recursive sum (work happens AFTER the recursive
    call returns, via "n + recurse(...)") with a tail-recursive version
    (the recursive call is the very last operation, with the running
    total threaded through as an accumulator parameter).

    Note: Python does NOT perform tail-call optimisation, so
    sum_tail_recursive() still grows the call stack just like
    sum_non_tail() — the point here is the pattern itself, which
    languages/compilers that DO optimise tail calls turn into an O(1)
    space loop instead of O(N) stack frames.

    sum_non_tail()   -> n + sum_non_tail(n-1)              : work after the call
    sum_tail_recursive() -> recurse(n-1, acc + n)          : call is the last action
    Time Complexity  : O(N) for both
    Space Complexity : O(N) for both, in Python (see note above)
    """

    def __init__(self, n: int):
        self.n = n

    def sum_non_tail(self) -> int:
        if self.n <= 0:
            return 0
        return self.n + TailRecursion(self.n - 1).sum_non_tail()

    def sum_tail_recursive(self, accumulator: int = 0) -> int:
        if self.n <= 0:
            return accumulator
        return TailRecursion(self.n - 1).sum_tail_recursive(accumulator + self.n)


n = int(input("Enter n: "))
tr = TailRecursion(n)
print("Sum (non-tail):", tr.sum_non_tail())
print("Sum (tail-recursive):", tr.sum_tail_recursive())
