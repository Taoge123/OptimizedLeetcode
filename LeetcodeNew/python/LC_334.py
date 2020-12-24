
"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""


class SolutionLIC:
    def increasingTriplet(self, nums):

        n = len(nums)
        leftMin = [0] * n
        rightMax = [0] * n

        leftMin[0] = float('inf')

        for i in range(1, n):
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])

        rightMax[-1] = float('-inf')
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], nums[i + 1])

        for i in range(n):
            if leftMin[i] < nums[i] and rightMax[i] > nums[i]:
                return True

        return False



class Solution:
    def increasingTriplet(self, nums):

        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False



nums = [1,2,3,4,5]
a = Solution()
print(a.increasingTriplet(nums))


