"""
[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

4  0  5  0-5
4  9  5  4-9
10 9  5  5-10
10 90 18 9-18


"""

import heapq

class Solution:
    def smallestRange(self, nums):
        # first elem of all lists
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)

        res = [float('-inf'), float('inf')]
        # get the max from first elem of all lists
        right = max(row[0] for row in nums)

        while heap:
            left, row, pos = heapq.heappop(heap)
            if right - left < res[1] - res[0]:
                res = [left, right]
            print(pos + 1, len(nums[row]))
            # pos tracks index, i tracks which row
            if pos + 1 == len(nums[row]):
                return res
            # next val
            val = nums[row][pos + 1]
            right = max(right, val)
            heapq.heappush(heap, (val, row, pos + 1))



nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
a = Solution()
print(a.smallestRange(nums))

