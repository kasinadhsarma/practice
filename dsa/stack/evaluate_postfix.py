"""
Evaluate Postfix Expression
----------------------------
Technique : Stack-based expression evaluation
Idea      : In postfix (Reverse Polish) notation, operators come after
            their operands (e.g. "3 4 +" instead of "3 + 4"), so no
            parentheses or precedence rules are ever needed. Scan left to
            right: push numbers; when an operator is seen, pop the two most
            recent operands, apply the operator, and push the result back.

Steps
    1. Split the expression into tokens.
    2. For each token:
       a. If it's a number, push it onto the stack.
       b. If it's an operator, pop two operands (b, then a — order
          matters for - and /), compute a OP b, and push the result.
    3. After all tokens are processed, the stack holds exactly one value:
       the final result.

Applications
    - Calculators, compilers (expression evaluation without precedence
      parsing)
    - Stack machines / bytecode interpreters

Time  Complexity : O(N) — one pass over the tokens
Space Complexity : O(N) — worst case, all operands pushed before any operator
"""

class EvaluatePostfix:
    OPS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    def __init__(self, expression: str):
        self.tokens = expression.split()

    def evaluate(self):
        stack = []
        for token in self.tokens:
            if token in self.OPS:
                if len(stack) < 2:
                    return None  # malformed expression — not enough operands
                b = stack.pop()
                a = stack.pop()
                stack.append(self.OPS[token](a, b))
            else:
                stack.append(float(token))
        return stack[0] if len(stack) == 1 else None


expr = input("enter postfix expression (space-separated, e.g. '3 4 + 2 *'): ")
print("result:", EvaluatePostfix(expr).evaluate())
