
"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False


Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
import collections


class SolutionTony:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        count1 = collections.Counter(s1)
        count2 = collections.Counter(s2[:m])

        # count2 will be a fixed length window
        if count1 == count2:
            return True

        # shift count2 (the second window), if we are able to get this window to match the first window, the we good.
        for i in range(m, n):
            count2[s2[i]] += 1
            count2[s2[i - m]] -= 1
            if count1 == count2:
                return True

        return False



class SolutionRika:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # compare freq of char in both s1 and s2 + sliding window

        counter = collections.Counter(s1)

        window = collections.defaultdict(int)
        left, right = 0, 0
        match = 0

        while right < len(s2):
            ch = s2[right]
            right += 1
            if ch in counter:
                window[ch] += 1
                if window[ch] == counter[ch]:
                    match += 1
            if right - left >= len(s1):
                if match == len(counter):
                    return True
                ch = s2[left]
                left += 1
                if ch in counter:
                    if window[ch] == counter[ch]:  # only match -= 1 once
                        match -= 1
                    window[ch] -= 1
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        counter1, counter2 = collections.Counter(s1), collections.Counter(s2[:n1])
        for i in range(n1, n2):
            if counter1 == counter2:
                return True

            counter2[s2[i]] += 1
            counter2[s2[i - n1]] -= 1
            if counter2[s2[i - n1]] <= 0:
                del counter2[s2[i - n1]]

        return counter1 == counter2


s1 = "ab"
s2 = "eidbaooo"

a = Solution()
print(a.checkInclusion(s1, s2))


