import heapq

class Solution:
    def smallestRange(self, nums):
        # first elem of all lists
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)

        res = -1e9, 1e9
        # get the max from first elem of all lists
        right = max(row[0] for row in nums)
        while heap:
            left, i, pos = heapq.heappop(heap)
            if right - left < res[1] - res[0]:
                res = left, right
            if pos + 1 == len(nums[i]):
                return res
            val = nums[i][pos + 1]
            right = max(right, val)
            heapq.heappush(heap, (val, i, pos + 1))



