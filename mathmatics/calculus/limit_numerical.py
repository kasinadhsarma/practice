class limit_numerical:
    # approximates lim(x -> a) f(x) by evaluating f just to either side of
    # a (never exactly at a, since the limit can exist even where f(a)
    # itself is undefined) and averaging the two — this is exactly how a
    # limit is motivated before the formal epsilon-delta definition
    # time complexity O(1) per call (two evaluations of f), space O(1)
    def calculate(self,f,a:float,h:float=1e-6)->float:
        left = f(a - h)
        right = f(a + h)
        return (left + right) / 2

f = lambda x: (x ** 2 - 1) / (x - 1)  # undefined at x=1, but limit is 2
a = 1
result = limit_numerical().calculate(f, a)
print(result)
