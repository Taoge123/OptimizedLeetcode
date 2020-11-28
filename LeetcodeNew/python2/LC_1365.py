
class Solution:
    def smallerNumbersThanCurrent(self, nums):

        table = {}
        for i, num in enumerate(sorted(nums)):
            if num not in table:
                table[num] = i

        return [table[num] for num in nums]


class Solution2:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 102

        for num in nums:
            count[num + 1] += 1

        for i in range(1, 102):
            count[i] += count[i - 1]

        return [count[num] for num in nums]



