


"""
For each index i, run search starting from i left and right up to d steps.
This way, we can easily detect if arr[j] is blocking further jumps.

So, we stop the search when we encounter j where arr[i] <= arr[j].

To prevent re-computations, we need to memoise max jumps for every index in dp.

"""
class Solution:
    def maxJumps(self, arr, d: int) -> int:
        n = len(arr)
        dp = [0 for _ in range(n)]
        res = 1
        for i in range(n):
            res = max(res, self.dfs(arr, n, d, i, dp))
        return res

    def dfs(self, arr, n, d, i, dp):
        if dp[i]:
            return dp[i]
        res = 1
        for j in range( i +1, min( i +d, n- 1) + 1):
            if arr[i] <= arr[j]:
                break
            res = max(res, self.dfs(arr, n, d, j, dp) + 1)

        for j in range(i - 1, max(i - d, 0) - 1, -1):
            if arr[i] <= arr[j]:
                break
            res = max(res, self.dfs(arr, n, d, j, dp) + 1)

        dp[i] = res
        return dp[i]




class Solution2:
    def maxJumps(self, arr, d: int) -> int:
        dp = [1 for _ in range(len(arr))]
        nums = [[num, i] for i, num in enumerate(arr)]
        nums = sorted(nums)

        for _, i in nums:
            for j in range(i + 1, i + d + 1):
                if j < 0 or j >= len(arr) or arr[i] <= arr[j]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)

            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or j >= len(arr) or arr[i] <= arr[j]:
                    break
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


