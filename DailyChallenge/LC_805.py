
class Solution:
    def splitArraySameAverage(self, A) -> bool:
        total = sum(A)
        n = len(A)
        for num in range(1, n // 2 + 1):
            if total * num % n != 0:
                continue
            # total * num / n is the curSum
            if self.dfs(A, num, total * num / n, 0):
                return True
        return False

    def dfs(self, A, num, curSum, index):
        if curSum == 0 and num == 0:
            return True

        if index == len(A):
            return False

        if num == 0 or curSum == 0:
            return False

        if self.dfs(A, num - 1, curSum - A[index], index + 1):
            return True

        i = index
        while i < len(A) and A[i] == A[index]:
            i += 1

        if i < len(A) and self.dfs(A, num, curSum, i):
            return True

        return False




"""
with cache is slower
"""