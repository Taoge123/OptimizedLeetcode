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


class Solution:
    def combine(self, n, k):
        res = []
        self.backtrack(n, k, 0, [], res)
        return res

    def backtrack(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path)
            return

        for i in range(index+1, n+1):
            self.backtrack(n, k, i, path + [i], res)



class Solution2:
    def combine(self, n, k):

        res = []
        self.backtrack(n, k, 1, [], res)
        return res

    def backtrack(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path[:])
        for i in range(index, n + 1):
            path.append(i)
            self.backtrack(n, k, i + 1, path, res)
            path.pop()





