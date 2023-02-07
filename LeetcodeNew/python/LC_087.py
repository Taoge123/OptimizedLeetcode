"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false
"""

import functools

class SolutionTony:
    def isScramble(self, s1: str, s2: str) -> bool:

        @functools.lru_cache(None)
        def dfs(s1, s2):
            n = len(s1)
            if s1 == s2:
                return True
            # if not s1 and not s2:
            #     return True
            # if sorted(s1) != sorted(s2):
            #     return False

            for i in range(1, n):
                if (dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:])) or (dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i])):
                    return True
            return False

        return dfs(s1, s2)



class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        memo = {}
        return self.dfs(s1, s2, memo)

    def dfs(self, s1, s2, memo):
        if (s1, s2) in memo:
            return memo[(s1, s2)]

        if sorted(s1) != sorted(s2) or len(s1) != len(s2):
            return False

        if s1 == s2:
            memo[(s1, s2)] = True
            return True

        if not s1 and not s2:
            return True

        for i in range(1, len(s1)):
            if (self.dfs(s1[:i], s2[:i], memo) and self.dfs(s1[i:], s2[i:], memo)) or (
                    self.dfs(s1[:i], s2[-i:], memo) and self.dfs(s1[i:], s2[:-i], memo)):
                memo[(s1, s2)] = True
                return True
        memo[(s1, s2)] = False
        return False







