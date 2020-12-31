import collections

class Solution:
    def largestSubarray(self, nums, k: int):

        if k == 1:
            return [max(nums)]
        n = len(nums)
        queue = collections.deque()

        for i, val in enumerate(nums):
            if n - i >= k:
                while queue and val > queue[0]:
                    queue.popleft()
            if len(queue) < k:
                queue.append(val)

            elif len(queue) == k and queue and queue[1] > queue[0]:
                queue.popleft()
                queue.append(val)

        return list(queue)

