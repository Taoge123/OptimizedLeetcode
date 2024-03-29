"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

"""

import functools

class SolutionTony:
    def partition(self, s: str):

        res = []
        return self.dfs(s, 0, [], res)

    def dfs(self, s, i, path, res):
        @functools.lru_cache(None)
        def isPal(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            if s[i] == s[j]:
                return isPal(i + 1, j - 1)

        n = len(s)
        if i == n:
            res.append(path)
            return

        for j in range(i, n):
            if isPal(i, j):
                self.dfs(s, j + 1, path + [s[i:j + 1]], res)
        return res


class Solution:
    def partition(self, s):

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)

    def isPar(self, s):
        return s == s[::-1]


class Solution2:
    def partition(self, s):
        res = []
        self.dfs(s, [], 1, res)
        return res

    def dfs(self, s, path, index, res):
        if index == len(s) + 1:
            res.append(path[:])
            return
        for i in range(index, len(s) + 1):
            if self.isPalindrome(s[index - 1:i]):
                path.append(s[index - 1:i])
                self.dfs(s, path, i + 1, res)
                path.pop()

    def isPalindrome(self, s):
        return s == s[::-1]




