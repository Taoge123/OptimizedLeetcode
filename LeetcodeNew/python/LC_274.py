"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""


class Solution:
    def hIndex(self, citations) -> int:
        citations = sorted(citations)
        n = len(citations)
        i = 0
        while i < len(citations) and citations[n - 1 - i] > i:
            i += 1
        return i


class Solution2:
    def hIndex(self, citations) -> int:
        n = len(citations)
        table = [0] * (n+1)

        for i in citations:
            if i >= n + 1:
                table[n] += 1
            else:
                table[i] += 1

        total = 0
        for i in range(len(table) - 1, -1, -1):
            total += table[i]
            if total >= i:
                return i



class Solution3:
    def hIndex(self, citations) -> int:
        nums = sorted(citations, reverse=True)
        for i in range(len(nums)):
            if i >= nums[i]:
                return i
        return len(nums)






