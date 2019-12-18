"""

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""

import heapq

class Solution:
    def findKthLargest(self, nums, k):

        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, left, right, k):

        pos = self.partition(nums, left, right)

        if pos == k - 1:
            return nums[pos]

        elif pos < k - 1:
            return self.quickSelect(nums, pos + 1, right, k)

        return self.quickSelect(nums, left, pos - 1, k)

    def partition(self, nums, left, right):

        pivot = nums[right]
        lo = left

        for i in range(left, right):

            if nums[i] > pivot:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1

        nums[lo], nums[right] = nums[right], nums[lo]

        return lo

class Solution2:
    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]



