class Solution:
    def smallestFactorization(self, a: int) -> int:

        if a < 10:
            return a
        res = []

        for i in range(9, 1, -1):
            while a % i == 0:
                a //= i
                res.append(i)

        if a != 1:
            return 0

        res.sort()
        num = 0
        for i in range(len(res)):
            num = num * 10 + res[i]
            if num > 2 ** 31:
                return 0

        return num



