"""
连续k的最大和
"""
"""
 1 2 3 4 5 6 1
 1 2 3
 1 1 2
 6 1 1 
 5 6 1 
"""

import functools


class SolutionSlidingWindow:
    def maxScore(self, cardPoints, k: int) -> int:

        n = len(cardPoints)
        windowSize = n - k  # 窗口的大小
        summ = 0
        res = float("inf")  # 正无穷大
        for i in range(n):
            summ += cardPoints[i]
            if i >= windowSize:
                summ -= cardPoints[i - windowSize]
            if i >= windowSize - 1:
                res = min(res, summ)
        return sum(cardPoints) - res


class SolutionTonyMemo:
    def maxScore(self, nums, k: int) -> int:
        n = len(nums)
        if k >= n:
            return sum(nums)
        @functools.lru_cache(None)
        def dfs(i, j, k):
            if k <= 0:
                return 0
            if i > j:
                return 0
            if i == j:
                return nums[i]

            pick_left = dfs(i + 1, j, k - 1) + nums[i]
            pick_right = dfs(i, j - 1, k - 1) + nums[j]

            return max(pick_left, pick_right)

        return dfs(0, n - 1, k)


class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        # presum
        # O(k)
        n = len(cardPoints)
        i = k - 1
        cur = sum(cardPoints[:k])
        res = cur

        for j in range(k):
            cur -= cardPoints[i - j]
            cur += cardPoints[n - 1 - j]
            res = max(cur, res)
        return res



class SolutionSame:
    def maxScore(self, nums, k: int) -> int:
        res = cur = sum(nums[:k])
        for i in range(k):
            print(k - i - 1, -i - 1)
            cur -= nums[k - i - 1]
            cur += nums[-i - 1]
            res = max(res, cur)

        return res

cardPoints = [1,2,3,4,5,6,1]
k = 3
a = Solution()
print(a.maxScore(cardPoints, k))

