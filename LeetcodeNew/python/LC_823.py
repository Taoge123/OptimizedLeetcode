"""
https://leetcode.com/problems/binary-trees-with-factors/discuss/289994/DFS-in-Python


"""


import collections
import functools

class SolutionTony1:
    def numFactoredBinaryTrees(self, arr) -> int:

        nums = sorted(arr)
        se = set(nums)

        @functools.lru_cache(maxsize=None)
        def dfs(i):
            res = 1
            for j in range(len(nums)):
                # Early stop
                if nums[j] > i // 2:
                    break
                if i % nums[j] == 0 and i // nums[j] in se:
                    res += dfs(nums[j]) * dfs(i // nums[j])
            return res

        res = 0
        for i in range(len(nums)):
            # Get the number of trees with s[i] as root
            res += dfs(nums[i])
        return res % 1000000007




class SolutionTony2:
    def numFactoredBinaryTrees(self, arr) -> int:

        mod = 10 ** 9 + 7
        nums = set(arr)

        def factor(i):
            res = []
            for j in nums:
                if i % j == 0 and i // j in nums:
                    res.append([j, i // j])
            return res

        @functools.lru_cache(None)
        def dfs(i):
            res = 1
            for left, right in factor(i):
                res += dfs(left) * dfs(right)

            return res

        return sum(dfs(num) for num in nums) % mod


class Solution:
    def numFactoredBinaryTrees(self, A) -> int:

        A.sort()
        table = collections.defaultdict(int)
        count = 1
        table[A[0]] = count

        for i in range(1, len(A)):
            count = 1
            for num in table.keys():
                if A[i] % num == 0 and A[i] // num in table:
                    count += table[num] * table[A[i] // num]
            table[A[i]] = count

        res = 0
        for num in table.keys():
            res += table[num]
            res %= (10**9 + 7)
        return res



