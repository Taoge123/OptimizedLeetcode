
"""
https://www.cnblogs.com/grandyang/p/4743837.html

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
"""
import heapq

# Renat Bekbolatov 2018
class SolutionHeap:
    def nthUglyNumber(self, n):
        q, counted = [1], {1}
        for i in range(n - 1):
            m = heapq.heappop(q)
            for mm in [2*m, 3*m, 5*m]:
                if mm not in counted:
                    heapq.heappush(q, mm)
                    counted.add(mm)
        return heapq.heappop(q)

class SolutionHeap2:
    def nthUglyNumber(self, n):
        heap = [1]
        i = 0
        s = set()
        while i < n:
            e = heapq.heappop(heap)
            if e not in s:
                s.add(e)
                heapq.heappush(heap, e*2)
                heapq.heappush(heap, e*3)
                heapq.heappush(heap, e*5)
                i += 1
        return e

class SolutionCaikehe:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]

    def nthUglyNumber2(self, n):
        ugly = [0] * n
        nxt = ugly[0] = 1
        i2 = i3 = i5 = 0
        nxt2, nxt3, nxt5 = ugly[i2]*2, ugly[i3]*3, ugly[i5]*5
        for i in range(1, n):
            nxt = min(nxt2, nxt3, nxt5)
            ugly[i] = nxt
            if nxt == nxt2:
                i2 += 1
                nxt2 = ugly[i2]*2
            if nxt == nxt3:
                i3 += 1
                nxt3 = ugly[i3]*3
            if nxt == nxt5:
                i5 += 1
                nxt5 = ugly[i5]*5
        return nxt # ugly[-1]


class Solution2:
    def nthUglyNumber(self, n):
        ugly = [1] * n
        primes = [2, 3, 5]
        i = [-1] * 3
        v = [1] * 3
        for k in range(n):
            ugly[k] = min(v)
            for j in range(3):
                if v[j] == ugly[k]:
                    i[j] += 1
                    v[j] = ugly[i[j]] * primes[j]
        return ugly[-1]






