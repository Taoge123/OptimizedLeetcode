
import collections

class Solution:
    def largestOverlap(self, A, B) -> int:
        n = len(A)
        p1, p2 = [], []

        for i in range(n * n):
            if A[i // n][i % n] == 1:
                p1.append([i // n, i % n])
            if B[i // n][i % n] == 1:
                p2.append([i // n, i % n])

        table = collections.defaultdict(int)
        res = 0
        for a in p1:
            for b in p2:
                diff = tuple([(a[0] - b[0]), (a[1] - b[1])])
                table[diff] += 1
                res = max(res, table[diff])
        return res

