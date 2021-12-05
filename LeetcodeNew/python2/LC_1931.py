
import functools


class SolutionTonyRika:
    def colorTheGrid(self, m: int, n: int) -> int:
        def valid(row, col, state):
            up = 1 << (m - 1)
            if col == 0 and row == 0:
                return True

            if col > 0 and state & 1:  # has neighbor
                return False

            if row > 0 and state & up:  # has neighbor
                return False
            return True

        mod = 10 ** 9 + 7
        fullmask = (1 << m) - 1

        @functools.lru_cache(None)
        def dfs(pos, red, yellow, green):
            if pos == m * n:
                return 1

            row, col = pos // m, pos % m

            nxt_red = (red << 1) & fullmask
            nxt_yellow = (yellow << 1) & fullmask
            nxt_green = (green << 1) & fullmask

            res = 0
            if valid(row, col, red):
                res += dfs(pos + 1, nxt_red + 1, nxt_yellow, nxt_green)
            if valid(row, col, yellow):
                res += dfs(pos + 1, nxt_red, nxt_yellow + 1, nxt_green)
            if valid(row, col, green):
                res += dfs(pos + 1, nxt_red, nxt_yellow, nxt_green + 1)

            return res % mod

        # n *= 3
        return dfs(0, 0, 0, 0) % mod



class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        mod = 10 ** 9 + 7
        @functools.lru_cache(None)
        def dfs(pos, lastRow):
            if pos >= m * n:
                return 1

            i, j = pos // m, pos % m

            lastRowList = list(lastRow)
            res = 0

            neighbors = set()
            if i > 0:
                neighbors.add(lastRowList[j]) # check above nrighbor

            if j > 0:
                neighbors.add(lastRowList[j-1]) # check above nrighbor

            for color in (0, 1, 2):
                if color not in neighbors:
                    newRow = lastRowList
                    newRow[j] = color
                    res += dfs(pos + 1, tuple(newRow))
            return res % mod

        return dfs(0, tuple([0 ] *m))




