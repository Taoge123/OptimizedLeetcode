
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

"""
A/len(A) = B/len(B) = C/len(C)

A/a = C/c
A * c = C * a

cur/count = summ/n
cur * n = summ * count


"""


class SolutionMemo:
    def splitArraySameAverage(self, A) -> bool:
        self.summ = sum(A)
        self.n = len(A)
        memo = {}
        for count in range(1, len(A) // 2 + 1):
            if self.summ * count % self.n != 0:
                continue
            if self.dfs(A, count, self.summ * count / self.n, 0, memo):
                return True
        return False

    def dfs(self, nums, count, target, pos, memo):
        if (count, target, pos) in memo:
            return memo[(count, target, pos)]
        if count == 0 and target == 0:
            return True
        if pos == len(nums):
            return False
        if count == 0 or target == 0:
            return False
        if self.dfs(nums, count - 1, target - nums[pos], pos + 1, memo):
            memo[(count, target, pos)] = True
            return memo[(count, target, pos)]
        i = pos
        while i < len(nums) and nums[i] == nums[pos]:
            i += 1
        if self.dfs(nums, count, target, i, memo):
            memo[(count, target, i)] = True
            return memo[(count, target, i)]
        memo[(count, target, pos)] = False
        return memo[(count, target, pos)]











