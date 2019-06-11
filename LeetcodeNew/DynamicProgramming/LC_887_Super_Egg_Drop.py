
"""
https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn

You are given K eggs, and you have access to a building with N floors from 1 to N.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break,
and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is,
regardless of the initial value of F?

Example 1:

Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4

Note:

1 <= K <= 100
1 <= N <= 10000
"""

"""
Drop eggs is a very classical problem.
Some people may come up with idea O(KN^2)
where dp[K][N] = 1 + max(dp[K - 1][i - 1],dp[K][N - i]) for i in 1...N.
However this idea is very brute force, for the reason that you check all possiblity.

So I consider this problem in a different way:
dp[M][K]means that, given K eggs and M moves,
what is the maximum number of floor that we can check.

The dp equation is:
dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
which means we take 1 move to a floor,
if egg breaks, then we can check dp[m - 1][k - 1] floors.
if egg doesn't breaks, then we can check dp[m - 1][k - 1] floors.

dp[m][k] is similar to the number of combinations and it increase exponentially to N

Time Complexity:
For time, O(NK) decalre the space, O(KlogN) running,
For space, O(NK).

"""

class SolutionLee1:
    def superEggDrop(self, K, N):
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][K] >= N: return m


"""
Optimized to 1D DP

Time Complexity:
C++/Java O(KlogN) Time, O(K) Space
Python O(min(K, logN)^2) Time, O(min(K, logN)) Space
"""

class Solution2Lee2:
    def superEggDrop(self, K, N):
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp) - 1, 0, - 1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m


"""
The dp equation is:
dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1,
assume, dp[m-1][k-1] = n0, dp[m-1][k] = n1
the first floor to check is n0+1.
if egg breaks, F must be in [1,n0] floors, we can use m-1 moves and k-1 eggs to find out F is which one.
if egg doesn't breaks and F is in [n0+2, n0+n1+1] floors, we can use m-1 moves and k eggs to find out F is which one.
So, with m moves and k eggs, we can find out F in n0+n1+1 floors, whichever F is.
"""

"""
If we know the maximum height of building for which we can learn the highest floor 
that an egg can be dropped from without breaking for a certain number of drops (d) and a certain number of eggs (e). Call this f(d, e).
We also know the same result for the same number of drops and one fewer egg = f(d, e - 1).

Now we take an additional drop from floor f(d, e - 1) + 1.
If it breaks, we know that we can find the result with one less egg f(d, e - 1).
If it doesn't break, we can explore the f(d, e) floors above the one we just dropped from.
So we can get the result for a building of height 1 + f(d, e - 1) + f(d, e).

Time complexity is O(K * drops), but is there a bound on drops in terms of N and K?
"""

class Solution2:
    def superEggDrop(self, K, N):
        drops = 0                           # the number of eggs dropped
        floors = [0 for _ in range(K + 1)]  # floors[i] is the number of floors that can be checked with i eggs

        while floors[K] < N:                # until we can reach N floors with K eggs

            for eggs in range(K, 0, -1):
                floors[eggs] += 1 + floors[eggs - 1]
            drops += 1

        return drops



