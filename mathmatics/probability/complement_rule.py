class complement_rule:
    # P(not A) = 1 - P(A) — everything that isn't A, in the same sample space
    # time complexity O(1), space O(1)
    def calculate(self,p_event:float)->float:
        if not (0 <= p_event <= 1):
            return None
        return 1 - p_event

p_event = 0.3
result = complement_rule().calculate(p_event)
print(result)
