"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.

"""

import collections

class Solution:
    def isIsomorphic(self, s, t):

        table = collections.defaultdict(str)

        for i, j in zip(s, t):
            if i in table:
                if table[i] != j:
                    return False
            else:
                if j in table.values():
                    return False
                else:
                    table[i] = j

        return True


