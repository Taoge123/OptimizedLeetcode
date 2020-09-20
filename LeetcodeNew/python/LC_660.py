"""
9进制

"""


class Solution:
    def newInteger(self, n: int) -> int:
        res = 0
        base = 1

        while n > 0:
            res += (n % 9 * base)
            n //= 9
            base *= 10

        return res





