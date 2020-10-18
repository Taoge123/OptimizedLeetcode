
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


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0
        for m in range(1, int(math.sqrt(2 * N)) + 1):
            if (2 * N - m * m + m) % (2 * m) == 0:
                res += 1
        return res




