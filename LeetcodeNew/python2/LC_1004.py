"""
dp[i][k]: A[0:i], using k previligies, the length of the longest (contiguous) subarray that contains onlu 1s

A[i] == 1, dp[i][k] = dp[i-1][k] + 1
A[i] == 0, dp[i][k] = dp[i-1][k-1] + 1

X X X X X 1

X [i X X j] 0 X X

X 1 [X X j] 0 X X

X [i X X j] 0 X X

Translation:
Find the longest subarray with at most K zeros.


"""


class SolutionTony:
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



class Solution:
    def longestOnes(self, A, K):
        res = 0
        i = 0
        for j in range(len(A)):
            K -= A[j] == 0
            if K < 0:
                K += A[i] == 0
                i += 1
            res = j - i + 1
        return res


