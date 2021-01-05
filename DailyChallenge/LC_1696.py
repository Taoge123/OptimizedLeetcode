import collections

class Solution:
    def maxResult(self, nums, k: int) -> int:

        n = len(nums)
        queue = collections.deque()
        queue.append([nums[0], 0])

        for i in range(1, n):
            while queue and i - queue[0][1] > k:
                queue.popleft()

            cur = queue[0][0] + nums[i]
            while queue and cur > queue[-1][0]:
                queue.pop()

            queue.append([cur, i])

        return queue[-1][0]

