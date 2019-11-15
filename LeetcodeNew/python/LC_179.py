from functools import cmp_to_key


class Solution:

    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums = sorted(nums, key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

        res = ''.join(nums).lstrip('0')
        return res or '0'



