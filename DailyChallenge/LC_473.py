class SolutionTony:
    def makesquare(self, nums) -> bool:
        if not nums:
            return False
        nums.sort(reverse=True)
        summ = sum(nums)
        if summ % 4:
            return False

        target = summ // 4
        res = [0] * 4
        memo = {}
        return self.dfs(nums, 0, 0, target, res, memo)

    def dfs(self, nums, pos, cur, target, res, memo):
        if (pos, tuple(res)) in memo:
            return memo[(pos, tuple(res))]

        if pos == len(nums):
            if res[-1] == res[-2] == res[-3]:
                return True
            return False

        for i in range(4):
            if res[i] + nums[pos] > target:
                continue
            res[i] += nums[pos]
            if self.dfs(nums, pos + 1, cur + nums[i], target, res, memo):
                memo[(pos, tuple(res))] = True
                return memo[(pos, tuple(res))]
            res[i] -= nums[pos]
        memo[(pos, tuple(res))] = False
        return memo[(pos, tuple(res))]



