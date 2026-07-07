class quartiles_iqr:
    # Q1/Q2/Q3 split sorted data into quarters; IQR = Q3 - Q1 measures the
    # spread of the middle 50% (robust to outliers, unlike range/variance)
    # time complexity O(N log N) for the sort, space O(N)
    def _median(self,values:list)->float:
        n = len(values)
        mid = n // 2
        if n % 2 == 1:
            return values[mid]
        return (values[mid - 1] + values[mid]) / 2

    def calculate(self,data:list)->dict:
        if not data:
            return None
        ordered = sorted(data)
        n = len(ordered)
        if n == 1:
            return {"Q1": ordered[0], "Q2": ordered[0], "Q3": ordered[0], "IQR": 0}
        mid = n // 2
        lower_half = ordered[:mid]
        upper_half = ordered[mid + 1:] if n % 2 == 1 else ordered[mid:]

        q1 = self._median(lower_half)
        q2 = self._median(ordered)
        q3 = self._median(upper_half)
        return {"Q1": q1, "Q2": q2, "Q3": q3, "IQR": q3 - q1}

data = [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]
result = quartiles_iqr().calculate(data)
print(result)
