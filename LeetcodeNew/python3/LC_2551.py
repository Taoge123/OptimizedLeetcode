import functools


class SolutionRika:
    def putMarbles(self, nums, k: int) -> int:
        n = len(nums)

        @functools.lru_cache(None)
        def dfs(i, k):
            if i == n and k == 0:
                return 0, 0

            if i == n or k == 0:
                return float('-inf'), float('inf')  # max, min

            maxi = float('-inf')
            mini = float('inf')
            for j in range(i, n):
                # if j - i + 1 > k:
                #    continue
                cost = nums[j] + nums[i]
                # 区间dp，下一步从下一个区间开始
                maxx, minn = dfs(j + 1, k - 1)
                maxi = max(maxi, maxx + cost)
                mini = min(mini, minn + cost)

            return maxi, mini

        maxx, minn = dfs(0, k)
        return maxx - minn


class SolutionTony:
    def putMarbles(self, weights, k: int) -> int:

        n = len(weights)
        @functools.lru_cache(None)
        def maxi(i, j, k):
            if j >= n and k < 0:
                return 0
            if j >= n or k < 0:
                return float('-inf')

            same = maxi(i, j + 1, k)
            nxt = maxi(j + 1, j + 1, k - 1) + weights[j] + weights[i]
            return max(same, nxt)

        @functools.lru_cache(None)
        def mini(i, j, k):
            if j >= n and k < 0:
                return 0
            if j >= n or k < 0:
                return float('inf')

            same = mini(i, j + 1, k)
            nxt = mini(j + 1, j + 1, k - 1) + weights[j] + weights[i]
            return min(same, nxt)

        a = maxi(0, 0, k)
        b = mini(0, 0, k)
        return a - b






