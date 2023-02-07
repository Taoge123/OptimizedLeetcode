"""
https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/2850089/c-dp-dfs/
https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/2678462/recursive-dfs-with-memoization/

Explanation
Sort the jobs by endTime.

dp[time] = profit means that within the first time duration,
we cam make at most profit money.
Intial dp[0] = 0, as we make profit = 0 at time = 0.

For each job = [s, e, p], where s,e,p are its start time, end time and profit,
Then the logic is similar to the knapsack problem.
If we don't do this job, nothing will be changed.
If we do this job, binary search in the dp to find the largest profit we can make before start time s.
So we also know the maximum cuurent profit that we can make doing this job.

Compare with last element in the dp,
we make more money,
it worth doing this job,
then we add the pair of [e, cur] to the back of dp.
Otherwise, we'd like not to do this job.

max number of non-overlap interlaps
---------
  ---------
     ----------
       ----------

we have weights in this problem

t:
-------[ t ]
t: k-th meeting ending time
dp[t] : max{dp[nearestEndTime], dp[lastEndTimeBeforeKthStartTime] + val[k]}

------------e
-----e
        s-------t

1235.Maximum-Profit-in-Job-Scheduling
将所有的区间按照endTime进行排序是一个很常见的尝试的手段。

假设我们按照如上排序后的顺序，遍历每个区间。我们会想，如果我们选择了第i个区间的话，那么我们就有机会更新这么一个记录dp[endTime[i]]，其中dp[t]表示截至t时刻的最大收益。显然，我们会有dp[endTime[i]] = max(dp[endTime[i]], dp[startTime[i]]+profit[i]).这像不像DP的思想？

当然，我们不可能在dp里存放每一个时刻的最大收益，我们只能离散化存放每一个endTime时刻的最大收益。也就是说，dp应该是一个哈希表。因此，可能dp记录里并没有startTime[i]，但我们只需要找到第一个小于等于startTime[i]的时刻即可，记为t，对应的dp[t]=val。特别注意，我们试图记录dp[endTime[i]] = val+profit[i]的时候，前提条件是val + profit[i]一定要比dp里面最后时刻的收益还要大。也就是说，我们在dp里面只存放按收益递增的time->profit键值对。事实上，这也合情合理，如果t0<t1，且dp[t0]>dp[t1]的话，t1并没有必要塞入这个dp数组里面（既浪费了时间反而收益下降）。

于是我们的算法就呼之欲出了。对于当前的区间i，我们在dp数组（或者有序的map）里面考察在startTime[i]时刻之前的最大收益val。假设通过二分法我们得到了它，于是我们就有机会添加dp[endTime[i]] = val+profit[i]，但这仅当t+profit[i]大于当前dp最后一个时刻的存储值时才操作。

有了这样一个在时间和收益上都是递增的序列dp，我们就可以不断追加dp[endTime[i]]的记录，来创建更新的时刻的最大收益。


----------|
   -------|-----
        --|--------
          |          -------
"""


import bisect
import heapq
import functools


class SolutionMemo:
    def jobScheduling(self, startTime, endTime, profit) -> int:

        nums = []
        for i, j, k in zip(startTime, endTime, profit):
            nums.append([i, j, k])
        nums = sorted(nums, key=lambda x: x[0])
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0

            # initialize it as current profit, if we can find another one after this, then add dfs after this value
            take = nums[i][2]
            for j in range(i + 1, n):
                # if j can be a new start, take it
                if nums[i][1] <= nums[j][0]:
                    # found the next one, should break
                    take += dfs(j)
                    break
            notTake = dfs(i + 1)
            return max(take, notTake)

        return dfs(0)



class SolutionRika: # binary search + topdown dp
    def jobScheduling(self, startTime, endTime, profit) -> int:
        graph = []
        n = len(startTime)
        for i in range(n):
            graph.append([startTime[i], endTime[i], profit[i]])
        graph.sort()    # sort by start time

        memo = {}
        return self.dfs(graph, 0, memo)

    def dfs(self, graph, i, memo):
        if i in memo:
            return memo[i]

        if i == len(graph):
            return 0

        not_pick = self.dfs(graph,i + 1, memo)
        start, end, p = graph[i]
        pos = self.search_right(graph, end) # find next start time position
        if pos == -1:
            pick = p                # this is the last job
        else:
            pick = p + self.dfs(graph,pos,memo)     # there is next job

        memo[i] = max(pick, not_pick)
        return memo[i]

    def search_right(self, graph, target):
        left, right = 0, len(graph) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if graph[mid][0] >= target:
                right = mid - 1
            elif graph[mid][0] < target:
                left = mid + 1

        return left


class SolutionTLE:
    def jobScheduling(self, startTime, endTime, profit) -> int:

        nums = []
        for i, j, k in zip(startTime, endTime, profit):
            nums.append([i, j, k])
        nums.sort()
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, last):
            if i >= n:
                return 0

            res = 0
            if nums[i][0] < last:
                # if current start time < previous ending time, we can take this
                res = max(res, dfs(i + 1, last))
            else:
                # if current start time >= previous ending time, we either skip or take it
                res = max(res, dfs(i + 1, last), dfs(i + 1, nums[i][1]) + nums[i][2])
            return res

        return dfs(0, 0)


startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]



a = Solution()
print(a.jobScheduling(startTime, endTime, profit))

class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for start, end, profit in jobs:
            idx = bisect.bisect_left(dp, [start + 1]) - 1
            newProfit = dp[idx][1] + profit
            if newProfit > dp[-1][1]:
                dp.append([end, newProfit])
        return dp[-1][1]



class Solution2:
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v: v[0])
        heap = []
        res = 0

        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                node = heapq.heappop(heap)
                res = max(res, node[1])

            heapq.heappush(heap, (e, p + res))

        while heap:
            node = heapq.heappop(heap)
            res = max(res, node[1])

        return res





class Solution3:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        n = len(startTime)
        endTime, startTime, profit = zip(*(sorted(zip(endTime, startTime, profit))))
        pre = [-1] * n
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if endTime[j] <= startTime[i]:
                    pre[i] = j
                    break
        dp = [0] * n
        dp[0] = profit[0]
        for i in range(1, n):
            dp[i] = max(dp[pre[i]]+profit[i], dp[i-1])
        return dp[-1]

