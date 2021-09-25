"""
total / n == curSUm / curNum
total * curNum == n * curSum

https://www.youtube.com/watch?v=tMaWUhj5YaU&feature=youtu.be
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/805.Split-Array-With-Same-Average




"""


"""
total // n == sum // num
"""


class SolutionTony:
    def splitArraySameAverage(self, nums):
        total, n = sum(nums), len(nums)
        memo = {}
        # as least one of the set have less than half of elements
        for k in range(1, len(nums) // 2 + 1):
            if total * k % n != 0:
                continue
            if self.dfs(nums, 0, total * k / n, k, memo):
                return True
        return False

    def dfs(self, nums, i, target, count, memo):

        if (i, count, target) in memo:
            return memo[(i, count, target)]

        if count == 0 and target == 0:
            return True
        if count == 0 and target == 0:
            return False
        if i >= len(nums):
            return False

        take = self.dfs(nums, i + 1, target - nums[i], count - 1, memo)
        no_take = self.dfs(nums, i + 1, target, count, memo)

        memo[(i, count, target)] = take or no_take
        return memo[(i, count, target)]


class SolutionTDTLEnow:
    def splitArraySameAverage(self, A) -> bool:
        total = sum(A)
        n = len(A)
        for num in range(1, n // 2 + 1):
            if total * num % n != 0:
                continue
            # total * num / n is the curSum
            if self.dfs(A, num, total * num / n, 0):
                return True
        return False

    def dfs(self, A, num, curSum, index):
        if curSum == 0 and num == 0:
            return True

        if index == len(A):
            return False

        if num == 0 or curSum == 0:
            return False

        if self.dfs(A, num - 1, curSum - A[index], index + 1):
            return True

        i = index
        while i < len(A) and A[i] == A[index]:
            i += 1

        if i < len(A) and self.dfs(A, num, curSum, i):
            return True

        return False


class SolutionTLE:
    def splitArraySameAverage(self, nums) -> bool:

        self.n = len(nums)
        self.total = sum(nums)
        # nums.sort()
        memo = {}
        return self.dfs(nums, 0, 0, 0, memo)

    def dfs(self, nums, i, curNum, curSum, memo):
        if (i, curNum, curSum) in memo:
            return memo[(i, curNum, curSum)]

        n = len(nums)
        if curNum > 0 and curNum < n and self.total * curNum == self.n * curSum:
            return True

        if i >= n:
            return False

        if self.dfs(nums, i + 1, curNum + 1, curSum + nums[i], memo):
            memo[(i, curNum, curSum)] = True
            return True

        if self.dfs(nums, i + 1, curNum, curSum, memo):
            memo[(i, curNum, curSum)] = True
            return True
        memo[(i, curNum, curSum)] = False
        return False


class SolutionTLE2:
    def splitArraySameAverage(self, A) -> bool:
        self.n = len(A)
        self.total = sum(A)
        self.avg = self.total / self.n
        # A.sort()

        return self.dfs(A, 0, 0, 0)

    def dfs(self, A, curSum, curNum, index):
        if curNum > 0 and curNum < len(A) and self.total * curNum == self.n * curSum:
            return True

        if index == len(A):
            return False
        if curNum > 0:
            if curNum / curNum > self.avg and A[index] > self.avg:
                return False

        # Choose
        if self.dfs(A, curSum + A[index], curNum + 1, index + 1):
            return True

        # We can skip the duplicated numbers
        i = index
        while i < len(A) and A[i] == A[index]:
            i += 1

        if self.dfs(A, curSum, curNum, i):
            return True

        return False




class SolutionTonyTLE:
    def splitArraySameAverage(self, A) -> bool:
        self.summ = sum(A)
        self.n = len(A)
        memo = {}
        return self.dfs(A, 0, 0, 0, memo)

    def dfs(self, nums, pos, summ, count, memo):
        # print(self.summ, self.n, summ, count)
        print(count, summ)
        if (pos, count, summ) in memo:
            return memo[(pos, count, summ)]

        if pos >= len(nums):
            return False

        if summ > self.summ:
            return False

        if summ and count < len(nums) and summ * self.n == self.summ * count:
            return True

        if self.dfs(nums, pos + 1, summ + nums[pos], count + 1, memo):
            memo[(pos, count, summ)] = True
            return memo[(pos, count, summ)]

        i = pos
        while i < len(nums) and nums[i] == nums[pos]:
            i += 1

        if self.dfs(nums, i, summ, count, memo):
            memo[(pos, count, summ)] = True
            return memo[(i, count, summ)]

        memo[(pos, count, summ)] = False
        return memo[(pos, count, summ)]



"""
total / n == sum / num
total * num == n * sum


背包问题外循环都是物品
for object in ...
    for capacity in ...
        dp[c] = dp[c-object][i] + 1


In this case, 
dp[sum][num] : 1/1
if (dp[sum-a][num-1] == 1)
    dp[sum][num] = 1


"""


class SolutionBottomUpTLE:
    def splitArraySameAverage(self, A) -> bool:
        n = len(A)
        total = sum(A)
        A.sort()
        # dp[summ][num] if there are num elements whose summ == num
        dp = [[0 for j in range(n + 1)] for i in range(total + 1)]
        dp[0][0] = 1

        for a in A:
            newDP = copy.deepcopy(dp)
            for summ in range(a, total + 1):
                for num in range(1, n):
                    # 这轮dp依赖于上轮dp
                    if newDP[summ - a][num - 1] == 1:
                        dp[summ][num] = 1
                        if dp[summ][num] == 1 and total * num == n * summ:
                            return True
        return False


class SolutionTLEAgain:
    def splitArraySameAverage(self, A) -> bool:
        n = len(A)
        total = sum(A)
        # dp[summ][num] if there are num elements whose summ == num
        dp = [[0 for j in range(n + 1)] for i in range(total + 1)]
        dp[0][0] = 1

        curSum = 0
        for a in A:
            curSum += a
            for summ in range(curSum, a - 1, -1):
                for num in range(n // 2 + 1, 0, -1):
                    # 这轮dp依赖于上轮dp
                    if dp[summ - a][num - 1] == 1:
                        dp[summ][num] = 1
                        if num != n and dp[summ][num] == 1 and total * num == n * summ:
                            return True
        return False







