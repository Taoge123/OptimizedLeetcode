
class Solution:
    def maxTurbulenceSize(self, A) -> int:
        res = cur = 0

        for i in range(len(A)):
            if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                cur += 1
            elif i >= 1 and A[i - 1] != A[i]:
                cur = 2
            else:
                cur = 1
            res = max(res, cur)
        return res





