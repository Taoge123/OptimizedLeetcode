"""
340. Longest Substring with At Most K Distinct Characters

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
        start = 0
        res = 0
        for j in range(len(A)):
            count[A[j]] += 1
            #超标了需要动
            while len(count) > K:
                count[A[start]] -= 1
                if count[A[start]] == 0:
                    del count[A[start]]
                start += 1
            #无论如何都要加
            res += j - start + 1
        return res



