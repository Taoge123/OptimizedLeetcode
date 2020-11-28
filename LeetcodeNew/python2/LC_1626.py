
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



