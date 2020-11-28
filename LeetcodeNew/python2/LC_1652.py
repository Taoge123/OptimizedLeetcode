
class Solution:
    def decrypt(self, code, k: int):
        n = len(code)
        res = [0] * n
        if k > 0:
            res[0] = sum(code[1 : k+ 1])
            for i in range(1, n):
                res[i] = res[i - 1] + code[(i + k) % n] - code[i]

        elif k < 0:
            res[0] = sum(code[n + k: n])
            for i in range(1, n):
                res[i] = res[i - 1] + code[i - 1] - code[(n + k + i - 1) % n]

        return res



