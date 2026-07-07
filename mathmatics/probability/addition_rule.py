class addition_rule:
    # P(A or B) = P(A) + P(B) - P(A and B)
    # the overlap is subtracted once so it isn't double-counted;
    # pass p_a_and_b=0 for mutually exclusive events
    # time complexity O(1), space O(1)
    def calculate(self,p_a:float,p_b:float,p_a_and_b:float=0)->float:
        return p_a + p_b - p_a_and_b

p_a = 0.5   # e.g. rolling an even number
p_b = 0.33  # e.g. rolling a multiple of 3
p_a_and_b = 1/6  # rolling a 6 (even AND multiple of 3)
result = addition_rule().calculate(p_a, p_b, p_a_and_b)
print(result)
