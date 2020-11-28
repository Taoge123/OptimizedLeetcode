class Solution:
    def encode(self, num: int) -> str:
        # print(num + 1, bin(num + 1), bin(num + 1)[3:])
        return bin(num + 1)[3:]



class Solution2:
    def encode(self, num: int) -> str:
        if num == 0:
            return ""
        n = 0
        while 2 ** n - 1 <= num:
            n += 1
        res = bin(num - (2 ** (n - 1) - 1))[2:]
        while len(res) != n - 1:
            res = "0" + res
        return res


