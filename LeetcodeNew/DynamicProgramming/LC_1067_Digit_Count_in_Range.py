
"""
Given an integer d between 0 and 9, and two positive integers low and high as lower and upper bounds,
respectively. Return the number of times that d occurs as a digit in all integers between low and high,
including the bounds low and high.

Example 1:

Input: d = 1, low = 1, high = 13
Output: 6
Explanation:
The digit d=1 occurs 6 times in 1,10,11,12,13. Note that the digit d=1 occurs twice in the number 11.
Example 2:

Input: d = 3, low = 100, high = 250
Output: 35
Explanation:
The digit d=3 occurs 35 times in 103,113,123,130,131,...,238,239,243.

Note:

0 <= d <= 9
1 <= low <= high <= 2×10^8
"""

class SolutionLee:
    def digitsCount(self, d, low, high):
        def count(N):
            if N == 0:
                return 0
            if d == 0 and N <= 10:
                return 0
            res = 0
            if N % 10 > d:
                res += 1
            if N / 10 > 0:
                res += str(N / 10).count(str(d)) * (N % 10)
            res += N / 10 if d else N / 10 - 1
            res += count(N / 10) * 10
            return res
        return count(high + 1) - count(low)


# Same as question 233. Number of Digit One

class Solution2:
    def countDigitOne(self, n: int) -> int:
        pivot, res = 1, 0
        while n >= pivot:
            res += n // (10 * pivot) * pivot + min(pivot, max(n % (10 * pivot) - pivot + 1, 0))
            pivot *= 10
        return res

# We should care when d == 0 in this question.
# can be 7 lines, but more clear with 8 lines.

class Solution3:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def helper(n, k):
            pivot, res = 1, 0
            while n >= pivot:
                res += (n // (10 * pivot)) * pivot + min(pivot, max(n % (10 * pivot) - k * pivot + 1, 0))
                res -= pivot if k == 0 else 0 # no leading zero
                pivot *= 10
            return res + 1 # last-digit can be zero
        return helper(high, d) - helper(low-1, d)





