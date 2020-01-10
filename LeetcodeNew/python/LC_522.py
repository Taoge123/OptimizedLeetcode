
"""
Given a list of strings, you need to find the longest uncommon subsequence among them.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters
without changing the order of the remaining elements. Trivially,
any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""


class Solution:
    def findLUSlength(self, strs) -> int:
        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not self.isSubsequence(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1

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



strs = ["aba", "cdc", "eae"]
a = Solution()
print(a.findLUSlength(strs))


