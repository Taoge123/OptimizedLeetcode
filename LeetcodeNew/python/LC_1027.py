import collections


class SolutionWisdom:
    def longestArithSeqLength(self, A) -> int:
        dp = collections.defaultdict(int)
        res = 1
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (j, diff) not in dp:
                    dp[(i, diff)] = 2
                else:
                    dp[(i, diff)] = dp[(j, diff)] + 1
                res = max(res, dp[(i, diff)])
        return res




class SolutionTLE:
    def longestArithSeqLength(self, A) -> int:
        # dp[i, diff] = length
        self.cache = collections.defaultdict(dict)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                res = max(res, self.dfs(A, i, diff) + 2)
        return res

    def dfs(self, A, i, diff):
        if i < 0:
            return 0

        if self.cache.get(i) != None and diff in self.cache.get(i):
            return self.cache[i][diff]

        res = 0
        for j in range(i - 1, -1, -1):
            if A[i] - A[j] == diff:
                res = max(res, 1 + self.dfs(A, j, diff))

        self.cache[i][diff] = res
        return self.cache[i][diff]




class Solution:
    def longestArithSeqLength(self, A) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())


A = [9,4,7,2,10]
a = Solution()
print(a.longestArithSeqLength(A))


