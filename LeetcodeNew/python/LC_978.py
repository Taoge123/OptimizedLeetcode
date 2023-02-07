
import functools

class SolutionTony:
    def maxTurbulenceSize(self, nums) -> int:
        n = len(nums)
        res = 0

        @functools.lru_cache(None)
        def dfs(i, last, up):
            if i >= n:
                return 0

            res = 0
            if (up and nums[i] > last) or (not up and nums[i] < last):
                res += dfs( i +1, nums[i], not up) + 1
            return res

        for i in range(n):
            # go up first
            o1 = dfs(i, 0, True)
            # go down first
            o2 = dfs(i, float('inf'), False)
            res = max(res, o1, o2)
        return res



class Solution:
    def maxTurbulenceSize(self, A) -> int:
        res = cur = 0

        for i in range(len(A)):
            if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
                cur += 1
            elif i >= 1 and A[i - 1] != A[i]:
                cur = 2
            else:
                cur = 1
            res = max(res, cur)
        return res





