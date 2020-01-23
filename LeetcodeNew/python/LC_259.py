"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?

"""


class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:

        res = 0
        nums = sorted(nums)

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
        return res


nums = [1,1,1,1]
target = 4
a = Solution()
print(a.threeSumSmaller(nums, target))
