class functions_properties:
    # a function is given as a dict mapping every domain element to a codomain element
    # injective (one-to-one): no two domain elements map to the same value
    # surjective (onto):      every codomain element is hit by some mapping
    # bijective:              both injective and surjective
    # time complexity O(N), space O(N)
    def is_injective(self,mapping:dict)->bool:
        values = list(mapping.values())
        return len(values) == len(set(values))

    def is_surjective(self,mapping:dict,codomain:set)->bool:
        return set(mapping.values()) == codomain

    def is_bijective(self,mapping:dict,codomain:set)->bool:
        return self.is_injective(mapping) and self.is_surjective(mapping, codomain)

mapping = {1: 'a', 2: 'b', 3: 'c'}
codomain = {'a', 'b', 'c'}
fp = functions_properties()
result = fp.is_bijective(mapping, codomain)
print(result)
