
"""
https://leetcode.com/problems/house-robber-ii/discuss/164055/Python-or-tm


You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
"""
213. House Robber II
> 类型：DP基础题
> Time Complexity O(N)
> Space Complexity O(1)
这道题相对于House Robber I里面要解决的edge就是circle的头和尾不能为邻居，那我们只需要在之前写好的代码基础上计算两个区间即可，
第一个区间是nums[1:]， 第二个区间是nums[:-1]，在比较这两个区间哪个大即可。
如上面的例图，对于[3, 10, 7]这个数组，其实我们要做的就将其分成两个数组:
数组1: [3, 10] ,也就是 nums[:-1]
数组2: [10, 7], 也就是nums[1:]
然后用求出这两个区间中的最大值即可。
"""


class Solution1:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * len(nums)
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])

        return res[-1]


"""
滚动数组优化
什么是滚动数组：
https://leetcode.com/problems/house-robber/discuss/164056/Python-or-tm
"""
class Solution2:
    def rob(self, nums):
        if not nums: return 0
        if len(nums) <= 2: return max(nums)
        return max(self.rob_row(nums[1:]), self.rob_row(nums[:-1]))

    def rob_row(self, nums):
        res = [0] * 2
        res[0], res[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i % 2] = max(res[(i - 1) % 2], res[(i - 2) % 2] + nums[i])

        return max(res[0], res[1])


class Solution3:
    def rob(self, nums):

        n = len(nums)
        if n == 0: return 0
        if n < 4: return max(nums)

        first, second = 0, 0
        for i in nums[:-1]: first, second = second, max(first + i, second)
        result = second

        first, second = 0, 0
        for i in nums[1:]: first, second = second, max(first + i, second)
        return max(result, second)


"""
A little bit different solution:
If nums is [1,2,3,4]
we can rob nums*2, witch is [1,2,3,4,1,2,3,4] then minus result of [1,2,3,4]
"""
class Solution4:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]
        m_low = m_high = 0
        for n in nums:            # first round
            m_high, m_low = max(m_low + n, m_high), m_high
        first_round = m_high

        for n in nums:            # second round
            m_high, m_low = max(m_low + n, m_high), m_high
        return m_high - first_round


class Solution5:
    def rob(self, nums):

        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        nums_1=nums[1:]
        nums_2=nums[:-1]
        def dp(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        return max(dp(nums_1),dp(nums_2))



