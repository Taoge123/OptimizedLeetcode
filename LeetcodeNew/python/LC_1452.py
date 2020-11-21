
class Solution:
    def peopleIndexes(self, favoriteCompanies):
        nums = [set(num) for num in favoriteCompanies]
        n = len(favoriteCompanies)
        dp = [True for i in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                # nums[i] is a subset
                if nums[i] & nums[j] == nums[i]:
                    dp[i] = False
                # nums[j] is a subset
                elif nums[i] & nums[j] == nums[j]:
                    dp[j] = False

        res = []
        for i in range(n):
            if dp[i]:
                res.append(i)
        return res

