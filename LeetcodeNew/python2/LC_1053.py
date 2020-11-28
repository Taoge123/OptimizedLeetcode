"""

325. Maximum Size Subarray Sum Equals k
363. Max Sum of Rectangle No Larger Than K
560. Subarray Sum Equals K
974. Subarray Sums Divisible by K
1074. Number of Submatrices That Sum to Target


https://leetcode.com/problems/previous-permutation-with-one-swap/discuss/305652/Java-JS-Python
从后往前找如果都是降序, 566789， 不行， 一定要找到一个升序的 7566789



7 5 6 6789
6 5 7 6789
-   -
"""

class Solution:
    def prevPermOpt1(self, A):
        n = len(A)
        left = n - 2
        right = n - 1

        # 找到升序的 7
        while left >= 0 and A[left] <= A[left + 1]:
            left -= 1

        # 没找到
        if left < 0:
            return A
        # 找到第一个比7小的数
        while A[left] <= A[right]:
            right -= 1
        # 我们需要后面的数字越大越好， 7和6交换就找前面的6
        while A[right] == A[right - 1]:
            right -= 1

        A[left], A[right] = A[right], A[left]
        return A




