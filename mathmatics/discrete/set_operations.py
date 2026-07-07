class set_operations:
    # the four core set operations, backed directly by Python's built-in set type
    # time complexity O(len(a) + len(b)) for each, space O(len(a) + len(b))
    def union(self,a:set,b:set)->set:
        return a | b

    def intersection(self,a:set,b:set)->set:
        return a & b

    def difference(self,a:set,b:set)->set:
        return a - b

    def symmetric_difference(self,a:set,b:set)->set:
        return a ^ b

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
ops = set_operations()
result = (ops.union(a, b), ops.intersection(a, b), ops.difference(a, b), ops.symmetric_difference(a, b))
print(result)
