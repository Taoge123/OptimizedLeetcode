
"""
x + x+1 + x+2 + x+3 .. x+m-1 = N
(x+x+m-1)*m / 2   =  N  {x, m}

2x = 2N/m - m/2 + 1/2 = 2N-m^2+m / 2m

x = 2N-m^2+m / 2m


求和公式:
kx + (k-1) * k // 2 = N

kx = N - (k-1) * k // 2

N - (k-1) * k // 2 > 0

k < sqrt(2N)


"""

import math
import functools

class SolutionTony:
    def consecutiveNumbersSum(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, step):
            if i == n:
                return True
            if i >= n:
                return False
            return dfs(i + step, step + 1)

        res = 0
        for i in range(1, n + 1):
            if dfs(i, i + 1):
                res += 1
        return res


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        for m in range(1, int(math.sqrt(2 * N)) + 1):
            if (2 * N - m * m + m) % (2 * m) == 0:
                res += 1
        return res



n = 9
a = SolutionTest()
print(a.consecutiveNumbersSum(n))
