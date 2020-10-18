"""
0 0 1 1
1 0 1 0
1 1 0 0
-----------
1 1 1 1
1 0 0 1
1 1 1 1


Assume A is M * N.

A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.
A[i][j] is worth 1 << (N - 1 - j)
For every col, I count the current number of 1s.
After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
if M - cur > cur, we can toggle this column to get more 1s.
max(cur, M - cur) will be the maximum number of 1s that we can get.

"""


class Solution:
    def matrixScore(self, A) -> int:
        m, n = len(A), len(A[0])
        res = (1 << (n - 1)) * m

        for j in range(1, n):
            cur = 0
            for i in range(m):
                if A[i][j] == A[i][0]:
                    cur += 1
            res += max(cur, m - cur) * (1 << (n - j - 1))

        return res

