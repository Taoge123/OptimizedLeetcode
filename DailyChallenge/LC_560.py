import collections

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        table = collections.defaultdict(int)
        table[0] = 1
        summ = 0
        res = 0

        for num in nums:
            summ += num
            # print(table[summ - k])
            res += table[summ - k]
            table[summ] += 1
        return res




