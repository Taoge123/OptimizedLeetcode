"""
1696.Jump-Game-VI
本题初看很像第二类序列型DP，令dp[i]表示跳到第i个位置所能得到的最大得分。很容易写出状态转移方程：

dp[i] = max(dp[j] + nums[i]) for j=i-k, i-k+1, ... i-1
这样的话时间复杂度是o(NK)，根据数据范围可以判断会超时。如何改进呢？我们发现，dp[i]的关键是在[i-k,i-1]这个区间里找最大的dp值；类似地，dp[i+1]的关键是在[i-k+1,i]这个区间里找最大的dp值。这两步的两个区间是大部分重叠的，因此应该有高效地方法来分享这些信息，将取区间最大值的操作耗时均摊变小。

显然，这本质就是一个sliding window maximum的问题。我们关注一个长度为k的滑动窗口，里面的最大值就用来更新窗口后的第一个元素的dp值。sliding window maximum的标准解法是用deque，维护一个单调递减的队列。如果有新元素比队尾元素更大，那么它就更有竞争力（更新、更大）被用来更新后面的dp值，故队尾元素就可以舍弃而加入新元素。此外，如果队首元素脱离了这个滑动窗口的范围，也就可以将其舍弃。在每一个回合，deque里面的最大元素就是队首元素。

所以本题最优解的时间复杂度是o(N)

"""

"""
dp[i] the maximum score you can get when you arrive at nums[i]

max{dp[i-k], dp[i-k+1], dp[i-k+2], ... , dp[i-1]} + nums[i] -> dp[i] O(NK)

sliding window maximum

deque: monotonic decreasing queue
[8 7 6 5] {7} X X X X X X X

"""

import collections
import functools


class SolutionTony:
    def maxResult(self, nums, k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = collections.deque([])
        queue.append(0)

        for i in range(1, n):
            while queue and i - queue[0] > k:
                queue.popleft()

            # dp[i] = max(dp[queue[0]] + nums[i], dp[queue[0]])
            dp[i] = dp[queue[0]] + nums[i]
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        # must go to destination, return the last value in dp
        return dp[-1]



nums = [10,-5,-2,4,0,3]
k = 3
a = SolutionTony()
print(a.maxResult(nums, k))
#
#
# class Solution:
#     def maxResult(self, nums, k: int) -> int:
#
#         n = len(nums)
#         queue = collections.deque()
#         queue.append([nums[0], 0])
#
#         for i in range(1, n):
#             # pop the old node
#             # print(queue[0])
#             while queue and i - queue[0][1] > k:
#                 queue.popleft()
#
#             # pop the new node that are less than cur
#             cur = queue[0][0] + nums[i]
#             while queue and cur > queue[-1][0]:
#                 queue.pop()
#
#             queue.append([cur, i])
#
#         return queue[-1][0]




class SolutionDPTLE:
    def maxResult(self, nums, k: int) -> int:

        n = len(nums)
        @functools.lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return nums[-1]
            if i >= n:
                return 0
            res = float('-inf')
            for j in range(i + 1, min(n - 1, i + k) + 1):
                res = max(res, dfs(j) + nums[i])
            return res

        return dfs(0)




