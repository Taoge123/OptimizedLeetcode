
import functools


class SolutionTD:
    def bestTeamScore(self, scores, ages):
        nums = list(zip(ages, scores))
        nums.sort()
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, max_age, max_score):
            # i represent index of nums, max_score represent max score until i-1 index in nums
            # and max_age represent max age until i-1 index
            if i == n:
                return 0

            res = 0
            for j in range(i, n):
                cur_age, cur_score = nums[j]
                if cur_score > max_score or (cur_score == max_score and max_age <= cur_age):
                    res = max(res, cur_score + dfs(j + 1, cur_age, cur_score))
            return res

        return dfs(0, 0, 0)


class SolutionTD1:
    def bestTeamScore(self, scores, ages) -> int:
        n = len(scores)
        nums = []
        for i in range(n):
            nums.append([scores[i], ages[i]])
        nums = sorted(nums, key=lambda x: (-x[0], -x[1]))

        # print(nums)
        @functools.lru_cache(None)
        def dfs(i, prevMax):
            if i >= len(nums):
                return 0
            res = dfs(i + 1, prevMax)
            if prevMax >= nums[i][1]:
                res = max(res, nums[i][0] + dfs(i + 1, nums[i][1]))
            return res

        return dfs(0, 1000)



class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        nums = sorted(zip(ages, scores))
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            dp[i] = nums[i][1]
            for j in range(i):
                if nums[j][1] <= nums[i][1]:
                    dp[i] = max(dp[i], dp[j] + nums[i][1])
        return max(dp)


class Solution11:
    def bestTeamScore(self, scores, ages) -> int:
        nums = sorted(zip(ages, scores))
        n = len(nums)
        dp = [i[1] for i in nums]

        for i in range(1, n):
            dp[i] = nums[i][1]
            for j in range(i):
                if nums[j][1] <= nums[i][1]:
                    dp[i] = max(dp[i], dp[j] + nums[i][1])
        return max(dp)


class Solution2:
    def bestTeamScore(self, scores, ages) -> int:
        nums = sorted(zip(scores, ages))
        n = len(nums)
        dp = [i[0] for i in nums]
        for i in range(1, n):
            for j in range(i):
                if nums[j][1] <= nums[i][1]:
                    dp[i] = max(dp[i], dp[j] + nums[i][0])
        return max(dp)



