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


class Solution:
    def maxProduct(self, words) -> int:
        byte = {}
        for word in words:
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            byte[mask] = max(byte.get(mask, 0), len(word))

        res = 0
        for x in byte:
            for y in byte:
                if not x & y:
                    res = max(res, byte[x] * byte[y])
        return res



words = ["abcw","baz","foo","bar","xtfn","abcdef"]
a = Solution()
print(a.maxProduct(words))


