
"""
89. Gray Code
"""


class Solution:
    def circularPermutation(self, n: int, start: int):
        res = []
        res.append(0)

        for i in range(n):
            step = len(res)
            for j in range(step - 1, -1, -1):
                res.append(res[j] | (1 << i))

        i = res.index(start)
        return res[i:] + res[:i]



