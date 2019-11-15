"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.



Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

"""


import collections
class Solution:
    def findSubstring(self, s: str, words):
        if not words: return []
        k = len(words[0])
        res = []

        for left in range(k):
            d = collections.Counter(words)

            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                d[word] -= 1

                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k

                if left + k * len(words) == right:
                    res.append(left)
        return res

