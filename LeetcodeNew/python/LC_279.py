"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""

import collections, math

class Solution:
    def numSquares(self, n):
        dp = [n ] *(n +1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            j = 1
            while j * j <= i:
                print(i, j * j)
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


class Solution2:
    def numSquares(self, n):
        queue = collections.deque([0])
        visited = set()
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for i in range(size):
                val = queue.popleft()
                for i in range(1, int(math.sqrt(n) + 1)):
                    j = val + i * i
                    if j > n:
                        break
                    if j == n:
                        return step
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)



n = 13
a = Solution()
print(a.numSquares(n))


