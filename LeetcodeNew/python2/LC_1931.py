
import functools

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
                neighbors.add(lastRowList[ j -1]) # check above nrighbor

            for color in (0, 1, 2):
                if color not in neighbors:
                    newRow = lastRowList
                    newRow[j] = color
                    res += dfs(pos + 1, tuple(newRow))
            return res % mod

        return dfs(0, tuple([0 ] *m))




