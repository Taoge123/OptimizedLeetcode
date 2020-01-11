
"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""


class Solution:
    def findLongestWord(self, s: str, d) -> str:
        res = ''
        for cand in d:
            if self.isSubsequence(s, cand) and (len(cand) > len(res)
                         or (len(cand) == len(res) and cand < res)):
                res = cand
        return res

    def isSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            i += 1
        return j == len(t)


class Solution1:
    def findLongestWord(self, s: str, d) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            if self.check(s, word):
                return word
        return ""

    def check(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            i += 1
        return j == len(t)



class Solution2:
    def findLongestWord(self, s: str, d) -> str:
        d.sort(key=lambda x: (-len(x), x))
        for word in d:
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
            if i == len(word):
                return word
        return ""



