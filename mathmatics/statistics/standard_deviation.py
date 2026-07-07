import math

class standard_deviation:
    # square root of variance — spread expressed in the same units as the data
    # time complexity O(N), space O(1)
    def calculate(self,data:list,sample:bool=False)->float:
        n = len(data)
        if n == 0 or (sample and n < 2):
            return None
        avg = sum(data) / n
        squared_deviations = sum((x - avg) ** 2 for x in data)
        denominator = (n - 1) if sample else n
        return math.sqrt(squared_deviations / denominator)

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = standard_deviation().calculate(data)
print(result)
