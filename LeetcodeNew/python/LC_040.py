class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, target, [], res)
        return res

    def backtrack(self, nums, index, target, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.backtrack(nums, i + 1, target - nums[i], path + [nums[i]], res)


