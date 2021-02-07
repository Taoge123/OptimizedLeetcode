class Solution:
    def minAbsDifference(self, nums, goal: int) -> int:
        self.res = float('inf')
        self.dfs(nums, 0, 0, goal)
        return self.res

    def dfs(self, nums, pos, summ, goal):
        if self.res == 0:
            return 0

        if pos == len(nums):
            self.res = min(self.res, abs(summ - goal))
            return self.res

        self.dfs(nums, pos + 1, summ + nums[pos], goal)
        self.dfs(nums, pos + 1, summ, goal)



nums = [3346,-3402,-9729,7432,2475,6852,5960,-7497,3229,6713,8949,9156,3945,-8686,1528,5022,-9791,-3782,-191,-9820,7720,-6067,-83,6793,340,7793,8742,8067]
goal = -20357
a = Solution()
print(a.minAbsDifference(nums, goal))










