class WhileLoop:
    """
    Demonstrates the basic `while` loop.

    countdown()  -> list counting down from n to 1  : O(N) time, O(N) space
    sum_upto()   -> sum of 1..n using a while loop   : O(N) time, O(1) space
    """

    def __init__(self, n: int):
        self.n = n

    def countdown(self) -> list:
        values = []
        current = self.n
        while current > 0:
            values.append(current)
            current -= 1
        return values

    def sum_upto(self) -> int:
        total = 0
        i = 1
        while i <= self.n:
            total += i
            i += 1
        return total


n = int(input("Enter n: "))
loop = WhileLoop(n)
print("Countdown:", loop.countdown())
print("Sum 1..n:", loop.sum_upto())
