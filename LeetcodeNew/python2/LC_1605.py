"""
X X X  a
X X X  b
X X X  c

x y z
res[0][0] = min(x, a)
res[0][1] = min(y, a - res[0][0])
res[0][2] = a - res[0][0] = min(z, a - res[0][0] - res[0][2])

x+y+z = a+b+c -> a<=x+y+z

x+y+z-a = b+c
x'+y'+z' = b+c -> b+c -> b <- x'+y'+z'

"""

class Solution:
    def restoreMatrix(self, rowSum, colSum):
        m, n = len(rowSum), len(colSum)
        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                val = min(rowSum[i], colSum[j])
                res[i][j] = val
                rowSum[i] -= val
                colSum[j] -= val
        return res

