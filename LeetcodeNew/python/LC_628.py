"""
628.Maximum-Product-of-Three-Numbers
1. all positive
2. only one negative
3. at least two negative

所有元素大于0： | X... X X X 肯定取最大的三个正数。即 nums[N-3]*nums[N-2]*nums[N-1]

仅有一个元素小于0： X | X... X X X 单个负数无法使用，依然只能取最大的三个正数。即 nums[N-3]*nums[N-2]*nums[N-1]

至少两个元素小于0： X X | ... X X X
尝试取绝对值最大的两个负数组合成一个较大的正数？（不可能取更多或者其他的负数） max { nums[N-3]*nums[N-2]*nums[N-1], nums[0]*nums[1]*nums[N-1]}

仅有一个元素大于0： X X ... X X | X 仅能取最小的两个负数和一个正数。即 nums[0]*nums[1]*nums[N-1]

所有元素小于0： X X ... X X | 仅能取最小的两个负数和最大的一个负数。即 nums[0]*nums[1]*nums[N-1]

所以我们发现规律，答案总是从 nums[N-3]*nums[N-2]*nums[N-1], nums[0]*nums[1]*nums[N-1] 这两个值中间取。

"""


class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[0] * nums[1] * nums[n - 1], nums[n - 1] * nums[n - 2] * nums[n - 3])


# class SolutionTest:
#     def maximumProduct(self, nums) -> int:
#         n = len(nums)
#         def dfs(i, k):
#             if i >= n and k <= 0:
#                 return 1
#             if i >= n or k <= 0:
#                 return -10 ** 10
#
#             pick = dfs(i+1, k-1) * nums[i]
#             no_pick = dfs(i+1, k)
#             return max(pick, no_pick)
#         return dfs(0, 3)

nums = [-1,-2,-3]
a = SolutionTest()
print(a.maximumProduct(nums))
