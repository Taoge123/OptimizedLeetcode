"""
https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/solution/tong-ji-zhi-chai-yi-ge-zi-fu-de-zi-chuan-shu-mu-by/
https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/solution/dong-tai-gui-hua-zui-hou-qiu-dpshu-zu-suo-you-yuan/



dp[i][j] : the number of ways s[0:i], t[0:j]

X X X [Z Z i]
Y Y [Z Z j]
(i, j) : 3*4 = 12

for i in ...:
    for j in ...:
        a = left(i, j)
        b = right(i, j)
        res += (a+1) * (b+1)


以i, j为截止最长公共子区间
if (s[i] == s[j]):
    dp[i][j] = dp[i-1][j-1]
else:
    dp[i][j] = 0


we can use DP to solve this problem
dp(i, j, k) means the number of substrings ending at a[i] and t[j] and differed by k (0 or 1) character


"""



import functools


class SolutionWisdom:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        s = '#' + s + '#'
        t = '#' + t + '#'

        dp1 = [[0 for i in range(105)] for j in range(105)]
        dp2 = [[0 for i in range(105)] for j in range(105)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == t[j]:
                    dp1[i][j] = dp1[i - 1][j - 1] + 1
                else:
                    dp1[i][j] = 0

        for i in range(m, 1, -1):
            for j in range(n, 1, -1):
                if s[i] == t[j]:
                    dp2[i][j] = dp2[i + 1][j + 1] + 1
                else:
                    dp2[i][j] = 0

        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] != t[j]:
                    res += (dp1[i - 1][j - 1] + 1) * (dp2[i + 1][j + 1] + 1)

        return res




class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @functools.lru_cache(None)
        def dp(i, j, k):
            # base cases
            if i < 0 or j < 0 or k < 0:
                return 0
            if k == 0 and s[i] != t[j]:
                return 0

            # dp transition
            res = 0
            if s[i] == t[j]:
                res += dp(i - 1, j - 1, k) + (k == 0)
            else:
                res += dp(i - 1, j - 1, k - 1) + 1
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                res += dp(i, j, 1)
        return res







