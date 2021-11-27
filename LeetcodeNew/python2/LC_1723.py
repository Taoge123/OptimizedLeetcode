"""

https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1009828/Simple-Python-using-Partition-to-K-Equal-Sum-Subsets
https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/discuss/1009828/Simple-Python-using-Partition-to-K-Equal-Sum-Subsets


解法1：状态压缩DP
考虑到只有不超过12件jobs，可以用大小不超过4096的01二进制bit来表示任何jobs的组合状态。我们令dp[i][state]表示使用i个工人、分配state所代表的jobs时，可以得到的the minimum possible maximum working time。突破口是第i个工人做了哪些工作？我们可以枚举state的子集subset作为第i个工人的分配任务，那么状态转移方程

dp[i][state] = min{max(dp[i-1][state-subset], time[subset])} for all subsets.

"""

import functools


class Solution:
    def minimumTimeRequired(self, jobs, k):
        n = len(jobs)
        cost = [0] * (1 << n)
        for mask in range(1 << n):
            for j in range(n):
                cost[mask] += jobs[j] * ((mask >> j) & 1)

        @functools.lru_cache(None)
        def dfs(mask, k):
            if k == 1:
                return cost[mask]

            res = cost[mask]
            submask = mask
            while (submask - 1) & mask:
                submask = (submask - 1) & mask
                if cost[submask] >= res:
                    continue
                res = min(res, max(cost[submask], dfs(mask ^ submask, k - 1)))
            return res

        return dfs((1 << n) - 1, k)




class SolutionTLE:
    def minimumTimeRequired(self, jobs, k):
        # each worker gets a subset of tasks
        # remaining subproblem = bitmask of remaining tasks, k-1
        # enumerate all subsets for each worker ;)
        # make sure no intersection with already selected
        n = len(jobs)

        subset_sums = [0] * (1 << (n + 1))
        for mask in range(1 << (n + 1)):
            for job in range(n):
                if (mask >> job) & 1:
                    subset_sums[mask] += jobs[job]

        @functools.lru_cache(None)
        def dfs(picked, k):
            n = len(jobs)
            # return 0 if No job remaining AND No person remaining
            if k == 0 and picked + 1 == 1 << (n + 1):
                return 0
            elif k == 0 or picked + 1 == 1 << (n + 1):
                return float('inf')

            res = float('inf')
            for pick in range(1 << (n + 1)):
                if pick & picked == 0:  # no intersection(picked again)
                    # now assign remaining workers
                    res = min(res, max(subset_sums[pick], dfs(picked | pick, k - 1)))
            return res
        return dfs(0, k)

