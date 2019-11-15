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





