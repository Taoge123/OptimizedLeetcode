

"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""

class Solution:
    def palindromePairs(self, words):
        table, r = dict(map(reversed, enumerate(words))), set()
        for i, word in enumerate(words):
            for k in range(len(word) + 1):
                a, b = word[:k], word[k:]

                if a == a[::-1] and table.get(b[::-1], -1) not in [-1, i]:
                    r.add((table[b[::-1]], i))

                if b == b[::-1] and table.get(a[::-1], -1) not in [-1, i]:
                    r.add((i, table[a[::-1]]))

        return list(r)









