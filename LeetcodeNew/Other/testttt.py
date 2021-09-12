import collections
import math

class Solution:
    def interchangeableRectangles(self, nums) -> int:

        table = collections.defaultdict(int)
        for i, j in nums:
            d = math.gcd(i, j)
            i, j = i // d, j // d
            table[(i, j)] += 1

        res = 0
        for k, v in table.items():
            if v == 2:
                res += 1
            else:
                res += (1 + v) * v // 2
        return res





