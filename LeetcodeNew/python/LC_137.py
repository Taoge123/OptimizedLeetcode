
"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution:
    def singleNumber(self, nums) -> int:
        a = set(nums)
        a = sum(a) * 3 - sum(nums)
        a = a // 2
        return a


class Solution2:
    def singleNumber(self, nums) -> int:
        ones, twos = 0, 0

        for i in range(len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones

        return ones


class Solution3:
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            summ = 0
            for num in nums:
                summ += (num >> i) & 1
                print(num, i, num >> i, (num >> i) & 1, summ)
            rem = summ % 3

            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem * (1 << i)

        return res


"""
13
13
13
34
34
34
...
...
...
25

% 3 -> 

"""


class Solution33:
    def singleNumber(self, nums):
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                bits[i] += num >> i & 1
        res = 0
        for i, val in enumerate(bits):
            # if the single numble is negative,
            # this case should be considered separately
            if i == 31 and val % 3:
                res = -((1 << 31) - res)
            else:
                res |= (val % 3) * (1 << i)
        return res


nums = [2, 2, 3, 2]
a = Solution()
print(a.singleNumber(nums))




