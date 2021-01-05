import collections


class Solution:
    def countPairs(self, deliciousness) -> int:
        mod = 10 ** 9 + 7
        res = 0
        count = collections.defaultdict(int)
        for num in deliciousness:
            for k in range(22):
                res += count[2 ** k - num]
            count[num] += 1
        return res % mod


