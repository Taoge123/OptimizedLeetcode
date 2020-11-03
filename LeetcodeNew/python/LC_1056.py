
"""
246. Strobogrammatic Number
"""

class Solution:
    def confusingNumber(self, N: int) -> bool:
        table = {6 : 9,
                 9 : 6,
                 0 : 0,
                 1 : 1,
                 8 : 8
                 }

        res = 0
        n = N
        while n != 0:
            remainder = n % 10
            if remainder not in table:
                return False
            res = res * 10 + table[remainder]
            n //= 10

        return False if N == res else True



