
import functools

class SolutionDFS1:
    def maxDotProduct(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)
        @functools.lru_cache(None)
        def dfs(i, j):
            # if i == m and j == n:
            #     return 0
            if i == m or j == n:
                return float('-inf')

            res = float('-inf')
            # pick cur and prev, pick cur and abandon prev, i move or j move
            res = max(dfs(i + 1, j + 1) + nums1[i] * nums2[j], nums1[i] * nums2[j], dfs(i + 1, j), dfs(i, j + 1))
            return res

        return dfs(0, 0)



class SolutionDFS2:
    def maxDotProduct(self, nums1, nums2) -> int:
        memo = {}
        return self.dfs(nums1, nums2, 0, 0, memo)

    def dfs(self, nums1, nums2, i, j, memo):
        m, n = len(nums1), len(nums2)
        if (i, j) in memo:
            return memo[(i, j)]

        if i == m or j == n:
            return float('-inf')

        # pick cur and prev, pick cur and abandon prev, i move or j move
        res = max(self.dfs(nums1, nums2, i + 1, j + 1, memo) + nums1[i] * nums2[j],
                  nums1[i] * nums2[j],
                  self.dfs(nums1, nums2, i + 1, j, memo),
                  self.dfs(nums1, nums2, i, j + 1, memo))
        memo[(i, j)] = res
        return res

