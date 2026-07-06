class rank:
    def calculate(self,matrix:list)->int:
        # work on a copy of floats so the original matrix is untouched
        rows = len(matrix)
        cols = len(matrix[0])
        work = [[float(value) for value in row] for row in matrix]

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
            # move the pivot row into place
            work[rank_count], work[pivot_row] = work[pivot_row], work[rank_count]
            # eliminate this column from every row below the pivot
            for r in range(rank_count + 1, rows):
                factor = work[r][col] / work[rank_count][col]
                for c in range(col, cols):
                    work[r][c] -= factor * work[rank_count][c]
            rank_count += 1
        return rank_count

matrix = [[1, 2, 3], [2, 4, 6], [1, 0, 1]]
result = rank().calculate(matrix)
print(result)
