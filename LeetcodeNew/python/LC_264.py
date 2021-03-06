"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1

        i2, i3, i5 = 0, 0, 0
        for i in range(1, len(dp)):
            n2, n3, n5 = dp[i2] * 2, dp[i3] * 3, dp[i5] * 5

            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                i2 += 1
            if dp[i] == n3:
                i3 += 1
            if dp[i] == n5:
                i5 += 1

        return dp[-1]


class Solution2:
    def nthUglyNumber(self, n):
        h = [(1, 1)]
        for _ in range(n):
            val, fact = heapq.heappop(h)
            for x in 2, 3, 5:
                if fact <= x:
                    heapq.heappush(h, (val * x, x))
        return val


class SolutionTest:
    def nthUglyNumber(self, n):
        heap = [(1, 1)]
        for i in range(n):
            num, step = heapq.heappop(heap)
            if step <= 2:
                heapq.heappush(heap, [num * 2, 2])
            if step <= 3:
                heapq.heappush(heap, [num * 3, 3])
            if step <= 5:
                heapq.heappush(heap, [num * 5, 5])
        return num


n = 10
a = SolutionTest()
print(a.nthUglyNumber(n))



