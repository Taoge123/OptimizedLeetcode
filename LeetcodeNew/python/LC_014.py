"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''

        for i in range(len(strs[0])):
            for j in strs:
                if len(j) <= i or strs[0][i] != j[i]:
                    return strs[0][:i]

        return strs[0]

