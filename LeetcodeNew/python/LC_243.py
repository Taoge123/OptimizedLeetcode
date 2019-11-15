"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

"""


class Solution:
    def shortestDistance(self, words, word1: str, word2: str) -> int:

        n = len(words)
        res = float('inf')
        index1, index2 = float('inf') ,float('inf')
        for i in range(n):
            if words[i] == word1:
                index1 = i
                res = min(res, abs(index2 - index1))
            elif words[i] == word2:
                index2 = i
                res = min(res, abs(index2 - index1))
        return res




