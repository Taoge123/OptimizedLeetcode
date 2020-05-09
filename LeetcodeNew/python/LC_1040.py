
"""
https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/289357/c%2B%2B-with-picture

一步到位
rightmost - leftmost == n - 1

min
1 2 4 5 10
1 2 3 4 5 - one step

1 2 3 4 10 - cant move 10 because its the edge. you cant move the edge
2 3 4 6 10 - 1 move to 6 and move 10 to 5



max

"""

class Solution:
    def numMovesStonesII(self, stones):
        nums = sorted(stones)
        n = len(nums)
        low = n
        i = 0
        for j in range(n):
            while nums[j] - nums[i] + 1 > n:
                i += 1

            already = j - i + 1
            if already == n - 1 and nums[j] - nums[i] + 1 == n - 1:
                low = min(low, 2)
            else:
                low = min(low, n - already)

        high = max(nums[n - 1] - nums[1] - n + 2, nums[n - 2] - nums[0] - n + 2)
        return [low, high]





