class truth_table:
    # enumerates every combination of two boolean variables (p, q) and
    # evaluates every core logical connective against them
    # time complexity O(1) — always exactly 4 rows for 2 variables, space O(1)
    def generate(self)->list:
        rows = []
        for p in (True, False):
            for q in (True, False):
                rows.append({
                    "p": p,
                    "q": q,
                    "AND": p and q,
                    "OR": p or q,
                    "NOT p": not p,
                    "XOR": p != q,
                    "IMPLIES (p->q)": (not p) or q,
                    "IFF (p<->q)": p == q,
                })
        return rows

result = truth_table().generate()
for row in result:
    print(row)
