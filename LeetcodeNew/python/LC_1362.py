import math


class Solution:
    def closestDivisors(self, num: int):
        a = self.closePair(num + 1)
        b = self.closePair(num + 2)
        return a[1:] if a[0] < b[0] else b[1:]

    def closePair(self, num):
        if not num:
            return 0
        for i in range(math.floor(math.sqrt(num)) + 1, 0, -1):
            j = num // i
            if i * j == num and num % j == 0:
                return abs(int(i - j)), i, j
        return [num - 1, 1, num]



