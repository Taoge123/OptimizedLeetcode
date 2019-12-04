
"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

import collections

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:

        count = collections.Counter()
        curMax = 0
        for i, val in enumerate(p):
            a, b = ord(p[i-1]), ord(p[i])
            if i > 0 and (b - a == 1 or a - b == 25):
                curMax += 1
            else:
                curMax = 1
            count[ord(val) - ord('a')] = max(curMax, count[ord(val) - ord('a')])

        res = sum([v for k, v in count.items()])
        return res



class Solution2:
    def findSubstringInWraproundString(self, p: str) -> int:
        res = {char: 1 for char in p}
        count = 1
        for pre, cur in zip(p, p[1:]):
            count = count + 1 if (ord(cur) - ord(pre)) % 26 == 1 else 1
            res[cur] = max(res[cur], count)
        print(res)
        return sum(res.values())





