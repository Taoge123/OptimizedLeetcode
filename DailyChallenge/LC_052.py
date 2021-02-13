


class Solution:
    def totalNQueens(self, n: int) -> int:

        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res

    def dfs(self, nums, pos):
        if pos == len(nums):
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
