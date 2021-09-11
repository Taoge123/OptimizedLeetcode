"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

"""

"""
jhbdsjhcds
          a*
"""


class SolutionTD:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def match(self, s, p, i, j):
        if i == len(s) or j == len(p):
            return False

        return s[i] == p[j] or p[j] == '.'

    def dfs(self, s, p, i, j, memo):

        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)
        if i == m and j == n:
            return True

        if j < n - 1 and p[j + 1] == '*':
            if (self.match(s, p, i, j) and self.dfs(s, p, i + 1, j, memo)) or self.dfs(s, p, i, j + 2, memo):
                memo[(i, j)] = True
                return True

        if self.match(s, p, i, j):
            if self.dfs(s, p, i + 1, j + 1, memo):
                memo[(i, j)] = True
                return True

        memo[(i, j)] = False
        return False



class SolutionTD2:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        m, n = len(s), len(p)
        if j == n:
            return i == m

        if (i, j) in memo:
            return memo[(i, j)]

        first_match = i != m and (s[i] == p[j] or p[j] == '.')
        res = False
        if j < n - 1 and p[j + 1] == '*':
            res = (first_match and self.dfs(s, p, i + 1, j, memo)) or self.dfs(s, p, i, j + 2, memo)
        else:
            res = first_match and self.dfs(s, p, i + 1, j + 1, memo)

        memo[(i, j)] = res
        return res



class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        M = [[False for x in range(m + 1)] for y in range(n + 1)]
        M[0][0] = True

        for j in range(2, m + 1):
            if p[j - 1] == "*":
                M[0][j] = M[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == ".":
                    M[i][j] = M[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if M[i][j - 2] or M[i][j - 1] or ((p[j - 2] == "." or p[j - 2] == s[i - 1]) and M[i - 1][j]):
                        M[i][j] = True
                else:
                    M[i][j] = M[i - 1][j - 1] and p[j - 1] == s[i - 1]
        print(M)
        return M[n][m]


class Solution:
    def isMatch(self, s, p):
        n = len(s)
        m = len(p)

        M = [[False for x in range(m + 1)] for y in range(n + 1)]
        M[0][0] = True

        for j in range(2, m + 1):
            if p[j - 1] == "*":
                M[0][j] = M[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    M[i][j] = M[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if M[i][j - 2] or M[i][j - 1] or ((p[j - 2] == "." or p[j - 2] == s[i - 1]) and M[i - 1][j]):
                        M[i][j] = True
                # else:
                #     M[i][j] = M[i - 1][j - 1] and p[j - 1] == s[i - 1]
        print(M)
        return M[n][m]


s = "aa"
p = "a*"
a = SolutionTD()
print(a.isMatch(s, p))

