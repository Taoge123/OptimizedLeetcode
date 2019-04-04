
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
