class TowerOfHanoi:
    """
    Move n disks from a source peg to a target peg (using an auxiliary
    peg), never placing a larger disk on top of a smaller one. The
    classic three-way recursive decomposition: move n-1 disks out of the
    way, move the largest disk, then move the n-1 disks back on top.

    solve() -> list of (disk, from_peg, to_peg) moves, in order
    Recurrence : move(n-1, source, aux, target)  ->  move disk n  ->  move(n-1, aux, target, source)
    Time Complexity  : O(2^N) — minimum possible moves is 2^N - 1
    Space Complexity : O(N)   — recursion call stack
    """

    def __init__(self, n: int):
        self.n = n

    def solve(self) -> list:
        moves = []
        self._move(self.n, 'A', 'C', 'B', moves)
        return moves

    def _move(self, n, source, target, auxiliary, moves):
        if n == 0:
            return
        self._move(n - 1, source, auxiliary, target, moves)
        moves.append((n, source, target))
        self._move(n - 1, auxiliary, target, source, moves)

    def minimum_moves(self) -> int:
        return 2 ** self.n - 1


n = int(input("Enter number of disks: "))
hanoi = TowerOfHanoi(n)
for disk, src, dst in hanoi.solve():
    print(f"Move disk {disk} from {src} to {dst}")
print("Minimum moves:", hanoi.minimum_moves())
