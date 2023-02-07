
class Solution:
    def minOperations(self, grid, x: int) -> int:
        # 这里的2D和1D没有差太多 --> 把它变为1D来看

        m, n = len(grid), len(grid[0])
        # convert to 1D array
        nums = []
        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])

        nums.sort()
        # check if there is valid solution
        for i in range(len(nums)):
            if nums[i] % x != nums[0] % x:
                return -1

        # find middle value, use it as origin point
        res = 0
        mid = nums[len(nums) // 2]
        for num in nums:
            res += abs(num - mid) // x
        return res



