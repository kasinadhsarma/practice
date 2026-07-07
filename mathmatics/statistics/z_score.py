class z_score:
    # standardizes a value: how many standard deviations it sits from the mean
    # z = (x - mean) / std_dev  — z > 3 or < -3 is a common outlier threshold
    # time complexity O(1) per value, space O(1)
    def calculate(self,x:float,mean:float,std_dev:float)->float:
        if std_dev == 0:
            return None
        return (x - mean) / std_dev

x = 8
mean = 5.2
std_dev = 2.4
result = z_score().calculate(x, mean, std_dev)
print(result)
