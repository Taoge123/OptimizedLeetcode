"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

import collections

class SolutionTony:
    def groupAnagrams(self, strs):
        table = collections.defaultdict(list)
        for word in strs:
            # print(word)
            word_key = "".join(sorted(word))
            table[word_key].append(word)

        res = []
        for k, val in table.items():
            res.append(val)
        return res



class Solution:
    def groupAnagrams(self, strs):

        table = {}

        for word in strs:
            word_key = "".join(sorted(word))

            if word_key not in table:
                table[word_key] = [word]
            else:
                table[word_key].append(word)

        result = []
        for value in table.values():
            result += [value]

        return result



