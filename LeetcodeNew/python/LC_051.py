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
    def solveNQueens(self, n: int):

        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, pos, path, res):
        if pos == len(nums):
            res.append(path)
            return

        for i in range(len(nums)):
            nums[pos] = i
            if self.valid(nums, pos):
                node = "." * len(nums)
                self.dfs(nums, pos + 1, path + [node[:i] + 'Q' + node[i + 1:]], res)

    def valid(self, nums, pos):
        for i in range(pos):
            if nums[i] == nums[pos] or abs(nums[i] - nums[pos]) == abs(pos - i):
                return False
        return True


n = 8
a = Solution()
res = a.solveNQueens(n)
for i in res:
    print(i)


