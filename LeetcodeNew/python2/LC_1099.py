class Solution:
    def twoSumLessThanK(self, A, K: int) -> int:
        i, j = 0, len(A) - 1
        A = sorted(A)
        res = -1
        while i < j:
            if A[i] + A[j] < K:
                res = max(res, A[i] + A[j])
                i += 1
            else:
                j -= 1

        return res




