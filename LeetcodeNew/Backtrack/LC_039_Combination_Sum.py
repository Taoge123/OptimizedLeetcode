"""
Algorithm

The most important clue in these questions is to build the recursion tree.
https://goo.gl/photos/u3RDJWAiPEWUYbH46
Also you need to remember to prune the tree, else you run into maximum recursion depth issue.
We make use of the condition that all input numbers are positive.
This allows us to prune when adding the candidate[i] increases sum beyond target.
Since there are no negative numbers, we can safely stop at this point.
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(candidates, start, target, path, res):
            if target == 0:
                return res.append(path + [])

            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    path.append(candidates[i])
                    dfs(candidates, i, target - candidates[i], path, res)
                    path.pop()

        res = []
        dfs(candidates, 0, target, [], res)
        return res


def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(0, candidates, target, [], result, 0)
        return result

    def helper(self, idx, candidates, target, so_far, result, sum_so_far):
        if sum_so_far == target:
            result.append([x for x in so_far])
        else:
            for i in range(idx, len(candidates)):
                if sum_so_far + candidates[i] <= target:
                    so_far.append(candidates[i])
                    self.helper(i, candidates, target, so_far, result, sum_so_far + candidates[i])
                    so_far.pop()
        return



#Summary solution
class Solution:
    def combinationSum(self, candidates, target):
        def backtrack(tmp, start, end, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    tmp.append(candidates[i])
                    backtrack(tmp, i, end, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack([], 0, len(candidates), target)
        return ans


