
class Solution:
    def longestMountain(self, A) -> int:
        n = len(A)
        if n < 3:
            return 0

        left = 0
        res = 0
        while left < n - 2:
            while left < n - 1 and A[left] >= A[left + 1]:
                left += 1
            right = left + 1
            while right < n - 1 and A[right] < A[right + 1]:
                right += 1

            while right < n - 1 and A[right] > A[right + 1]:
                right += 1
                res = max(res, right - left + 1)

            left = right

        return res

