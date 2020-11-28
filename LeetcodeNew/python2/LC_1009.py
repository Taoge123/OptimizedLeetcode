"""
1010
我们需要找0101， 那就直接10000 - 1 = 1111
1010 ^ 1111 = 0101

"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        num = 1
        while N >= num:
            num <<= 1

        return N ^ (num - 1)


class Solution2:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        num = 1
        while N >= num:
            num <<= 1

        # 减法也可以
        return num - 1 - N


