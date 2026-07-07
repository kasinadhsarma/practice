class arithmetic_progression:
    # a sequence where each term adds a fixed common difference d to the last
    #   nth_term:    a_n = a1 + (n-1)*d
    #   sum_n_terms: S_n = n/2 * (2*a1 + (n-1)*d)  — derived by pairing the
    #                first and last terms, which both sum to (a1 + a_n)
    # time complexity O(1), space O(1)
    def nth_term(self,a1:float,d:float,n:int)->float:
        return a1 + (n - 1) * d

    def sum_n_terms(self,a1:float,d:float,n:int)->float:
        return (n / 2) * (2 * a1 + (n - 1) * d)

a1, d, n = 3, 5, 10
ap = arithmetic_progression()
result = (ap.nth_term(a1, d, n), ap.sum_n_terms(a1, d, n))
print(result)
