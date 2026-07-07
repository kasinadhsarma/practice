class relations:
    # a relation on a set is just a collection of ordered pairs;
    # reflexive:  every element relates to itself            -> (a,a) for all a
    # symmetric:  (a,b) implies (b,a)
    # transitive: (a,b) and (b,c) implies (a,c)
    # an equivalence relation is reflexive AND symmetric AND transitive
    # time complexity O(N^2) to O(N^3) depending on the check, space O(N)
    def is_reflexive(self,elements:set,pairs:set)->bool:
        return all((a, a) in pairs for a in elements)

    def is_symmetric(self,pairs:set)->bool:
        return all((b, a) in pairs for (a, b) in pairs)

    def is_transitive(self,pairs:set)->bool:
        for (a, b) in pairs:
            for (c, d) in pairs:
                if b == c and (a, d) not in pairs:
                    return False
        return True

    def is_equivalence(self,elements:set,pairs:set)->bool:
        return self.is_reflexive(elements, pairs) and self.is_symmetric(pairs) and self.is_transitive(pairs)

elements = {1, 2, 3}
pairs = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
rel = relations()
result = rel.is_equivalence(elements, pairs)
print(result)
