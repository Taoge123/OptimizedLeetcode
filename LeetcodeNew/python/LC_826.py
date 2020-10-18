
class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker) -> int:
        n = len(difficulty)
        jobs = [[0, 0]] * n
        for i in range(n):
            jobs[i] = [difficulty[i], profit[i]]

        jobs.sort()
        worker.sort()

        maxi = 0
        res = 0
        i = 0
        for skill in worker:
            while i < n and skill >= jobs[i][0]:
                maxi = max(maxi, jobs[i][1])
                i += 1
            res += maxi
        return res


