"""
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
"""

import bisect
import heapq

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

