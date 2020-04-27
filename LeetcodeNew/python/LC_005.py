"""
https://www.youtube.com/watch?v=YVZttWzvyw8
https://www.youtube.com/watch?v=SV1ZaKCozS4
https://www.youtube.com/watch?v=kbUiR5YWUpQ


Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

"""


class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring
    def longestPalindrome(self, s):
        # Transform S into T.

        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]



class Solution1:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(set(s)) == 1:
            return s

        n = len(s)
        maxi, res = 0, 0

        dp = [[0] * n for i in range(n)]

        for j in range(n):
            dp[j][j] = 1
            for i in range(j):
                # print('[', i, ']', '[', j, ']', '+', '[',i+1,']', '[',j-1,']')
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and maxi < j - i + 1:
                    maxi = j - i + 1
                    res = s[i: j + 1]

        for i in dp:
            print(i)
        return res if res else s[0]



class Solution2:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)

        return res

    def helper(self, s, l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


class Solution22:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        res = ""
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            res = tmp if len(tmp) > len(res) else res
            tmp = self.helper(s, i, i + 1)
            res = tmp if len(tmp) > len(res) else res
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]



"""
[ 0 ] [ 1 ] + [ 1 ] [ 0 ]
[ 0 ] [ 2 ] + [ 1 ] [ 1 ]
[ 1 ] [ 2 ] + [ 2 ] [ 1 ]
[ 0 ] [ 3 ] + [ 1 ] [ 2 ]
[ 1 ] [ 3 ] + [ 2 ] [ 2 ]
[ 2 ] [ 3 ] + [ 3 ] [ 2 ]
[ 0 ] [ 4 ] + [ 1 ] [ 3 ]
[ 1 ] [ 4 ] + [ 2 ] [ 3 ]
[ 2 ] [ 4 ] + [ 3 ] [ 3 ]
[ 3 ] [ 4 ] + [ 4 ] [ 3 ]


 b  a  b  a  d
[1, F, 1, F, F]
[0, 1, F, 1, F]
[0, 0, 1, F, F]
[0, 0, 0, 1, F]
[0, 0, 0, 0, 1]
 
 a  b  b  b  b  c  a  d
[1, F, F, F, F, F, F, F]
[0, 1, T, 1, T, F, F, F]
[0, 0, 1, T, 1, F, F, F]
[0, 0, 0, 1, T, F, F, F]
[0, 0, 0, 0, 1, F, F, F]
[0, 0, 0, 0, 0, 1, F, F]
[0, 0, 0, 0, 0, 0, 1, F]
[0, 0, 0, 0, 0, 0, 0, 1]
"""



s = "abbbbcad"
a = Solution2()
print(a.longestPalindrome(s))













