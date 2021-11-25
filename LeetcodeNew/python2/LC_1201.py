
import math

"""
1-100 : 2,3,5 => 100/2 + 100/3 + 100/5 - 100/6-100/10 + 100/30

1-M: a,b,c -> n
M => count(M) v.s. n ?


"""


class Solution2:
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



class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 2 * 10 ** 9
        while left < right:
            mid = left + (right - left) // 2
            if self.count(mid, a, b, c) < n:
                left = mid + 1
            else:
                right = mid
        return left

    def count(self, m, a, b, c):
        def gcd(x, y):
            if y == 0:
                return x
            return lcm(y, x % y)

        def lcm(x, y):
            return x * y // gcd(x, y)

        return m // a + m // b + m // c - m // lcm(a, b) - m // lcm(a, c) - m // lcm(b, c) + m // lcm(lcm(a, b), c)


n = 4
a = 2
b = 3
c = 4
a = Solution()
print(a.nthUglyNumber(n, a, b, c))

