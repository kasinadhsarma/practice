class cartesian_product:
    # every possible ordered pair (a, b) with a from set A and b from set B
    # |A x B| = |A| * |B|
    # time complexity O(N * M), space O(N * M)
    def calculate(self,a:list,b:list)->list:
        return [(x, y) for x in a for y in b]

a = [1, 2]
b = ['x', 'y', 'z']
result = cartesian_product().calculate(a, b)
print(result)
