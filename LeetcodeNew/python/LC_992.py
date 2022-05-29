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
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, s, k):
        count = collections.defaultdict(int)
        left = 0
        res = 0

        for right, char in enumerate(s):
            count[char] += 1
            #超标了需要动
            while len(count) > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1
            #无论如何都要加
            res += right - left + 1
        return res



class SolutionRika:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        # s = map(str, nums)
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, s, k):
        window = collections.defaultdict(int)

        count = 0
        left, right = 0, 0

        while right < len(s):
            ch1 = s[right]
            window[ch1] += 1

            while len(window) > k:
                ch2 = s[left]
                window[ch2] -= 1
                if window[ch2] == 0:
                    del window[ch2]
                left += 1
            count += right - left + 1
            right += 1

        return count
