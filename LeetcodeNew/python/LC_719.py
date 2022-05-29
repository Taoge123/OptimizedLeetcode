

import heapq


class SolutionTony:  # binary search template 1
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # binary search diff --> check if there k diff less than it

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSmallerCount(nums, mid, k) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getSmallerCount(self, nums, target, k):
        count = 0
        for i, num in enumerate(nums):
            idx = bisect_right(nums, num + target, i + 1)
            count += idx - i - 1
        return count



class Solution:
    def smallestDistancePair(self, nums, k):
        # sort the points
        nums.sort()  # [1,1,3] , heap = [(0,0,1),(2,1,2)]
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (right - left) // 2 + left
            count = 0
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left



class SolutionTLE:
    def smallestDistancePair(self, nums, k):
        # sort the points
        nums.sort()  # [1,1,3] , heap = [(0,0,1),(2,1,2)]
        heap = [(nums[i + 1] - nums[i], i, i + 1)
                for i in range(len(nums) - 1)]
        heapq.heapify(heap)  # Makes it into a BST

        for _ in range(k):
            d, root, nei = heapq.heappop(heap)
            if nei + 1 < len(nums):
                heapq.heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))
        return d



