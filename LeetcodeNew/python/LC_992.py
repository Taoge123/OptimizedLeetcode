"""
340. Longest Substring with At Most K Distinct Characters
Good luck and have fun.

Count Number of Nice Subarrays
Replace the Substring for Balanced String
Max Consecutive Ones III
Binary Subarrays With Sum
Subarrays with K Different Integers
Fruit Into Baskets
Shortest Subarray with Sum at Least K
Minimum Size Subarray Sum



class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        start, res = 0, 0
        table = collections.defaultdict(int)

        for i, char in enumerate(s):
            table[char] = i
            if len(table) > k:
                start = min(table.values())
                del table[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res


"""

import collections

class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        return self.atMostK(A, K) - self.atMostK(A, K-1)

    def atMostK(self, A, K):
        count = collections.defaultdict(int)
        left = 0
        res = 0
        for right in range(len(A)):
            count[A[right]] += 1
            #超标了需要动
            while len(count) > K:
                count[A[left]] -= 1
                if count[A[left]] == 0:
                    del count[A[left]]
                left += 1
            #无论如何都要加
            res += right - left + 1
        return res



