"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
Notes:
You may assume both pattern and str contains only lowercase letters.

"""


class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        res = {}
        return self.dfs(pattern, str, res)

    def dfs(self, pattern, str, dict):
        p, s = len(pattern), len(str)
        if p == 0 and s == 0:
            return True
        if p == 0:
            return False

        for i in range(1, s - p + 2):
            print(str)
            if pattern[0] not in dict and str[:i] not in dict.values():
                dict[pattern[0]] = str[:i]
                if self.dfs(pattern[1:], str[i:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and str[:i] == dict.get(pattern[0]):
                if self.dfs(pattern[1:], str[i:], dict):
                    return True

        return False




