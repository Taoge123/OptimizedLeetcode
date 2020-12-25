"""
https://www.youtube.com/watch?v=B5fa989qz4U&t=1s
https://www.youtube.com/watch?v=FSbFPH7ejHk

"""

"""

dp[i] : the maximum sum of nn-empty subsequence of that array ending wth nums[i]

XXXX [X j XX] i

dp[i] = max{dp[j] + nums[i]} for j = i-1, i-2, ..., i-k
O(NK)


sliding window maximum

"""
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
            if len(queue) > 0:
                dp[i] = max(dp[i], dp[queue[0]] + nums[i])

            while len(queue) > 0 and dp[queue[-1]] <= dp[i]:
                queue.pop()

            queue.append(i)

        return max(dp)




