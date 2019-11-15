
class Solution:
    def hammingWeight(self, n):

        res = 0

        for i in range(32):
            if (n & 1) == 1:
                res += 1
            n >>= 1

        return res



