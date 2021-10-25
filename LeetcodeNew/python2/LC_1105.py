
"""
https://www.youtube.com/watch?v=a7TLEVdqg0Q
https://www.youtube.com/watch?v=qkgpaVprCZ8
"""

import functools


class SolutionTony:
    def minHeightShelves(self, books, shelf_width):
        n = len(books)

        @functools.lru_cache(None)
        def dfs(i, h, w):
            if w < 0:
                return float('inf')
            if i >= n:
                return h

            w1, h1 = books[i]
            add_curr = dfs(i + 1, max(h1, h), w - w1)
            add_new = dfs(i + 1, h1, shelf_width - w1) + h
            return min(add_curr, add_new)

        return dfs(0, 0, shelf_width)



class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:

        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            maxHeight = 0
            widthLeft = shelf_width
            for j in range(i - 1, -1, -1):
                widthLeft -= books[j][0]
                #Optimization
                if widthLeft < 0:
                    break
                maxHeight = max(maxHeight, books[j][1])

                if widthLeft >= 0:
                    dp[i] = min(dp[i], dp[j] + maxHeight)

        return dp[-1]



class Solution2:
    def minHeightShelves(self, books, shelf_width: int) -> int:

        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            maxHeight = 0
            totalWeight = 0
            for j in range(i - 1, -1, -1):
                totalWeight += books[j][0]
                if totalWeight > shelf_width:
                    break
                maxHeight = max(maxHeight, books[j][1])
                if totalWeight >= 0:
                    dp[i] = min(dp[i], dp[j] + maxHeight)

        return dp[-1]






