class covariance:
    # measures how two variables move together: positive when they rise
    # together, negative when one rises as the other falls
    # time complexity O(N), space O(1)
    def calculate(self,x:list,y:list)->float:
        if len(x) != len(y) or len(x) == 0:
            return None
        n = len(x)
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        return sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n)) / n

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
result = covariance().calculate(x, y)
print(result)
