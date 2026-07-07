class geometric_progression:
    # a sequence where each term multiplies the last by a fixed common ratio r
    #   nth_term:        a_n = a1 * r^(n-1)
    #   sum_n_terms:     S_n = a1 * (1 - r^n) / (1 - r)      (r != 1)
    #   sum_to_infinity: S   = a1 / (1 - r)                  (only converges
    #                    when |r| < 1 — otherwise terms never shrink to 0
    #                    and the sum has no finite limit)
    # time complexity O(1), space O(1)
    def nth_term(self,a1:float,r:float,n:int)->float:
        return a1 * (r ** (n - 1))

    def sum_n_terms(self,a1:float,r:float,n:int)->float:
        if r == 1:
            return a1 * n
        return a1 * (1 - r ** n) / (1 - r)

    def sum_to_infinity(self,a1:float,r:float)->float:
        if abs(r) >= 1:
            return None  # diverges — no finite sum
        return a1 / (1 - r)

a1, r, n = 2, 0.5, 5
gp = geometric_progression()
result = (gp.nth_term(a1, r, n), gp.sum_n_terms(a1, r, n), gp.sum_to_infinity(a1, r))
print(result)
