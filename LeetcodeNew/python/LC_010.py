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


s = "aab"
p = "c*a*b"
a = Solution()
print(a.isMatch(s, p))

