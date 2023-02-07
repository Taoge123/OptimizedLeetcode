"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


"""
val != 1 << (words[i][j] - 'a')

1 << 0 00001 = 1 a
1 << 1 00010 = 2 b
1 << 2 00100 = 4 c
1 << 3 01000 = 8

abc = 00111 = 7
ab  = 00011 = 3

bytes[i] & bytes[j] == 0

00111
11000
00000

"""

import collections

class SolutionTony:
    def maxProduct(self, words) -> int:
        byte = collections.defaultdict(int)
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))
            byte[mask] = max(byte[mask], len(word))

        res = 0
        for x in byte:
            for y in byte:
                if x & y == 0:
                    res = max(res, byte[x] * byte[y])
        return res


class SolutionTLE:
    def maxProduct(self, words) -> int:
        n = len(words)
        res = 0

        for i in range(n):
            for j in range(i+1, n):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
a = Solution()
print(a.maxProduct(words))


