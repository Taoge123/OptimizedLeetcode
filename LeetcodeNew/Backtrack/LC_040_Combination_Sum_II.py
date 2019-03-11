"""
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates
where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


#Solution DFS 1

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0 ,target)

    def search(self, candidates, start, target):
        if target==0:
            return [[]]
        res=[]
        for i in xrange(start,len(candidates)):
            if i!=start and candidates[i]==candidates[i-1]:
                continue
            if candidates[i]>target:
                break
            for r in self.search(candidates, i+1, target-candidates[i]):
                res.append([candidates[i]]+r)
        return res

#Solution DFS 2
class Solution:

    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])




#Solution 2 -- DP
class Solution2:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])


class Solution3:
    def combinationSum2(self, candidates, target):
        def backtrack(start, end, tmp, target):
            if target == 0:
                ans.append(tmp[:])
            elif target > 0:
                for i in range(start, end):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    tmp.append(candidates[i])
                    backtrack(i+1, end, tmp, target - candidates[i])
                    tmp.pop()
        ans = []
        candidates.sort(reverse= True)
        backtrack(0, len(candidates), [], target)
        return ans


