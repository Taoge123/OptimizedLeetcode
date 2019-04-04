
"""
We have jobs: difficulty[i] is the difficulty of the ith job, and profit[i] is the profit of the ith job.

Now we have some workers. worker[i] is the ability of the ith worker,
which means that this worker can only complete a job with difficulty at most worker[i].

Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.
If a worker cannot complete any job, his profit is $0.

What is the most profit we can make?

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.
Notes:

1 <= difficulty.length = profit.length <= 10000
1 <= worker.length <= 10000
difficulty[i], profit[i], worker[i]  are in range [1, 10^5]

"""

"""
Algorithm

We can use a "two pointer" approach to process jobs in order. We will keep track of best, the maximum profit seen.

For each worker with a certain skill, after processing all jobs with lower or equal difficulty, we add best to our answer.

思考
首先数据量很大，直接暴力写是不太可能了，可以先对难度和利润进行排序，这样worker的遍历时就可以及时停止遍历了，
还有就是使用HashMap记录已经有了的worker数据进行重用，因为能力相同的工人可以得到的最大利润也是相同的。

解题方法
给的提示是双指针，其实我第一感觉是贪心的。事实上就是贪心。

贪心的策略是给每个工人计算在他的能力范围内，他能获得的最大收益，把这样的工作分配给他。

做的方法是先把困难程度和收益压缩排序，然后对工人排序，再对每个工人，通过从左到右的遍历确定其能获得收益最大值。
由于工作和工人都已经排好序了，每次只需要从上次停止的位置继续即可，因此各自只需要遍历一次。

你可能会想到，每个工作的收益和其困难程度可能不是正相关的，可能存在某个工作难度小，但是收益反而很大，
这种怎么处理呢？其实这也就是这个算法妙的地方，curMax并不是在每个工人查找其满足条件的工作时初始化的，
而是在一开始就初始化了，这样一直保持的是所有的工作难度小于工人能力的工作中，能获得的收益最大值。

也就是说在查找满足条件的工作的时候，curMax有可能不更新，其保存的是目前为止的最大。
res加的也就是在满足工人能力情况下的最大收益了。

时间复杂度是O(M+N)，空间复杂度是O(MN)。


"""

class Solution1:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

"""
Explanation

1. zip difficulty and profit as jobs.
2. sort jobs and sort 'worker'.
3. 2 pointers idea, for each worker, find his maximum profit he can make under his ability.
   Because we have sorted jobs and worker, we will go through two lists only once.
   It will be only O(M+N).

Time Complexity
O(NlogN + MlogM), as we sort list.
"""

class SolutionLee:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        res = i = maxp = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maxp = max(jobs[i][1], maxp)
                i += 1
            res += maxp
        return res


class Solution3:
    def maxProfitAssignment(self, difficulty, profit, worker):

        job = sorted(list(zip(profit, difficulty)), reverse=True)
        worker.sort(reverse=True)

        i = j = 0
        total = 0
        while i < len(worker) and j < len(job):
            if worker[i] >= job[j][1]:
                total += job[j][0]
                i += 1
            else:
                j += 1
        return total


class Solution4:
    def maxProfitAssignment(self, difficulty, profit, worker):
        g = sorted(zip(difficulty, profit))
        s = curr = 0
        for i in sorted(worker):
            while g and g[0][0] <= i:
                curr = max(curr, g.pop(0)[1])
            s += curr
        return s
