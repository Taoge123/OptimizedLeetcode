






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