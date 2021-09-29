"""
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1420180/Python-recursion-%2B-memo-%2B-early-stop-condition
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1420561/Python-3-Simple-fast-solution-using-memoization-and-inverse-running-sums
https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/discuss/1455340/Top-down-DP-with-some-pruning-tricks
"""

import functools


class Solution:
    def minimizeTheDifference(self, mat, target):

        memo = {}
        # optimization
        mat = map(set, mat)
        mat = list(map(sorted, mat))
        return self.dfs(mat, target, 0, memo)

    def dfs(self, mat, target, i, memo):
        if (i, target) in memo:
            return memo[(i, target)]

        if i == len(mat):
            return abs(target)

        res = float('inf')
        for num in mat[i]:
            res = min(res, self.dfs(mat, target - num, i + 1, memo))
            # optimization
            # We don't need to go further since this array is sorted.
            if target - num < 0:
                break
        memo[(i, target)] = res
        return res



class SolutionTLE:
    def minimizeTheDifference(self, mat, target):

        memo = {}
        return self.dfs(mat, target, 0, memo)

    def dfs(self, mat, target, i, memo):
        if (i, target) in memo:
            return memo[(i, target)]

        if i == len(mat):
            return abs(target)

        res = float('inf')
        for num in mat[i]:
            res = min(res, self.dfs(mat, target - num, i+ 1, memo))
        memo[(i, target)] = res
        return res



