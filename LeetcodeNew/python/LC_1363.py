import collections


class Solution:
    def largestMultipleOfThree(self, nums):
        total = sum(nums)
        count = collections.Counter(nums)
        nums.sort(reverse=True)

        def f(i):
            if count[i]:
                nums.remove(i)
                count[i] -= 1
            if not nums:
                return ''
            if not any(nums):
                return '0'
            if sum(nums) % 3 == 0:
                return ''.join(map(str, nums))


        if total % 3 == 0:
            return f(-1)
        if total % 3 == 1 and count[1] + count[4] + count[7]:
            return f(1) or f(4) or f(7)
        if total % 3 == 2 and count[2] + count[5] + count[8]:
            return f(2) or f(5) or f(8)
        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)




