class conditional_probability:
    # P(A|B) = P(A and B) / P(B) — probability of A, restricted to the
    # outcomes where B is already known to have happened
    # time complexity O(1), space O(1)
    def calculate(self,p_a_and_b:float,p_b:float)->float:
        if p_b == 0:
            return None
        return p_a_and_b / p_b

p_a_and_b = 0.15
p_b = 0.5
result = conditional_probability().calculate(p_a_and_b, p_b)
print(result)
