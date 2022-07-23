import functools

class Solution:
    def findMax(self, saving, currentValue, futureValue):

        @functools.lru_cache(None)
        def dfs(i, total):
            # print(i, total)

            if i >= len(currentValue):
                return 0
            if total < currentValue[i]:
                return 0

            pick = 0
            if futureValue[i] - currentValue[i] > 0:
                pick = dfs(i+1, total - currentValue[i]) + futureValue[i] - currentValue[i]
            # pick = dfs(i+1, total - currentValue[i]) + futureValue[i] - currentValue[i]
            no_pick = dfs(i+1, total)

            return max(pick, no_pick)

        return dfs(0, saving)


saving = 250
currentValue = [175, 133, 109, 210, 97]
futureValue = [200, 125, 128, 228, 133]

a = Solution()
print(a.findMax(saving, currentValue, futureValue))
