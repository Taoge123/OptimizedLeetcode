
class Solution:

    def titleToNumber(self, s: str) -> int:
        base = ord('A') - 1
        res = 0
        for char in s:
            temp = ord(char) - base
            res = res * 26 + temp

        return res


s = 'AA'
a = Solution()
print(a.titleToNumber(s))












