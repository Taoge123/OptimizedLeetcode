"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""



import collections

class Solution:
    def findAnagrams(self, s: str, p: str):

        res = []

        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p ) -1])

        for i in range(len(p ) -1, len(s)):
            head = i- len(p) + 1

            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i - len(p) + 1)
            sCounter[s[head]] -= 1
            if sCounter[s[head]] == 0:
                del sCounter[s[head]]
        return res

s = "cbaebabacd"
p = "abc"
a = Solution()
print(a.findAnagrams(s, p))

