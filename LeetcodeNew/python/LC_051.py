"""
The n-queens puzzle is the problem of placing n queens
on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


"""

class Solution:
    def solveNQueens(self, n):

        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                temp = "." * len(nums)
                self.dfs(nums, index + 1, path + [temp[:i] + "Q" + temp[i + 1:]], res)

    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[i] - nums[n]) == abs(n - i):
                return False
        return True





