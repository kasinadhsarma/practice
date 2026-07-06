class linear_independence:
    def check(self,vectors:list)->bool:
        rows = len(vectors)
        cols = len(vectors[0])
        work = [[float(value) for value in vector] for vector in vectors]

        rank_count = 0
        for col in range(cols):
            if rank_count >= rows:
                break
            # find a row below rank_count with a non-zero entry in this column
            pivot_row = None
            for r in range(rank_count, rows):
                if abs(work[r][col]) > 1e-9:
                    pivot_row = r
                    break
            if pivot_row is None:
                continue
            work[rank_count], work[pivot_row] = work[pivot_row], work[rank_count]
            for r in range(rank_count + 1, rows):
                factor = work[r][col] / work[rank_count][col]
                for c in range(col, cols):
                    work[r][c] -= factor * work[rank_count][c]
            rank_count += 1
        # vectors are independent only if every row survives elimination
        return rank_count == rows

vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
result = linear_independence().check(vectors)
print(result)
