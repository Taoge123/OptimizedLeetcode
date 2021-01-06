import collections



class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:

        n = len(nums)
        dp = [0] * n
        queue = collections.deque()

        for i in range(n):
            while queue and queue[0] < i - k:
                queue.popleft()

            dp[i] = nums[i]
            if queue:
                dp[i] = max(dp[i], dp[queue[0]] + nums[i])

            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()

            queue.append(i)

        return max(dp)

