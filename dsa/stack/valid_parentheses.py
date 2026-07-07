"""
Valid Parentheses
------------------
Technique : Stack matching
Idea      : Brackets nest — the most recently opened bracket must be the
            next one closed. A stack captures exactly that: push every
            opening bracket, and on a closing bracket, it must match
            whatever is currently on top of the stack.

Steps
    1. For each character in the string:
       a. If it is an opening bracket, push it.
       b. If it is a closing bracket:
          - If the stack is empty, or the top doesn't match the expected
            opening bracket, the string is invalid.
          - Otherwise pop the stack.
    2. After processing every character, the string is valid only if the
       stack is empty (no unmatched opens remain).

Applications
    - Syntax validation (code editors, compilers/parsers)
    - HTML/XML tag matching

Time  Complexity : O(N)
Space Complexity : O(N) — worst case, all opening brackets
"""

class ValidParentheses:
    PAIRS = {')': '(', ']': '[', '}': '{'}

    def __init__(self, s: str):
        self.s = s

    def is_valid(self) -> bool:
        stack = []
        for ch in self.s:
            if ch in '([{':
                stack.append(ch)
            elif ch in ')]}':
                if not stack or stack.pop() != self.PAIRS[ch]:
                    return False
        return len(stack) == 0


s = input("enter a string of brackets: ")
print("valid:", ValidParentheses(s).is_valid())
