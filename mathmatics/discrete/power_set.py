class power_set:
    # every possible subset of a set, including the empty set and the set itself
    # a set of size N has exactly 2^N subsets — build them by treating each
    # of the N bits of a counter from 0 to 2^N-1 as "include this element?"
    # time complexity O(N * 2^N), space O(N * 2^N)
    def calculate(self,elements:list)->list:
        n = len(elements)
        subsets = []
        for mask in range(2 ** n):
            subset = [elements[i] for i in range(n) if mask & (1 << i)]
            subsets.append(subset)
        return subsets

elements = [1, 2, 3]
result = power_set().calculate(elements)
print(result)
