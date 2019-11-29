"""
Given a non-empty string s and an integer k, rearrange the string
such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""

import collections, heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        _len = len(s)
        wordCount = collections.Counter(s)
        queue = []
        heapq.heapify(queue)
        res = ""
        for word, count in wordCount.items():
            heapq.heappush(queue, (-count, word))

        while queue:
            loop = min(_len, max(1, k))
            used = []
            for i in range(loop):
                if not queue:
                    return ""
                count, word = heapq.heappop(queue)
                res += word
                if -count > 1:
                    used.append((count + 1, word))
                _len -= 1
            for use in used:
                heapq.heappush(queue, use)
        return res





