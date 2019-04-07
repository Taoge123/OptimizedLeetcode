
"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated
and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

class SolutionCaikehe:
    # Binary search
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid + 1


class Solution2:
    def mySqrt(self, x):

        if x==1: return 1 #deal with exception
        l, r = 0, x
        while l <= r:
            mid = (r+l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                r = mid
            else:
                l = mid


class Solution3:
    def mySqrt(self, x):
        left, right = 0, x
        while left <= right:
            mid = (left + right) / 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1

