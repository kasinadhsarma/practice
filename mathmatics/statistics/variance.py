class variance:
    # average squared deviation from the mean
    # population variance divides by N; sample variance divides by N-1
    # (sample uses N-1, Bessel's correction, since the sample mean itself
    # already uses up one degree of freedom)
    # time complexity O(N), space O(1)
    def calculate(self,data:list,sample:bool=False)->float:
        n = len(data)
        if n == 0 or (sample and n < 2):
            return None
        avg = sum(data) / n
        squared_deviations = sum((x - avg) ** 2 for x in data)
        denominator = (n - 1) if sample else n
        return squared_deviations / denominator

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = variance().calculate(data)
print(result)
