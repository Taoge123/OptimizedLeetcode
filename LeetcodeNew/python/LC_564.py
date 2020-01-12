
"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
res: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


class Solution:
    def nearestPalindromic(self, s: str) -> str:
        n = len(s)
        isEven = (n % 2 == 0)
        mid = n // 2 - 1 if isEven else n // 2

        left = int(s[0:mid + 1])

        candidates = []
        candidates.append(self.getPalindrome(left, isEven))
        candidates.append(self.getPalindrome(left + 1, isEven))
        candidates.append(self.getPalindrome(left - 1, isEven))
        candidates.append(pow(10, n - 1) - 1)
        candidates.append(pow(10, n) + 1)

        diff = float('inf')
        res = 0
        num = int(s)

        for cand in candidates:
            if cand == num:
                continue

            if abs(cand - num) < diff:
                diff = abs(cand - num)
                res = cand
            elif abs(cand - num) == diff:
                res = min(res, cand)

        return str(res)

    def getPalindrome(self, left, isEven):
        res = left
        if not isEven:
            left = left // 10

        while left > 0:
            res = res * 10 + left % 10
            left //= 10

        return res










