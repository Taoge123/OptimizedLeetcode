

class Solution:
    def missingNumber(self, arr) -> int:
        return (min(arr) + max(arr)) * (len(arr) + 1) // 2 - sum(arr)


class SolutionBinarySearch:
    def missingNumber(self, A) -> int:
        n = len(A)
        d = (A[-1] - A[0]) // n
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if A[mid] == A[0] + d * mid:
                left = mid + 1
            else:
                right = mid
        return A[0] + d * left



