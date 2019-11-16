
"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""


class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        cache = set(words)
        res = []
        for word in words:
            if self.dfs(word, cache, res):
                res.append(word)
        return res

    def dfs(self, word, cache, res):
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            if prefix in cache and suffix in cache:
                return True
            if prefix in cache and self.dfs(suffix, cache, res):
                return True
            if suffix in cache and self.dfs(prefix, cache, res):
                return True

        return False


