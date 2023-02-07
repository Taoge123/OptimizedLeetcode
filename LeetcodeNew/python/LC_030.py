"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.



Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

"""


import collections
import copy


class SolutionTony:
    def findSubstring(self, s: str, words):
        m, n = len(words), len(words[0])
        table = collections.defaultdict(int)
        for i, word in enumerate(words):
            table[word] += 1
        res = []
        for i in range(len(s) - m * n + 1):
            temp = copy.deepcopy(table)
            count = 0
            for j in range(i, len(s), n):
                # print(i, j)
                word = s[j:j + n]
                if word not in temp or temp[word] <= 0:
                    break
                temp[word] -= 1
                count += 1
                if count == m:
                    res.append(i)
        return res



class Solution:
    def findSubstring(self, s: str, words):
        if not words:
            return []
        k = len(words[0])
        res = []

        for left in range(k):
            d = collections.Counter(words)

            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                d[word] -= 1

                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k

                if left + k * len(words) == right:
                    res.append(left)
        return res


class Solution1:
    def findSubstring(self, s: str, words):
        if not words: return []
        k = len(words[0])
        res = []

        # [aaa]bbbccc, then a[aab]bbccc, then aa[abb]bccc
        for left in range(k):
            # Init counter
            d = collections.Counter(words)

            # For first iteration of left:
            # Iterate through each [aaa]{b}bbccc, then [aaa]bbb{c}cc, then [aaa]bbbccc{}
            for right in range(left + k, len(s) + 1, k):
                # Grab the preceding word: aaa, then bbb, then ccc
                word = s[right - k: right]
                d[word] -= 1

                # If a word is seen that shouldn't have been seen before,
                # Push left all the way up until it hits right
                # Anything we've seen before is skipped
                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k

                # If, however, we don't push left, and we've explored enough
                # that our window is the size of the words we need to find,
                # we have a winner!
                if left + k * len(words) == right:
                    res.append(left)
        return res




# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]

a = Solution3()
print(a.findSubstring(s, words))

