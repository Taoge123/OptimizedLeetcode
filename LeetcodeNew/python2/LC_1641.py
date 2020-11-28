"""
      a e i o u
1 ->  1 1 1 1 1
2 ->  1 2 3 4 5
3 ->          5+4+3+2+1
            4+3+2+1
          3+2+1
        2+1

a 5 aa ae ai ao au -> 15
e 4 ee ei eo eu    ->
i 3 ii io iu
o 2 oo ou
u 1 uu


a e i o u
1 2 3 4 5

3 ->

dp[1] = 5
dp[2] = 5 + 4 + 3 + 2 + 1 = 15
dp[3] = 15 * a + 14 * e +


X X X X X i-1 i

dp[i][k] : the number of strings of which the ith element is k

"""

"""
X X X X X i-1 i

dp[i][k] : the number of strings of which the ith element is k

"""

import functools


class SolutionDFS1:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, n):
            # found a value solution
            if n == 0:
                return 1
            # Reach to length of vowels [a, e, i, o, u]
            if i == 5:
                return 0
            # skip the vowels
            res = dfs(i + 1, n)
            # include the vowels
            res += dfs(i, n - 1)
            return res
        return dfs(0, n)



"""
f(n, m) is the number of valid strings that are n character long and have its first character picked from "aeiou"[m: ].

For example, f(2, 0) is the number of valid strings that are 2 character long and have its first character picked from "aeiou"[0: ]

if the first character is a, then there are f(1, 0) possibilities: aa, ae, ai, ao, au
if the first character is e, then there are f(1, 1) possibilities: ee, ei, eo, eu
if the first character is i, then there are f(1, 2) possibilities: ii, io, iu
if the first character is o, then there are f(1, 3) possibilities: oo, ou
if the first character is u, then there are f(1, 4) possibilities: u
so f(n, m) = f(n - 1, m) + f(n - 1, m + 1) + ... + f(n - 1, 4).

The state is i,n, i being the vowel we are currently on (0:a,1:e,2:i,3:o,4:u). At each step, we can either use the same vowel, or go to a lexicographically larger vowel. The new state i',n-1 is the vowel we choose to go to, and n-1 because we finished. End state is when i >= 5 (out of vowels) or n == 0, out of letters.

O(n) O(n). If we convert to bottom up DP then we can save some memory, instead of using memoization.

Note: This week's contest last 3 problems all are the same flavor of DP. Know what state you are at, define the recurrence relation by possible moves, then perform the recursion by doing those moves.

"""


class SolutionDFS111:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(i, n):  # i indexes vowels, n is characters remaining
            if i >= 5:
                return 0
            elif n == 0:
                return 1
            else:
                count = 0
                for j in range(i, 5):
                    count += dfs(j, n - 1)
                return count

        return dfs(0, n)


class SolutionDFS11:
    def countVowelStrings(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(n: int, i: int) -> int:
            if i == 5 or n == 0:
                return 0
            elif n == 1:
                return 5 - i
            else:
                return sum(dfs(n - 1, j) for j in range(i, 5))

        return f(n, 0)


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 15

        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = a, a + e, a + e + i, a + e + i + o, a + e + i + o + u
        return a + e + i + o + u






