
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


