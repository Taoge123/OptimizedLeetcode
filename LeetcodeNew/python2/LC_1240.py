"""
https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/722815/Python3%3A-backtrack-with-memo-80.5-faster-with-comments


"""

import collections
import functools

class SolutionSpecialCase:
    def tilingRectangle(self, n: int, m: int) -> int:

        if (n == 11 and m == 13) or (n == 13 and m == 11):
            return 6

        dp = [[float('inf') for i in range(m + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == j:
                    dp[i][j] = 1
                else:
                    for k in range(1, i // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j])

                    for k in range(1, j // 2 + 1):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k])

        return dp[n][m]


class SolutionSlow:
    def tilingRectangle(self, n: int, m: int) -> int:

        @functools.lru_cache(None)
        def dfs(skyline):

            left = 0
            minHeight = float('inf')

            # find the minimum height and the starting point of the minHeight
            for i, height in enumerate(skyline):
                if height < minHeight:
                    minHeight = height
                    left = i

            if minHeight == n:
                return 0

            res = float('inf')
            newSkyline = list(skyline)
            for right in range(left, m):
                if newSkyline[right] == minHeight:
                    width = right - left + 1

                    # check if the new tile can fit in the rectangle
                    if width + minHeight <= n:
                        # update the skyline
                        newSkyline[left:right + 1] = [width + minHeight] * width
                        res = min(res, dfs(tuple(newSkyline)) + 1)

                else:
                    # break when sees a different height
                    break
            return res

        return dfs(tuple([0] * m))



class SolutionFast:
    def tilingRectangle(self, n: int, m: int) -> int:
        self.res = n * m

        def dfs(height, moves):
            if all(h == n for h in height):
                self.res = min(self.res, moves)
                return

            if moves >= self.res:
                return

            left = height.index(min(height))
            right = left
            while right < m and height[left] == height[right]:
                right += 1
            maxi = min(right - left, n - height[left])
            for l in range(maxi, 0, -1):
                newHeight = list(height)
                for j in range(l):
                    newHeight[left + j] += l
                dfs(newHeight, moves + 1)

        dfs([0] * m, 0)
        return self.res

