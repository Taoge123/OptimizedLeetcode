
"""
https://www.youtube.com/watch?v=a7TLEVdqg0Q
https://www.youtube.com/watch?v=qkgpaVprCZ8
"""


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









