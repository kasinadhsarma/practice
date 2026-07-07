class modular_arithmetic:
    # mod_pow: fast exponentiation under a modulus via repeated squaring —
    #   avoids ever computing the full (huge) base^exp before reducing
    # mod_inverse: the x such that (a * x) % m == 1, found via the
    #   Extended Euclidean Algorithm (exists only when gcd(a, m) == 1)
    # time complexity: mod_pow O(log exp), mod_inverse O(log m), space O(1)
    def mod_pow(self,base:int,exp:int,mod:int)->int:
        result = 1
        base %= mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    def mod_inverse(self,a:int,m:int)->int:
        old_r, r = a, m
        old_s, s = 1, 0
        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
        if old_r != 1:
            return None  # inverse doesn't exist — gcd(a, m) != 1
        return old_s % m

ma = modular_arithmetic()
result = (ma.mod_pow(4, 13, 497), ma.mod_inverse(3, 11))
print(result)
