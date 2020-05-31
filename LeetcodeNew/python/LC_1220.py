
"""
https://leetcode.com/problems/count-vowels-permutation/discuss/398286/Simple-Python-(With-Diagram)
https://leetcode.com/problems/count-vowels-permutation/discuss/398222/Detailed-Explanation-using-Graphs-With-Pictures-O(n)
https://www.youtube.com/watch?v=6v7m6SgFEZU

"""

class Solution:
    def count_vowel_permutations(self, n):
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10**9 + 7)


class Solution22:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            # a is allowed to follow e, i, or u.
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            # e is allowed to follow a or i.
            dp[i][1] = dp[i - 1][0] +  dp[i - 1][2]
            # i is allowed to follow e or o.
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            # o is allowed to follow i
            dp[i][3] = dp[i - 1][2]
            # u is allowed to follow i or o.
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
        return sum(dp[n]) % ((10 ** 9) + 7)


class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n + 1)]
        dp[1] = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            # a is allowed to follow e, i, or u.
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            # e is allowed to follow a or i.
            dp[i][1] = dp[i - 1][0] +  dp[i - 1][2]
            # i is allowed to follow e or o.
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            # o is allowed to follow i
            dp[i][3] = dp[i - 1][2]
            # u is allowed to follow i or o.
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]
        return sum(dp[n]) % ((10 ** 9) + 7)