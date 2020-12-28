

class Solution:
    def maxSlidingWindow(self, nums, k):

        queue = collections.deque([])
        res = []

        for i in range(len(nums)):
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


