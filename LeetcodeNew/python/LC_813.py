
"""
X X X X X [X X i]

dp[i][K] : the maximum of sum of the average of the k groups
dp[j][K-1] + avg(j+1, i):



"""

import collections

class Solution:
    def largestSumOfAverages(self, A, K: int) -> float:
        n = len(A)
        memo = collections.defaultdict(int)
        summ = 0
        # calculate the average - like preSum
        for i in range(n):
            summ += A[i]
            memo[(i + 1, 1)] = summ / (i + 1)

        return self.search(A, K, n, memo)

    def search(self, A, k, n, memo):
        if memo[(n, k)]:
            return memo[(n, k)]
        if n < k:
            return 0

        summ = 0
        for i in range(n - 1, -1, -1):
            summ += A[i]
            memo[(n, k)] = max(memo[(n, k)], self.search(A, k - 1, i, memo) + summ / (n - i))

        return memo[(n, k)]


"""
  
X X X X X X X X X
            i   n
"""



class SolutionBU:
    def largestSumOfAverages(self, A, K: int) -> float:
        n = len(A)
        dp = [[0 for j in range(K+1)] for i in range(n)]

        summ = 0
        for i in range(n):
            summ += A[i]
            dp[i][1] = summ / (i+1)


        for k in range(2, K+ 1):
            for i in range(k - 1, n):
                summ = 0
                # j >= k - 1
                for j in range(i, k - 2, -1):
                    summ += A[j]
                    dp[i][k] = max(dp[i][k], dp[j - 1][k - 1] + summ / (i - j + 1))

        return dp[n - 1][K]



class SolutionDP2:
    def largestSumOfAverages(self, A, K):
        prefix = [0]
        for x in A:
            prefix.append(prefix[-1] + x)

        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        n = len(A)
        dp = [average(i, n) for i in range(n)]
        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]

