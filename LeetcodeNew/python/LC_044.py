
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


# https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration

"""
B b a r c c b b b 
* c * * * b   
          s j
C a c a
          i
* a
   J
A a a a 
  i
* * * a 
      j
Star = 2
Match = 1

"""


class SolutionTonyTD:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)
        if i > m:
            return False
        if i == m and j == n:
            return True
        if i < m and j == n:
            return False

        first_match = i < m and j < n and (s[i] == p[j] or p[j] == '?')

        res = False
        if j < n and p[j] == '*':
            res = self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 1, memo)

        if first_match:
            res = self.dfs(s, p, i + 1, j + 1, memo)

        memo[(i, j)] = res
        return res



class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0
        match = 0
        star = -1
        while i < len(s):
            ## first case compare ? or whether they are exactly the same
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            ## if there is a * in p we mark current j and i
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                match = i
            ## if current p[j] is not * we check whether prior state has *
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        if j == len(p):
            return True
        return False




class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
            for j in range(1, len(s) + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[-1][-1]


class SolutionTest:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}
        return self.dfs(s, p, 0, 0, memo)

    def dfs(self, s, p, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        m, n = len(s), len(p)
        if i == m and j == n:
            return True
        if i < m and j == n:
            return False
        if i == m and j < n:
            if self.dfs(s, p, i, j + 1, memo):
                memo[(i, j)] = True
                return True

        res = False
        if j < n and p[j] == '*':
            if self.dfs(s, p, i + 1, j, memo) or self.dfs(s, p, i, j + 1, memo):
                res = True

        if i < m and j < n and (p[j] == '?' or s[i] == p[j]):
            if self.dfs(s, p, i + 1, j + 1, memo):
                res = True

        memo[(i, j)] = res
        return res


s = "cdcb"
p = "*c?b"
a = SolutionTest()
print(a.isMatch(s, p))


