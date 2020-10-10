

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        res = 0
        for i in range(L, R + 1):
            if self.isSmallPrime(bin(i)[2:].count('1')):
                res += 1
        return res

    def isSmallPrime(self, num):
        return num in [2, 3, 5, 7, 11, 13, 17, 19]


