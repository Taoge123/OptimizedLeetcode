
"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""
import functools


class SolutionTony:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= m:
                return True
            if j >= n:
                return False

            # s move, t move
            if s[i] == t[j]:
                return dfs(i + 1, j + 1)
            # ch does not match, s stay t move
            else:
                return dfs(i, j + 1)

        return dfs(0, 0)



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False

        si, ti = 0, 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
            ti += 1
        return si == len(s)




class SolutionTony:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s):
            if j >= len(t):
                return False
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return True







