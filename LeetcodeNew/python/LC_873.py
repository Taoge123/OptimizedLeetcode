
"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/discuss/233537/Python-detailed-explanation-evolution-from-O(n3)-to-O(n2)-(DP)

Solution 1
Save array A to a hash set s.
Start from base (A[i], A[j]) as the first two element in the sequence,
we try to find the Fibonacci like subsequence as long as possible,

Initial (a, b) = (A[i], A[j])
While the set s contains a + b, we update (a, b) = (b, a + b).
In the end we update the longest length we find.

Time Complexity:
O(N^2logM), where M is the max(A).

Quote from @renato4:
Just clarifying a little bit more.
Since the values grow exponentially,
the amount of numbers needed to accommodate a sequence
that ends in a number M is at most log(M).

"""

import collections


class SolutionHuahua:
    def lenLongestFibSubseq(self, A) -> int:
        table = {val: i for i, val in enumerate(A)}
        n = len(A)
        res = 0
        dp = [[2 for i in range(n)] for j in range(n)]
        for j in range(n):
            for k in range(j + 1, n):
                diff = A[k] - A[j]
                # Pruning
                if diff >= A[j]:
                    break
                if diff not in table:
                    continue
                i = table[diff]
                dp[j][k] = dp[i][j] + 1
                res = max(res, dp[j][k])
        return res





class Solution:
    def lenLongestFibSubseq(self, A) -> int:
        nums = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                temp = 2

                while a + b in nums:
                    a, b = b, a + b
                    temp += 1

                res = max(res, temp)

        if res > 2:
            return res
        else:
            return 0



class SolutionCS:
    def lenLongestFibSubseq(self, A) -> int:
        visited = set()
        for num in A:
            visited.add(num)

        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                size = 2
                while a + b in visited:
                    a, b = b, a + b
                    size += 1
                res = max(res, size)

        return res if res > 2 else 0



"""
Solution 2
Another solution is kind of dp.
dp[a, b] represents the length of fibo sequence ends up with (a, b)
Then we have dp[a, b] = (dp[b - a, a] + 1 ) or 2
The complexity reduce to O(N^2).
In C++/Java, I use 2D dp and index as key.
In Python, I use value as key.

Time Complexity:
O(N^2)"""


class SolutionDPLee:
    def lenLongestFibSubseq(self, A) -> int:
        dp = collections.defaultdict(int)
        nums = set(A)
        for j in range(len(A)):
            for i in range(j):
                a = A[i]
                b = A[j]

                if b - a < a and b - a in nums:
                    dp[a, b] = dp.get((b - a, a), 2) + 1

        return max(dp.values() or [0])



class SolutionDP2:
    def lenLongestFibSubseq(self, A) -> int:
        table = {val: i for i, val in enumerate(A)}

        n = len(A)
        dp = [[2 for i in range(n + 1)] for j in range(n + 1)]

        for j in range(n):
            for i in range(j):
                diff = A[j] - A[i]
                if diff in table and table[diff] < i:
                    val = table[diff]
                    dp[i][j] = max(dp[i][j], dp[val][i] + 1)

        res = max([max(row) for row in dp])
        if res <= 2:
            return 0
        else:
            return res





