class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        res = []

        dirR, dirC = 0, 1
        moves, nextMoves = 1, 2
        twice = 2

        while len(res) < rows * cols:
            if 0 <= rStart < rows and 0 <= cStart < cols:
                res.append([rStart, cStart])
            
            rStart += dirR
            cStart += dirC

            moves -= 1
            if moves == 0:
                dirR, dirC = dirC, -dirR
                
                twice -= 1
                if twice == 0:
                    twice = 2
                    moves = nextMoves
                    nextMoves += 1
                else:
                    moves = nextMoves - 1

        return res