
class Solution:
    def subsetXORSum(self, nums):

        res = []
        n = len(nums)
        def dfs(i, xor):
            if i >= n:
                res.append(xor)
                return

            dfs( i +1, xor)
            dfs( i +1, xor ^ nums[i])

        dfs(0, 0)
        return sum(res)


