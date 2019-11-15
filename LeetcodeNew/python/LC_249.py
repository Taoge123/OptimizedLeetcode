"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

"""

import collections

class Solution:
    def groupStrings(self, strings):

        table = collections.defaultdict(list)

        for string in strings:
            key = ""
            for i in range(len(string) - 1):
                diff = str((ord(string[ i +1]) - ord(string[i])) % 26)
                key += diff
            table[key].append(string)
        return table.values()





