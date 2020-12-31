"""
https://www.youtube.com/watch?v=UeuV-6Ygxs4&t=32s

218
715
"""


class Solution:
    def fallingSquares(self, positions):
        dp = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            dp[i] += size
            for j in range(i + 1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2:  # intersect
                    dp[j] = max(dp[j], dp[i])

        res = []
        for x in dp:
            res.append(max(res[-1], x) if res else x)
        return res




