class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        res = 0
        while a or b or c:
            i, j, k = a & 1, b & 1, c & 1
            if i | j != k:
                if i == 1 and j == 1:
                    res += 2
                else:
                    res += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return res



