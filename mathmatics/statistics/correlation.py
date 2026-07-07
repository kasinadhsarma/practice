import math

class correlation:
    # Pearson correlation coefficient: covariance normalized by both
    # standard deviations, so it always falls in [-1, 1] regardless of scale
    # time complexity O(N), space O(1)
    def calculate(self,x:list,y:list)->float:
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n

        cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x))
        std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y))

        if std_x == 0 or std_y == 0:
            return None
        return cov / (std_x * std_y)

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
result = correlation().calculate(x, y)
print(result)
