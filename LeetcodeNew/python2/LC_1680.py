import math


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        s = "".join(bin(i)[2:] for i in range(n + 1))
        return int(s, 2) % mod


"""
n=1, 1 -> 1
n=2, 110 -> 1*2^2 + 2 = 6
n=3, 110 11 -> 6*2^2 + 3 = 27

res[n] = res[n-1] * 2 ^ len + n
len = how many bits for n


1. 1
2. 2
3. 2
4. 3




"""


class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10 ** 9 + 7
        res = 1
        for i in range(2, n + 1):
            size = int(math.log(i) / math.log(2)) + 1
            res = ((res << size) + i) % mod
            res %= mod
        return res

