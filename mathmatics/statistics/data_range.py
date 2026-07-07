class data_range:
    # spread between the largest and smallest value
    # time complexity O(N), space O(1)
    def calculate(self,data:list)->float:
        if not data:
            return None
        return max(data) - min(data)

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = data_range().calculate(data)
print(result)
