class median:
    # middle value of sorted data; average of the two middles when N is even
    # time complexity O(N log N) for the sort, space O(N)
    def calculate(self,data:list)->float:
        if not data:
            return None
        ordered = sorted(data)
        n = len(ordered)
        mid = n // 2
        if n % 2 == 1:
            return ordered[mid]
        return (ordered[mid - 1] + ordered[mid]) / 2

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = median().calculate(data)
print(result)
