"""
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:
There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""

import collections


class Solution:
    def wordSquares(self, words):
        res = []
        table = collections.defaultdict(set)
        for word in words:
            for i in range(len(word)):
                table[word[:i]].add(word)
        for word in words:
            self.dfs(table, word, 1, [], res)
        return res

    def dfs(self, table, word, index, path, res):
        path.append(word)
        if index == len(word):
            res.append(path[:])
        else:
            prefix = "".join(path[i][index] for i in range(index))
            for word in table[prefix]:
                self.dfs(table, word, index + 1, path, res)
        path.pop()


"""
ie, when index == 2:
LEA will be the prefix, then we will search LEA in table and continue to backtrack

[[ "w a L l",
   "a r E a",
   "l e A d",
   "l a d y"],


["ball","area","lead","lady"]]

"""

words = ["area","lead","wall","lady","ball"]
a = Solution()
print(a.wordSquares(words))



