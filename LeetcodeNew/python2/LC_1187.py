"""
https://leetcode.com/problems/make-array-strictly-increasing/discuss/377816/Python-DFS%2BMemo-with-explanation
https://leetcode.com/problems/make-array-strictly-increasing/discuss/1389044/Simple-python-solution-using-SortedList.
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1187.Make-Array-Strictly-Increasing

dp[i][k] : arr1[1:i] using k operations to make them strictly increasing,
            the minimum value of arr[i]

dp[i-1][k] < arr1[i] => dp[i][k] = arr1[i]
dp[i-1][k-1] < replace(arr1[i]) => dp[i][k] = replace(arr1[i])
"""

import functools
import collections
import bisect


class SolutionTony:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        arr2 = sorted(set(arr2))
        @functools.lru_cache(None)
        def dfs(i, prev):
            if i >= len(arr1):
                return 0

            j = bisect.bisect_right(arr2, prev)

            swap = dfs(i + 1, arr2[j]) + 1 if j < len(arr2) else float('inf')
            noswap = dfs(i + 1, arr1[i]) if arr1[i] > prev else float('inf')

            return min(swap, noswap)

        res = dfs(0, float('-inf'))
        return res if res != float('inf') else -1



class SolutionTony2:
    def makeArrayIncreasing(self, A, B):
        n = len(A)
        B = sorted(set(B))
        m = len(B)

        @functools.lru_cache(None)
        def dfs(i, prev):
            if i == n:
                return 0

            j = bisect.bisect_right(B, prev)

            swap = 1 + dfs(i + 1, B[j]) if j < m else float('inf')
            no_swap = dfs(i + 1, A[i]) if prev < A[i] else float('inf')

            return min(no_swap, swap)

        res = dfs(0, -float('inf'))
        return -1 if res == float('inf') else res



class Solution22:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        nums = sorted(set(arr2))

        @functools.lru_cache(None)
        def min_changes(i, cur_min):
            if i >= len(arr1):
                return 0

            j = bisect.bisect_right(nums, cur_min)
            swap_cost = 1 + min_changes(i + 1, nums[j]) if j < len(nums) else float("+inf")
            keep_cost = min_changes(i + 1, arr1[i]) if arr1[i] > cur_min else float("+inf")

            return min(swap_cost, keep_cost)

        changes = min_changes(0, float("-inf"))
        return changes if changes != float("inf") else -1



class SolutionTony:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        n = len(arr1)
        if n == 1:
            return 0
        dp = [[float('inf') for i in range(n + 1)] for j in range(n + 1)]
        arr2.sort()

        dp[0][0] = float('-inf')
        for i in range(1, n + 1):
            for k in range(i + 1):
                if arr1[i - 1] > dp[i - 1][k]:
                    dp[i][k] = arr1[i - 1]
                if k > 0:
                    idx = bisect.bisect_right(arr2, dp[i - 1][k - 1])
                    if idx < len(arr2):
                        dp[i][k] = min(dp[i][k], arr2[idx])

                    if i == n and dp[i][k] != float('inf'):
                        return k
        return -1


class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        dp = {-1: 0}
        arr2 = sorted(arr2)
        for num in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if num > key:
                    tmp[num] = min(tmp[num], dp[key])
                replace = bisect.bisect_right(arr2, key)
                if replace < len(arr2):
                    tmp[arr2[replace]] = min(tmp[arr2[replace]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1


class Solution2:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        arr2 = sorted(set(arr2))
        changes = self.dfs(tuple(arr1), tuple(arr2), 0, float('-inf'))
        return changes if changes != float('inf') else -1

    @lru_cache(None)
    def dfs(self, arr1, arr2, i, prev):
        if i >= len(arr1):
            return 0
        j = bisect.bisect_right(arr2, prev)
        swap = 1 + self.dfs(arr1, arr2, i + 1, arr2[j]) if j < len(arr2) else float('inf')
        noswap = self.dfs(arr1, arr2, i + 1, arr1[i]) if arr1[i] > prev else float('inf')
        return min(swap, noswap)





a = Solution2()
arr1 = [1,5,3,6,7]
arr2 = [1,3,2,4]
a.makeArrayIncreasing(arr1, arr2)

