import math


class Solution:
    def numOfWays(self, nums) -> int:
        def ways(nums):
            if len(nums) <= 2:
                return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return math.comb(len(left) + len(right), len(left)) * ways(left) * ways(right)

        return (ways(nums) - 1) % (10 ** 9 + 7)




class Solution11:
    def numOfWays(self, nums) -> int:
        n = len(nums)
        memo = [[-1 for _ in range(n)] for _ in range(n)]

        def combine(x, y):
            if x == 0 or y == 0: return 1
            if memo[x][y] != -1: return memo[x][y]
            memo[x][y] = combine(x, y - 1) + combine(x - 1, y)
            return memo[x][y]

        def compute(nums):
            if len(nums) <= 2:
                return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return combine(len(left), len(right)) * compute(left) * compute(right)

        return (compute(nums) - 1) % (10 ** 9 + 7)





