
"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
import collections
import copy

class SolutionLee:
    def findSubstring(self, s, words):
        if not words: return []
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

"""
Solution

Substring with Concatenation of All Words https://leetcode.com/problems/substring-with-concatenation-of-all-words/

Two Pointer Sliding Window

- Say length of each word is wl and we have wc words. total_len of substring = wl * wc
- Two pointer sliding window solution. Initialize a window [start, end] = [0, total_len-1]
- Now we slide through s and capture every substring. We then test if this substring is valid and meets our conditions.
- We prepare a frequency map of input words. We call it ctr.
- We initialize a dictionary called seen.
- Now we pick every word (called next_word) sequentially in our window. Note there will be only wc words each of length wl.
- If next_word is not in ctr then we know the window is invalid. If it is, but the frequency in seen is already equal to the frequency in ctr, 
  then we know we have an extra occurence of this word in the window and the window is invalid. Otherwise, we increment its frequency in seen.
- If every word in this window is valid, then the entire window is valid.
- Time complexity: (len(s) - wl * wc) * wc or number_of_windows * words_per_window
- Space complexity: O(wc) + O(wc)
"""


class Solution2:
    def test(self, sub_str, word_len, ctr):
        i, seen = 0, collections.defaultdict(int)
        while i < len(sub_str):
            next_word = sub_str[i:i + word_len]
            if next_word not in ctr or seen[next_word] == ctr[next_word]:
                return False
            seen[next_word], i = seen[next_word] + 1, i + word_len
        return True

    def findSubstring(self, s, words):

        start, end, result = 0, len(words) * len(words[0]) - 1, []
        ctr = collections.Counter(words)
        while end < len(s):
            if self.test(s[start:end + 1], len(words[0]), ctr):
                result.append(start)
            start, end = start + 1, end + 1
        return result

"""
The algorithm is window sliding like used by many others. Using collections.defaultdict eliminates 
the if-else conditional statements while checking new words:
"""

class Solution3:

    def findSubstring(self, S, L):
        if not L or not L[0]: return None
        wl = len(L[0])
        totl = len(L) * wl
        count_tmpl = collections.defaultdict(int)
        for word in L: count_tmpl[word] += 1
        rtn = []
        for i in range(wl):
            count = copy.copy(count_tmpl)
            j = i
            while j < len(S)-wl+1:
                count[S[j:j+wl]] -= 1
                while count[S[j:j+wl]] < 0:
                    count[S[i:i+wl]] += 1
                    i += wl
                j += wl
                if j-i == totl: rtn.append(i)
        return rtn


class Solution4:
    class Solution:
        def findSubstring(self, s, words):
            if not words: return []
            m, n, o, target = len(s), len(words), len(words[0]), []
            for i in range(m - n * o + 1):
                word_target = words[:]
                for k in range(n):
                    word = s[i + k * o:i + k * o + o]
                    if word in word_target:
                        word_target.remove(word)
                    else:
                        break
                if not word_target: target.append(i)
            return target
