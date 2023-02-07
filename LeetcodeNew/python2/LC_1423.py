"""
连续k的最大和
"""
"""
    xxxxxxxxxxxx
    yyyyy
    yyyy       y
    yyy       yy
    yy       yyy
    y       yyyy
           yyyyy

"""



import functools

class SolutionTonySLiding:
    def maxScore(self, nums, k: int) -> int:
        n = len(nums)
        summ = sum(nums[:k])
        res = summ
        for i in range(k):
            # each time, remove element from right and add from left
            summ -= nums[k-1-i]
            summ += nums[n-i-1]
            res = max(res, summ)
        return res


# 两边最大就是中间最小
class SolutionRika:
    def maxScore(self, cardPoints, k: int) -> int:
        # take k cards from left side and right side, return max score
        # dp --> O(nk) --> TLE
        # use sliding window to get min subarray summ, size = n - k
        n = len(cardPoints)
        size = n - k
        l = 0
        summ = 0
        minn = float('inf')
        for r in range(n):
            summ += cardPoints[r]
            if r - l + 1 > size:
                summ -= cardPoints[l]
                l += 1
            if r - l + 1 == size:
                minn = min(minn, summ)

        return sum(cardPoints) - minn


class SolutionTonyMemo:
    def maxScore(self, nums, k: int) -> int:
        n = len(nums)
        if k >= n:
            return sum(nums)
        @functools.lru_cache(None)
        def dfs(i, j, k):
            if k <= 0:
                return 0

            pick_left = dfs(i + 1, j, k - 1) + nums[i]
            pick_right = dfs(i, j - 1, k - 1) + nums[j]

            return max(pick_left, pick_right)

        return dfs(0, n - 1, k)



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

