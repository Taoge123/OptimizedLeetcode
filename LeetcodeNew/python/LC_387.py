
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

import collections

class Solution:
    def firstUniqChar(self, s):

        table = collections.Counter(s)

        ans = -1

        for i, j in enumerate(s):
            if table[j] == 1:
                ans = i
                break

        return ans


