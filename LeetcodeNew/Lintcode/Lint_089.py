
class Solution:
    def kSum(self, A, k, target):
        memo = {}
        return self.dfs(A, 0, k, target, memo)

    def dfs(self, A, pos, k, target, memo):
        if (pos, k, target) in memo:
            return memo[(pos, k, target)]

        if pos == len(A):
            return 0

        if k == 0 and target == 0:
            return 1

        take = self.dfs(A, pos + 1, k - 1, target - A[pos], memo)
        no_take = self.dfs(A, pos + 1, k, target, memo)

        memo[(pos, k, target)] = take + no_take
        return memo[(pos, k, target)]


A = [1,2,3,4]
k = 2
target = 5

a = Solution()
print(a.kSum(A, k, target))


