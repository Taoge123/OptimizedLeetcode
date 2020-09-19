
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        mod = 10 ** 9 + 7
        j = n - 1
        for i in range(n):
            while j>= i and nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                break
            res += pow(2, j - i, mod)
            res %= mod

        return int(res)


