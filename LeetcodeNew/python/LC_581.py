
"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        sorts = sorted(nums)

        if nums == sorts:
            return 0

        left = min(i for i in range(n) if nums[i] != sorts[i])
        right = max(i for i in range(n) if nums[i] != sorts[i])

        return right - left + 1



class Solution2:
    def findUnsortedSubarray(self, nums) -> int:
        n = len(nums)
        start, end = -1, -2
        mini = nums[n - 1]
        maxi = nums[0]

        for i in range(1, n):
            maxi = max(maxi, nums[i])
            mini = min(mini, nums[n - 1 - i])

            if nums[i] < maxi:
                end = i
            if nums[n - 1 - i] > mini:
                start = n - 1 - i

        return end - start + 1





