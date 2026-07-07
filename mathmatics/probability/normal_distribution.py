import math

class normal_distribution:
    # the classic bell curve, defined by mean (mu) and standard deviation (sigma)
    # pdf(x) = (1 / (sigma * sqrt(2*pi))) * e^(-(x-mu)^2 / (2*sigma^2))
    # cdf(x) = P(X <= x), computed via the error function (erf)
    # time complexity O(1), space O(1)
    def pdf(self,x:float,mu:float,sigma:float)->float:
        if sigma <= 0:
            return None
        coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
        exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
        return coefficient * math.exp(exponent)

    def cdf(self,x:float,mu:float,sigma:float)->float:
        if sigma <= 0:
            return None
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

mu = 0
sigma = 1
x = 1.5
result = (normal_distribution().pdf(x, mu, sigma), normal_distribution().cdf(x, mu, sigma))
print(result)
