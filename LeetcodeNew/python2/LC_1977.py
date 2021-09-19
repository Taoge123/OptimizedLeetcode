"""
1 45631315361
14 5631315361
145 631315361
1456 31315361
14563 1315361
145631 315361
1456313 15361

"""


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




