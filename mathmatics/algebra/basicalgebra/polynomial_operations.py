class polynomial_operations:
    # a polynomial is represented as a coefficient list, lowest degree first:
    #   [c0, c1, c2, ...] means c0 + c1*x + c2*x^2 + ...
    # add:      pad the shorter list with zeros, then sum term-by-term
    # multiply: every pair of terms (i, j) contributes to the (i+j) coefficient
    # time complexity: add O(N), multiply O(N*M)
    def add(self,p1:list,p2:list)->list:
        n = max(len(p1), len(p2))
        p1 = p1 + [0] * (n - len(p1))
        p2 = p2 + [0] * (n - len(p2))
        return [p1[i] + p2[i] for i in range(n)]

    def multiply(self,p1:list,p2:list)->list:
        result = [0] * (len(p1) + len(p2) - 1)
        for i, c1 in enumerate(p1):
            for j, c2 in enumerate(p2):
                result[i + j] += c1 * c2
        return result

    def evaluate(self,p:list,x:float)->float:
        return sum(coeff * (x ** power) for power, coeff in enumerate(p))

p1 = [1, 2]      # 1 + 2x
p2 = [3, 0, 1]   # 3 + x^2
ops = polynomial_operations()
result = (ops.add(p1, p2), ops.multiply(p1, p2))
print(result)
