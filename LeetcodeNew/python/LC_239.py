"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

"""

import collections

class Solution:
    def maxSlidingWindow(self, nums, k):

        queue = collections.deque([])
        res = []

        for i in range(len(nums)):
            # checking front
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            # checking back
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if queue and i >= k - 1:
                res.append(nums[queue[0]])

        return res


