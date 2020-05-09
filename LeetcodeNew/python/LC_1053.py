"""
https://leetcode.com/problems/previous-permutation-with-one-swap/discuss/305652/Java-JS-Python
"""

class Solution:
    def prevPermOpt1(self, A):
        n = len(A)
        left = n - 2
        right = n - 1

        while left >= 0 and A[left] <= A[left + 1]:
            left -= 1

        if left < 0:
            return A

        while A[left] <= A[right]:
            right -= 1

        while A[right] == A[right - 1]:
            right -= 1

        A[left], A[right] = A[right], A[left]

        return A



