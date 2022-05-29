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
import random

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

class Solution3:
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums[:k]:
            heapq.heappush(heap, num)
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        return heapq.heappop(heap)


    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k-1]


# Alan

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1
        target_index = len(nums) - k
        while l <= r:
            pivot_index = self.partition(nums, l, r)
            if pivot_index == target_index:
                return nums[target_index]
            elif pivot_index < target_index:
                l = pivot_index + 1
            else:
                r = pivot_index - 1
        return 0

    def partition(self, nums, left, right):
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot] # put pivot at rightmost position
        i = left
        for j in range(left, right): # left to right-1
            if nums[j] <= nums[right]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
        return i

    # Hoare - faster but harder to implement
    def partition2(self, nums, lo, hi):
        pivot_index = random.randint(lo, hi)
        nums[lo], nums[pivot_index] = nums[pivot_index], nums[lo]
        i, j = lo + 1, hi
        while True:
            while i <= j and nums[i] <= nums[lo]:
                i += 1
            while i <= j and nums[j] >= nums[lo]:
                j -= 1
            if j <= i:
                nums[lo], nums[j] = nums[j], nums[lo]
                return j
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return 0


nums = [3,2,9,4,5,6,5]
k = 4
a = Solution()
print(a.findKthLargest(nums, k))


