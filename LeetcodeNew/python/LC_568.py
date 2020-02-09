
class Solution1:
    def maxVacationDays(self, flights, days) -> int:
        M = len(flights)
        N = len(days[0])

        memo = [[float('-inf') for i in range(N)] for j in range(M)]
        return self.dfs(flights, days, 0, 0, memo)

    def dfs(self, flights, days, curCity, weekno, memo):
        if weekno == len(days[0]):
            return 0

        if memo[curCity][weekno] != float('-inf'):
            return memo[curCity][weekno]
        res = 0
        for i in range(len(flights)):
            if flights[curCity][i] == 1 or i == curCity:
                temp = days[i][weekno] + self.dfs(flights, days, i, weekno +1, memo)
                res = max(res, temp)

        memo[curCity][weekno] = res
        return res


class Solution2:
    def maxVacationDays(self, flights, days) -> int:
        N = len(flights)
        K = len(days[0])
        dp = [float('-inf')] * N
        dp[0] = 0

        for i in range(K):
            temp = [float('-inf')] * N
            for j in range(N):
                for k in range(N):
                    if j == k or flights[k][j] == 1:
                        temp[j] = max(temp[j], dp[k] + days[j][i])

            dp = temp

        return max(dp)




