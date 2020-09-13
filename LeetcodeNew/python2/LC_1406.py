"""
   X X X X X X
stone[1]

dp[i]: the max scorre the player can get when there are i piles alreay taken

dp[0] = stone[1]   + sum[2:n] - dp[1]
        stone[1:2] + sum[3:n] - dp[2]
        stone[1:3] + sum[4:n] - dp[3]


dp[i] = stone[i+1] + sum[i+2:n] - dp[i+1]       dp[i+1]
        stone[1+1:i+2] + sum[i+3:n] - dp[i+2]   dp[i+2]
        stone[i+1:i+3] + sum[i+4:n] - dp[i+3]   dp[i+3]


"""


class Solution:
    def stoneGameIII(self, stoneValue) -> str:
        self.cache = {}
        score = self.solve(0, stoneValue)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def solve(self, i, stoneValue):  # score diff
        n = len(stoneValue)
        if i >= n:
            return 0

        if i in self.cache:
            return self.cache[i]

        res = float('-inf')
        presum = 0

        for x in range(1, 4):
            if i + x - 1 >= n:
                break
            presum += stoneValue[i + x - 1]
            res = max(res, presum - self.solve(i + x, stoneValue))  # min-max process
        self.cache[i] = res
        return res



class SolutionBU:
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)

        total = 0
        for i in range(n - 1, -1, -1):
            total += stoneValue[i]
            dp[i] = -float('inf')
            for k in range(1, 4, 1):
                dp[i] = max(total - dp[i + k], dp[i])

        oppo = total - dp[0]
        if dp[0] > oppo:
            return 'Alice'
        elif dp[0] < oppo:
            return 'Bob'
        return 'Tie'


class SolutionWisdom:
    def stoneGameIII(self, stoneValue) -> str:
        n = len(stoneValue)
        stoneValue.insert(0, 0)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stoneValue[i]

        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            temp = 0
            for k in range(1, 4):
                if i + k > n:
                    break
                temp += stoneValue[i + k]
                dp[i] = max(dp[i], temp + preSum[n] - preSum[i + k] - dp[i + k])

        if dp[0] > preSum[-1] - dp[0]:
            return 'Alice'
        elif dp[0] < preSum[-1] - dp[0]:
            return 'Bob'
        return 'Tie'


