
class Solution:
    def validMountainArray(self, A) -> bool:
        n = len(A)
        i = 0

        while i+ 1 < n and A[i] < A[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False

        # walk down
        while i + 1 < n and A[i] > A[i + 1]:
            i += 1

        return i == n - 1




