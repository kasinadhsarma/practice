class mean:
    # arithmetic mean: sum of values divided by count
    # time complexity O(N), space O(1)
    def calculate(self,data:list)->float:
        if not data:
            return None
        return sum(data) / len(data)

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = mean().calculate(data)
print(result)
