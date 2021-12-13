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

    def dfs(self, nums, i, path, res):
        if i == len(nums):
            res.append(path)
            return

        for j in range(len(nums)):
            nums[i] = j
            if self.valid(nums, i):
                node = "." * len(nums)
                self.dfs(nums, i + 1, path + [node[:j] + 'Q' + node[j + 1:]], res)

    def valid(self, nums, i):
        for j in range(i):
            if nums[i] == nums[j] or abs(nums[i] - nums[j]) == abs(i - j):
                return False
        return True

n = 8
a = Solution()
res = a.solveNQueens(n)
for i in res:
    print(i)


