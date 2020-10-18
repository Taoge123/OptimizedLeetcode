"""
X X X [X X X X] X X X
固定right, find left, because we need prsSum


sum[i:j] = presu[j] - presum[i-1]
r0         r          r-r0



"""


class Solution:
    def minSubarray(self, nums, p):
        need = sum(nums) % p
        table = {0: -1}
        presum = 0
        n = len(nums)
        res = len(nums)
        for i, num in enumerate(nums):
            presum = (presum + num) % p
            table[presum] = i
            if (presum - need) % p in table:
                res = min(res, i - table[(presum - need) % p])
        return res if res < n else -1



