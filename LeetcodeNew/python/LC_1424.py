import collections


class Solution:
    def findDiagonalOrder(self, nums):
        res = []
        m = len(nums)

        queue = collections.deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            res.append(nums[row][col])
            # we only add the number at the bottom if we are at column 0
            if col == 0 and row + 1 < m:
                queue.append((row + 1, col))
            # add the number on the right
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return res



