
class Solution:
    def longestOnes(self, A, K: int) -> int:
        i = 0
        count = 0
        res = 0
        for j in range(len(A)):
            if A[j] == 1:
                res = max(res, j - i + 1)
            else:
                count += 1
                while count > K:
                    if A[i] == 0:
                        count -= 1
                    i += 1
                res = max(res, j - i + 1)

        return res


