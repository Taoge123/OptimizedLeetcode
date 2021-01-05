


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        minQueue = collections.deque()
        maxQueue = collections.deque()
        i = 0
        res = 0

        for j in range(len(nums)):
            while abs(maxQueue[0][0] - minQueue[0][0]) > limit and i < j:
                if minQueue[0][-1] <= i:
                    minQueue.popleft()
                elif maxQueue[0][-1] <= i:
                    maxQueue.popleft()
                i += 1
            while minQueue and minQueue[-1][0] > nums[j]:
                minQueue.pop()
            minQueue.append([nums[j], j])
            while maxQueue and maxQueue[-1][0] < nums[j]:
                maxQueue.pop()
            maxQueue.append([nums[j], j])

            res = max(res, j - i + 1)

        return res


