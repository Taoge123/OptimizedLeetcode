

"""
https://www.youtube.com/watch?v=40plVtFcUSI
https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/

"""

from functools import lru_cache


class Solution:
    def minimumMoves(self, nums):
        return self.dp(tuple(nums), 0, len(nums) - 1)

    @lru_cache(None)
    def dp(self, nums, i, j):
        if i > j:
            return 0
        res = self.dp(nums, i, j - 1) + 1
        if nums[j] == nums[j - 1]:
            res = min(res, self.dp(nums, i, j - 2) + 1)
        for k in range(i, j - 1):
            if nums[j] == nums[k]:
                res = min(res, self.dp(nums, i, k - 1) + self.dp(nums, k + 1, j - 1))
        return res


class Solution2:
    def minimumMoves(self, arr) -> int:

        n = len(arr)
        dp = [[0 for x in range(n + 1)] for y in range(n + 1)]

        # loop for substring length
        # we are considering
        for l in range(1, n + 1):

            # loop with two variables i and j, denoting
            # starting and ending of substrings
            i = 0
            j = l - 1
            while j < n:
                # If substring length is 1, then 1 step will be needed
                if (l == 1):
                    dp[i][j] = 1
                else:
                    # delete the ith char individually and assign result for subproblem (i+1,j)
                    dp[i][j] = 1 + dp[i + 1][j]

                    # if current and next char are same, choose min from current and subproblem (i+2,j)
                    if (arr[i] == arr[i + 1]):
                        dp[i][j] = min(1 + dp[i + 2][j], dp[i][j])

                    ''' loop over all right characters and suppose Kth char is same as ith character then 
                        choose minimum from current and two substring after ignoring ith and Kth char '''
                    for K in range(i + 2, j + 1):
                        if (arr[i] == arr[K]):
                            dp[i][j] = min(dp[i + 1][K - 1] + dp[K + 1][j], dp[i][j])

                i += 1
                j += 1

        return dp[0][n - 1]


class SolutionERROR:
    def minimumMoves(self, arr):
        dp = [[1 for _ in range(len(arr))] for _ in range(len(arr))]

        for i in range(len(arr) - 1, -1, -1):
            for j in range(i + 1, len(arr)):
                dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else min(dp[i][k] + dp[k + 1][j] for k in range(i, j))

        return dp[0][-1] - 1


