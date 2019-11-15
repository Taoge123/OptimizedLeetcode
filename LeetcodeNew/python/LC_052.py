class Solution:
    def totalNQueens(self, n: int) -> int:

        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return

        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index + 1)

    def valid(self, nums, index):
        for i in range(index):
            if nums[index] == nums[i] or abs(nums[index] - nums[i]) == abs(index - i):
                return False
        return True







