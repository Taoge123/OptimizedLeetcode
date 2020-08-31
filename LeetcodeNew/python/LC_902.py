import math


class SolutionTLE:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        self.res = 0
        self.dfs(0, D, N)
        return self.res

    def dfs(self, cur, nums, N):
        if cur > N:
            return
        if cur > 0 and cur <= N:
            self.res += 1

        for char in nums:
            self.dfs(cur * 10 + int(char), nums, N)



class Solution:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        self.res = 0
        self.num = str(N)
        self.K = len(self.num)

        # 从1到K-1位，随便铸造
        for i in range(1, self.K):
            self.res += math.pow(len(D), i)

        self.dfs(0, 0, D)
        return int(self.res)

    def dfs(self, cur, pos, digits):
        if pos == self.K:
            self.res += 1
            return

        for char in digits:
            if char < self.num[pos]:
                self.res += math.pow(len(digits), self. K - 1 -pos)
            elif char == self.num[pos]:
                self.dfs(cur * 10 + int(char), pos + 1, digits)




