
class Solution:
    def minOperations(self, nums) -> int:
        res = 0
        high = 0

        for num in nums:
            h = -1
            while num:
                res += num & 1
                num >>= 1
                h += 1
            high = max(high, h)

        return res + high


class Solution2:
    def minOperations(self, nums) -> int:
        return sum(bin(x).count('1') for x in nums) + len(bin(max(nums))) - 3






