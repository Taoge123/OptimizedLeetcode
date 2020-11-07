import copy

class Solution:
    def minDeletionSize(self, A):
        m, n, res = len(A), len(A[0]), 0
        compare = [True] * m

        for j in range(n):
            new_compare = copy.copy(compare)
            for i in range(1, m):
                if compare[i]:
                    if A[i][j] < A[i - 1][j]:
                        res += 1
                        compare = new_compare
                        break

                    elif A[i][j] > A[i - 1][j]:
                        compare[i] = False

        return res




