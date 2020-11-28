"""
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/371864/Python-Find-all-Sub-Puzzles
"""

import collections


class Solution:
    def findNumOfValidWords(self, words, puzzles):
        count = collections.Counter()
        for word in words:
            if len(set(word)) > 7:
                continue

            mask = 0
            for char in word:
                mask |= 1 << (ord(char) - 97)
            count[mask] += 1

        res = []
        for p in puzzles:
            queue = [1 << (ord(p[0]) - 97)]
            for char in p[1:]:
                queue += [mask | 1 << (ord(char) - 97) for mask in queue]

            res.append(sum(count[mask] for mask in queue))

        return res


class Solution2:
    def findNumOfValidWords(self, words, puzzles):

        count = collections.Counter(frozenset(w) for w in words)
        res = []

        for p in puzzles:
            queue = [p[0]]
            for char in p[1:]:
                queue += [node + char for node in queue]
            print(queue)
            res.append(sum(count[frozenset(node)] for node in queue))
        return res


words = ["aaaa","asas","able","ability","actt","actor","access"],
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]

a = Solution()
print(a.findNumOfValidWords(words, puzzles))


