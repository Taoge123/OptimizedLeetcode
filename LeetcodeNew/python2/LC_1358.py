"""
1248 Count Number of Nice Subarrays
1234 Replace the Substring for Balanced String
1004 Max Consecutive Ones III
930 Binary Subarrays With Sum
992 Subarrays with K Different Integers
904 Fruit Into Baskets
862 Shortest Subarray with Sum at Least K
209 Minimum Size Subarray Sum

https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/discuss/516977/JavaC%2B%2BPython-Easy-and-Concise
"""

import collections

class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        res = 0
        left = 0
        count = collections.Counter()

        for right in range(len(s)):
            count[s[right]] += 1
            while all(count[c] > 0 for c in 'abc'):
                count[s[left]] -= 1
                left += 1
            #至少3个， 补集就是最多2个 (res += right - left + 1)
            res += left
        return res




