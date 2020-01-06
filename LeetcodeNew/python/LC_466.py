"""
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""




class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        count1, count2 = 0, 0
        i, j = 0, 0

        while (count1 < n1):
            if s1[i] == s2[j]:
                j += 1
                if j == len(s2):
                    j = 0
                    count2 += 1
            i += 1
            if i == len(s1):
                i = 0
                count1 += 1

        return count2 // n2


class Solution2:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        repeatCount = [0] * (n1 + 1)
        nextIndex = [0] * (n1 + 1)
        j, count = 0, 0

        for k in range(1, n1 + 1):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1
            repeatCount[k] = count
            nextIndex[k] = j

            for start in range(k):
                if nextIndex[start] == j:
                    prefixCount = repeatCount[start]
                    patternCount = (n1 - start) // (k - start) * (repeatCount[k] - prefixCount)
                    suffixCount = repeatCount[start + (n1 - start) % (k - start)] - prefixCount
                    return (prefixCount + patternCount + suffixCount) // n2

        return repeatCount[n1] // n2





