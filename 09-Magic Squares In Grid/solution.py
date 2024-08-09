class Solution:
    def numMagicSquaresInside(self, grid):
        res = 0
        rows = len(grid)
        cols = len(grid[0]) if grid else 0

        if rows < 3 or cols < 3:
            return res

        for r in range(rows - 2):
            for c in range(cols - 2):
                subgrid = [grid[r + i][c : c + 3] for i in range(3)]
                if self.isMagic(subgrid):
                    res += 1

        return res

    def isMagic(self, square):
        flat_square = [num for row in square for num in row]
        if sorted(flat_square) != list(range(1, 10)):
            return False

        magic_sum = sum(square[0])

        for row in square:
            if sum(row) != magic_sum:
                return False

        for col in range(3):
            if sum(square[row][col] for row in range(3)) != magic_sum:
                return False

        if (
            sum(square[i][i] for i in range(3)) != magic_sum
            or sum(square[i][2 - i] for i in range(3)) != magic_sum
        ):
            return False

        return True
