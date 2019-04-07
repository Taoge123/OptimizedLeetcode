
"""
https://leetcode.com/problems/valid-perfect-square/discuss/130010/Python-4-Methods-with-time-testing

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

class Solution1:
    def isPerfectSquare(self, num):
        b, e = 1, (num >> 1) + 1
        while b <= e:
            mid = (b + e) >> 1
            sq = mid * mid
            if sq == num:
                return True
            if sq > num:
                e = mid - 1
            else:
                b = mid + 1
        return False


class Solution2:
    def isPerfectSquare(self, num):
        def binary_search(num):
            lo = 0
            hi = num
            while lo <= hi:
                mi = lo + (hi - lo) / 2
                sqr = mi * mi
                if sqr == num:
                    return True
                elif sqr > num:
                    hi = mi - 1
                else:
                    lo = mi + 1
            return False

        return binary_search(num)










