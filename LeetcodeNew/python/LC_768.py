
class Solution1:
    def rotatedDigits(self, N: int) -> int:

        res = 0
        for num in range(1, N+ 1):
            num = str(num)
            if '3' in num or '4' in num or '7' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                res += 1
        return res


class Solution2:
    def rotatedDigits(self, N: int) -> int:
        skips = ['3', '4', '7']
        goods = ['2', '5', '6', '9']
        res = 0
        for num in range(1, N + 1):
            num = str(num)
            if any(skip in num for skip in skips):
                continue
            if any(good in num for good in goods):
                res += 1

        return res


class SolutionLeeSlow:
    def rotatedDigits(self, N):
        s1 = set([1, 8, 0])
        s2 = set([1, 8, 0, 6, 9, 2, 5])
        return sum(self.isGood(s1, s2, N, i) for i in range(N + 1))

    def isGood(self, s1, s2, N, x):
        s = set([int(i) for i in str(x)])
        return s.issubset(s2) and not s.issubset(s1)









