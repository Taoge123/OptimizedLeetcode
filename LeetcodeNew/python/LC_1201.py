
import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab, bc, ca = self.lcm(a, b), self.lcm(b, c), self.lcm(c, a)
        abc = self.lcm(ab, c)
        low = 1
        high = 2 * 10 ** 9
        while low < high:
            mid = low + (high - low) // 2
            if self.count_ugly(mid, a, b, c, ab, bc, ca, abc) < n:
                low = mid + 1
            else:
                high = mid
        return low

    def lcm(self, x, y):
        return x * y // math.gcd(x, y)

    def count_ugly(self, n, a, b, c, ab, bc, ca, abc):
        res = n // a + n // b + n // c
        res -= n // ab + n // bc + n // ca
        res += n // abc
        return res





