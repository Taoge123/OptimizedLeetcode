
class Solution:
    def waysToMakeFair(self, nums) -> int:
        res = 0
        odd = sum(nums[1::2])
        even = sum(nums[0::2])
        pre_odd = 0
        pre_even = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                if even - num + pre_odd == odd + pre_even:
                    res += 1
                even -= num
                pre_even += num
            else:
                if odd - num + pre_even == pre_odd + even:
                    res += 1
                odd -= num
                pre_odd += num

        return res

