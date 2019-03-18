
"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.


"""
import math
import collections

class Solution:
    def minSquare(self, n):

        square = [i * i for i in range(1, int(math.sqrt(n)) + 1)]  # Square numbers <= n
        level = 0  # BFS level
        currentLevel = [0]  # List of numbers in BFS level l

        while True:
            nextLevel = []
            for a in currentLevel:
                for b in square:
                    if a + b == n:
                        return level + 1  # Found n
                    if a + b < n:
                        nextLevel.append(a + b)
            currentLevel = list(set(nextLevel))  # Remove duplicates
            level += 1


class Solution2:
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft()
            step += 1
            for j in range(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))


class SolutionCaikehe:
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            val, dis = queue.popleft()
            # if val == n:
            #     return dis
            for i in range(1, n+1):
                j = val + i*i
                if j > n:
                    break
                if j == n:
                    return dis+1
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dis+1))



class Solution3:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n+1)
        for i in range(1, int(n**0.5)+1):
            dp[i**2] = 1

        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-k**2]+1)

        return dp[n]







