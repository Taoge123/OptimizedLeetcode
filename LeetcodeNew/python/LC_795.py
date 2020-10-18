
class SolutionTwoPointer:
    def numSubarrayBoundedMax(self, A, L: int, R: int) -> int:
        res = 0
        left = -1
        right = -1

        for i in range(len(A)):
            if A[i] > R:
                left = right = i
                continue

            if A[i] >= L:
                right = i

            res += right - left

        return res


class Solution:
    def numSubarrayBoundedMax(self, A, L: int, R: int) -> int:
        return self.count(A, R) - self.count(A, L - 1)

    def count(self, A, bound):
        res = cur = 0
        for num in A:
            if num <= bound:
                cur += 1
            else:
                cur = 0
            res += cur
        return res
