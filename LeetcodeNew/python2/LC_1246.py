

"""
https://www.youtube.com/watch?v=40plVtFcUSI
https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/
https://leetcode.com/problems/palindrome-removal/discuss/555111/Python%3A-DFS-%2B-Memo-but-TLE
https://leetcode.com/problems/palindrome-removal/discuss/745169/10-line-python-solution
"""

import functools


class Solution00:
    def minimumMoves(self, arr) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            res = 1 + dp(i + 1, j)
            for k in range(i + 1, j + 1):
                if arr[i] == arr[k]:
                    res = min(res, max(1, dp(i + 1, k - 1)) + dp(k + 1, j))
            return res

        return dp(0, len(arr) - 1)


class Solution01:
    def minimumMoves(self, A):

        @functools.lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 1
            if A[i] == A[j]:
                return dfs(i + 1, j - 1)
            else:
                res = float('inf')
                for k in range(i, j):
                    res = min(res, dfs(i, k) + dfs(k + 1, j))
                return res

        return dfs(0, len(A) - 1)


class SolutionDFS:
    def minimumMoves(self, arr) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        res = 1 + self.dfs(arr, i + 1, j, memo)

        for k in range(i + 1, j + 1):
            if arr[i] == arr[k]:
                res = min(res, max(1, self.dfs(arr, i + 1, k - 1, memo)) + self.dfs(arr, k + 1, j, memo))
        memo[(i, j)] = res
        return memo[(i, j)]



class SolutionLee:
    def minimumMoves(self, nums):
        return self.dp(tuple(nums), 0, len(nums) - 1)

    @functools.lru_cache(None)
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



class SolutionTony1:
    def minimumMoves(self, arr):
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, nums, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return 0

        res = self.dfs(nums, i, j - 1, memo) + 1

        if nums[j] == nums[j - 1]:
            res = min(res, self.dfs(nums, i, j - 2, memo) + 1)

        for k in range(i, j - 1):
            if nums[j] == nums[k]:
                res = min(res, self.dfs(nums, i, k - 1, memo) + self.dfs(nums, k + 1, j - 1, memo))

        memo[(i, j)] = res
        return memo[(i, j)]




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



class SolutionTest:
    def minimumMoves(self, arr) -> int:
        memo = {}
        return self.dfs(arr, 0, len(arr) - 1, memo)

    def dfs(self, arr, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0

        res = 1 + self.dfs(arr, i + 1, j, memo)
        for k in range(i + 1, j + 1):
            if arr[i] == arr[k]:
                left = self.dfs(arr, i + 1, k - 1, memo)
                right = self.dfs(arr, k + 1, j, memo)
                res = min(res, max(1, left) + right)
        memo[(i, j)] = res
        return memo[(i, j)]


nums = [1,4,4,1]
a = SolutionTest()
print(a.minimumMoves(nums))


