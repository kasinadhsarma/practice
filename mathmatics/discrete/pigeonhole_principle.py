import math

class pigeonhole_principle:
    # if N items are placed into M containers, at least one container must
    # hold at least ceil(N / M) items — you cannot spread items out evenly
    # enough to avoid it once N > M
    # time complexity O(1), space O(1)
    def guaranteed_minimum(self,items:int,containers:int)->int:
        if containers <= 0:
            return None
        return math.ceil(items / containers)

items = 13     # 13 people
containers = 12  # 12 months
result = pigeonhole_principle().guaranteed_minimum(items, containers)
print(result)  # at least 2 people must share a birth month
