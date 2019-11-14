
class Solution:

    def reverseBits(self, n):

        if n == 0:
            return 0
        res = 0
        for i in range(32):
            res <<= 1
            if (n & 1) == 1:
                res += 1
            n >>= 1
        return res



