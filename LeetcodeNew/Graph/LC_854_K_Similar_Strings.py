
"""

https://leetcode.com/problems/k-similar-strings/discuss/241213/Python-solution-with-lots-of-thinking


Strings A and B are K-similar (for some non-negative integer K)
if we can swap the positions of two letters in A exactly K times
so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2

"""
import collections, sys


class Solution:
    def kSimilarity(self, a, b):
        if len(a) != len(b) or collections.Counter(a) != collections.Counter(b):
            return 0
        memo = dict()
        self.ans = sys.maxsize

        def helper(a, b):
            if a == b: return 0
            if (a, b) in memo:
                return memo[(a, b)]
            if a[-1] == b[-1]:
                self.ans = min(self.ans, helper(a[:-1], b[:-1]))
            else:
                for i in range(len(a) - 1):
                    if a[i] == b[-1]:
                        a_ = a[:i] + a[-1] + a[i + 1:-1]
                        self.ans = min(self.ans, 1 + helper(a_, b[:-1]))

            memo[(a, b)] = self.ans
            return self.ans

        return helper(a, b)


"""
The idea is, find the first character i where A[i] != B[i] , 
then swap it with all occurrence of B[i] in A, and see which produce the smallest answer.
"""


class Solution2:
    def kSimilarity(self, A, B):
        return self.helper(A, B, {})

    def helper(self, A, B, mem):
        if A == B:
            return 0

        if A in mem:
            return mem[A]

        ans = float('inf')
        i = 0
        # find first i where A[i] != B[i]
        while A[i] == B[i]:
            i += 1

        diffChar = B[i]
        for j, c in enumerate(A[i:], i):
            if c == diffChar:
                # find the smallest answer after each swap
                ans = min(ans, 1 + self.helper(A[i + 1:j] + A[i] + A[j + 1:], B[i + 1:], mem))
        mem[A] = ans
        return ans







