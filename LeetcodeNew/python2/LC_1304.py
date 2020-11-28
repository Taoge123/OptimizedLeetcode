class Solution:
    def sumZero(self, n: int):
        res = []
        if n % 2 == 1:
            res.append(0)
        res.extend([-i for i in range(1, n // 2 + 1)])
        res.extend([i for i in range(1, n // 2 + 1)])
        return res



