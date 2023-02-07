"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/104904/Python-Heap-based-solution

[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]

4  0  5  0-5
4  9  5  4-9
10 9  5  5-10
10 90 18 9-18


"""

import heapq


class SolutionTony:
    def smallestRange(self, nums):
        res = [float('-inf'), float('inf')]
        heap = []
        maxi = 0
        for i, row in enumerate(nums):
            # store val, row and col
            heapq.heappush(heap, (row[0], i, 0))
            # get the largest value in first column
            maxi = max(maxi, row[0])

        while heap:
            mini, i, j = heapq.heappop(heap)
            if maxi - mini < res[1] - res[0]:
                res = [mini, maxi]
            # j到头了, 说明最后一列最小值算完了， 其他的都比他大， 再算没意义了
            if j + 1 == len(nums[i]):
                return res

            # current row, move to right, then update current max column and heap
            next_val = nums[i][j + 1]
            maxi = max(maxi, next_val)
            heapq.heappush(heap, (next_val, i, j + 1))



class Solution:
    def smallestRange(self, nums):
        # start our heap with the first element from every single list
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)

        mini, maxi = float('-inf'), float('inf')
        right = max(row[0] for row in nums)

        while heap:
            left, i, j = heapq.heappop(heap)
            # do we need to expand our bound for the final solution?
            if right - left < maxi - mini:
                mini, maxi = left, right
            # if we've finished iterating the current list, we've found our answer
            if j + 1 == len(nums[i]):
                return [mini, maxi]
            # get next element of the list we are currently iterating
            next_num = nums[i][j + 1]
            # set new maximum bound
            right = max(right, next_num)
            # put the next element into the heap
            heapq.heappush(heap, (next_num, i, j + 1))





nums = [[4,10,15,24,26],
        [0,9,12,20],
        [5,18,22,30]]
a = SolutionTony()
print(a.smallestRange(nums))

