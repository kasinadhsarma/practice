class expected_value_variance:
    # for a discrete random variable given as (value, probability) pairs:
    # E[X]   = sum(x * P(x))                — the long-run average outcome
    # Var[X] = sum((x - E[X])^2 * P(x))     — average squared spread around E[X]
    # time complexity O(N), space O(1)
    def expected_value(self,values:list,probabilities:list)->float:
        return sum(values[i] * probabilities[i] for i in range(len(values)))

    def variance(self,values:list,probabilities:list)->float:
        e_x = self.expected_value(values, probabilities)
        return sum(((values[i] - e_x) ** 2) * probabilities[i] for i in range(len(values)))

# a fair six-sided die
values = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6
evv = expected_value_variance()
result = (evv.expected_value(values, probabilities), evv.variance(values, probabilities))
print(result)
