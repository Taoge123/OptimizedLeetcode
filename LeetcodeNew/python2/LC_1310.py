
class Solution:
    def xorQueries(self, arr, queries):
        n = len(arr)
        xors = [0] * (n + 1)

        for i in range(n):
            xors[i + 1] = xors[i] ^ arr[i]

        res = []
        for l, r in queries:
            res.append(xors[r + 1] ^ xors[l])
        return res


