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


class Solution:
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

