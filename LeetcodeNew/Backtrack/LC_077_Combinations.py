

"""

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))


class Solution2:
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]


class Solution3:
    def combine(self, n, k):
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs

class SolutionCaikehe:
    def combine(self, n, k):
        res = []
        self.dfs(range(1, n + 1), k, 0, [], res)
        return res


    def dfs(self, nums, k, index, path, res):
        # if k < 0:  #backtracking
        # return
        if k == 0:
            res.append(path)
            return  # backtracking
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, i + 1, path + [nums[i]], res)


class Solution5:
    # @return a list of lists of integers
    # 9:14
    def __init__(self):
        self.output = []


    def combine(self, n, k, pos=0, temp=None):
        temp = temp or []

        if len(temp) == k:
            self.output.append(temp[:])
            return

        for i in range(pos, n):
            temp.append(i + 1)
            self.combine(n, k, i + 1, temp)
            temp.pop()

        return self.output


