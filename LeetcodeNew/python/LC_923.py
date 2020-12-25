"""
https://www.youtube.com/watch?v=GYIrV9yxgeU
"""


class Solution:
    def threeSumMulti(self, A, target):
        mod = 10 ** 9 + 7
        count = [0] * 101
        for x in A:
            count[x] += 1

        res = 0

        # All different
        for x in range(101):
            for y in range(x + 1, 101):
                z = target - x - y
                if y < z <= 100:
                    res += count[x] * count[y] * count[z]
                    res %= mod

        # x == y
        for x in range(101):
            z = target - 2 * x
            if x < z <= 100:
                res += count[x] * (count[x] - 1) // 2 * count[z]
                res %= mod

        # y == z
        for x in range(101):
            if (target - x) % 2 == 0:
                y = (target - x) // 2
                if x < y <= 100:
                    res += count[x] * count[y] * (count[y] - 1) // 2
                    res %= mod

        # x == y == z
        if target % 3 == 0:
            x = target // 3
            if 0 <= x <= 100:
                res += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                res %= mod

        return res


