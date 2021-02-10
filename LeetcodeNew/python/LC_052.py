"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]


"""

class Solution:
    def totalNQueens(self, n: int) -> int:

        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, pos):
        if index == len(nums):
            self.res += 1
            return

        for i in range(len(nums)):
            nums[pos] = i
            if self.valid(nums, pos):
                self.dfs(nums, pos + 1)

    def valid(self, nums, pos):
        for i in range(pos):
            if nums[pos] == nums[i] or abs(nums[pos] - nums[i]) == abs(pos - i):
                return False
        return True







