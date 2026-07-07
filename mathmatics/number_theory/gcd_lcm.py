class gcd_lcm:
    # gcd: the Euclidean algorithm — gcd(a, b) == gcd(b, a % b), bottoming
    #      out once the remainder hits 0
    # lcm: the smallest number divisible by both, derived from gcd via
    #      lcm(a, b) = (a * b) / gcd(a, b)  — since a*b always factors into
    #      gcd(a,b) * lcm(a,b)
    # time complexity O(log(min(a, b))), space O(1)
    def gcd(self,a:int,b:int)->int:
        while b:
            a, b = b, a % b
        return abs(a)

    def lcm(self,a:int,b:int)->int:
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.gcd(a, b)

a, b = 24, 36
gl = gcd_lcm()
result = (gl.gcd(a, b), gl.lcm(a, b))
print(result)
