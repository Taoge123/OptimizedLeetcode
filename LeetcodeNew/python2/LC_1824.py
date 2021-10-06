class SolutionTonnie:
    def minSideJumps(self, obstacles) -> int:

        memo = {}
        return self.dfs(obstacles, 0, 2, memo)

    def dfs(self, nums, i, lane, memo):

        if (i, lane) in memo:
            return memo[(i, lane)]

        if i >= len(nums):
            return 0

        if nums[i] == lane:
            return float('inf')

        res = float('inf')
        if i < len(nums) - 1 and lane == nums[i + 1]:
            for pos in range(1, 4):
                if nums[i] == pos:
                    continue
                res = min(res, self.dfs(nums, i + 1, pos, memo) + 1)
        else:
            res = self.dfs(nums, i + 1, lane, memo)

        memo[(i, lane)] = res
        return res



class SolutionTony:
    def minSideJumps(self, obstacles) -> int:

        memo = {}
        return self.dfs(obstacles, 0, 2, memo)

    def dfs(self, nums, i, lane, memo):

        if (i, lane) in memo:
            return memo[(i, lane)]

        if i >= len(nums):
            return 0

        if nums[i] == lane:
            return float('inf')

        res = self.dfs(nums, i + 1, lane, memo)
        if i < len(nums) - 1 and lane == nums[i + 1]:
            for pos in range(1, 4):
                if nums[i] == pos:
                    continue
                res = min(res, self.dfs(nums, i + 1, pos, memo) + 1)

        memo[(i, lane)] = res
        return res




