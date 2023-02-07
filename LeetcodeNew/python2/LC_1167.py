import heapq

class Solution:
    def connectSticks(self, sticks) -> int:
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            res += (a + b)
            heapq.heappush(sticks, a + b)
        return res




class SolutionToBeFixed:
    def connectSticks(self, nums) -> int:

        n = len(nums)

        def dfs(i, j):
            if i >= j:
                return 0

            res = 10 ** 10
            for k in range(i + 1, j + 1):
                res = min(res, dfs(i + 1, k - 1) + dfs(k + 1, j) + nums[i] * nums[k])
            return res

        return dfs(0, n - 1)


