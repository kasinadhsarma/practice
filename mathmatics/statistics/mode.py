class mode:
    # most frequently occurring value(s); returns every value tied for the max count
    # time complexity O(N), space O(N)
    def calculate(self,data:list)->list:
        if not data:
            return []
        counts = {}
        for value in data:
            counts[value] = counts.get(value, 0) + 1
        highest = max(counts.values())
        return [value for value, count in counts.items() if count == highest]

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5, 8]
result = mode().calculate(data)
print(result)
