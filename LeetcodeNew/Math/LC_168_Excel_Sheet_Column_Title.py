class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        base = ord('A')
        while n:
            n, remain = divmod(n - 1, 26)
            res = '{}{}'.format(chr(base + remain), res)

        return res

n = 88
a = Solution()
print(a.convertToTitle(n))












