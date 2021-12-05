"""
1 45631315361
14 5631315361
145 631315361
1456 31315361
14563 1315361
145631 315361
1456313 15361

"""

import functools


class SolutionMemo:
    def numberOfCombinations(self, num: str) -> int:
        n = len(num)
        @functools.lru_cache(None)
        def dfs(i, prev):
            if i == n:
                return 1

            if num[i] == '0':
                return 0

            res = 0
            for j in range(i, n):
                total = int(num[i:j+1])
                if total >= prev:
                    res += dfs(j + 1, total)
                    res %= (10 ** 9 + 7)
            return res

        return dfs(0, 0)



class Solution:
    def numberOfCombinations(self, num: str) -> int:
        memo = {}
        return self.dfs(num, 0, 0, memo)

    def dfs(self, nums, i, prev, memo):

        if (i, prev) in memo:
            return memo[(i, prev)]

        n = len(nums)
        if i == n:
            return 1

        if nums[i] == '0':
            return 0

        res = 0
        for j in range(i, n):
            total = int(nums[i:j+1])
            if total >= prev:
                res += self.dfs(nums, j + 1, total, memo)
                res %= (10 ** 9 + 7)
        memo[(i, prev)] = res
        return res


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10 ** 9 + 7

        # counts[i][j] is what is the count for number starts at i and end at j-1
        n = len(num)
        counts = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            # the last number starting at i
            counts[i][n] = 1 if num[i] != '0' else 0

        def less(i, j, L):
            return num[i:i + L] <= num[j:j + L]

        ans = counts[0][n]
        for j in range(n - 1, 0, -1):  # start of the next number
            k, total = n, 0  # total will accumulate the sum from j=>[j,k)
            start = max(0, 2 * j - k)  # ignore all the previous starting number that cause range [i:j) > [j:k)
            for i in range(start, j):  # start of the current number
                if num[i] != '0':
                    # ensure the number from [i,j) < [j,k)
                    while k - j > j - i or (k - j == j - i and less(i, j, j - i)):
                        total += counts[j][k]
                        total %= MOD
                        k -= 1

                    counts[i][j] = total

            ans += counts[0][j]
            ans %= MOD

        return ans


