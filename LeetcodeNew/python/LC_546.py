
"""
best
https://leetcode.com/problems/remove-boxes/discuss/1402561/C%2B%2BJavaPython-Top-down-DP-Clear-explanation-with-Picture-Clean-and-Concise

https://leetcode.com/problems/remove-boxes/discuss/1402468/Python-5-lines-dp-O(n4)-solution-explained-in-details
https://leetcode.com/problems/remove-boxes/discuss/101311/Python-Fast-DP-with-Explanation
pass
https://leetcode.com/problems/remove-boxes/discuss/101312/Memoization-DFS-C%2B%2B

XXXXOOOOXXXX
l       r
    i   
"""

import functools

class SolutionTD:
    def removeBoxes(self, boxes) -> int:
        @functools.lru_cache(None)
        def dfs(i, j, k):
            if i > j:
                return 0
            while i + 1 <= j and boxes[i] == boxes[i + 1]:  # Increase both `i` and `k` if they have consecutive colors with `boxes[i]`
                i += 1
                k += 1
            res = (k + 1) * (k + 1) + dfs(i + 1, j, 0)  # Remove all boxes which has the same with `boxes[i]`
            for mid in range(i + 1, j + 1):  # Try to merge non-contiguous boxes of the same color together
                if boxes[i] == boxes[mid]:
                    res = max(res, dfs(i + 1, mid - 1, 0) + dfs(mid, j, k + 1))
            return res

        return dfs(0, len(boxes) - 1, 0)


"""

(i, j, k)

2 2 2 2 (3 1 3 | 2 2 5)
      i          m    j
      k

option 1 : value + dfs(i+1, j, 0)
option 2 : dfs(i+1, m-1, 0) + dfs(m, j, i+1) 


2 2 2 2
greedy
(a + b) ** 2 >  a ** 2 + b ** 2


"""


class SolutionTony:
    def removeBoxes(self, nums) -> int:
        memo = {}
        return self.dfs(nums, 0, len(nums) - 1, 0, memo)

    def dfs(self, nums, i, j, k, memo):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        if i > j:
            return 0
        while i < j and nums[i] == nums[i + 1]:
            i += 1
            k += 1
        # option 1
        res = (k + 1) ** 2 + self.dfs(nums, i + 1, j, 0, memo)

        # option 2
        for m in range(i + 1, j + 1):
            if nums[i] == nums[m]:
                res = max(res, self.dfs(nums, i + 1, m - 1, 0, memo) + self.dfs(nums, m, j, k + 1, memo))
        memo[(i, j, k)] = res
        return res


class Solution:
    def removeBoxes(self, B):
        @functools.lru_cache(None)
        def dp(i, j, k):
            if i > j:
                return 0
            # This is for optimization
            while i + 1 <= j and B[i] == B[
                i + 1]:  # Increase both `l` and `k` if they have consecutive colors with `boxes[l]`
                i += 1
                k += 1
            res = (k + 1) ** 2 + dp(i + 1, j, 0)
            for m in range(i + 1, j + 1):
                if B[i] == B[m]:
                    res = max(res, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
            return res

        return dp(0, len(B) - 1, 0)




class Solution2:
    def removeBoxes(self, boxes):
        n = len(boxes)
        self.boxes = boxes
        self.dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        return self.search(0, n - 1, 0)

    def search(self, l, r, k):
        if l > r:
            return 0

        if self.dp[l][r][k]:
            return self.dp[l][r][k]

        while l < r and self.boxes[r] == self.boxes[r - 1]:
            r -= 1
            k += 1

        # Case 1
        self.dp[l][r][k] = self.search(l, r - 1, 0) + (k + 1) * (k + 1)
        # Case 2
        for i in range(l, r):
            if self.boxes[i] == self.boxes[r]:
                self.dp[l][r][k] = max(self.dp[l][r][k], self.search(l, i, k + 1) + self.search(i + 1, r - 1, 0))

        return self.dp[l][r][k]



nums = [2,2,2,3,1,3,2,2,5]
a = SolutionTD()
print(a.removeBoxes(nums))


