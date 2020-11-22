"""
100
10
aaa aaa aaa 9


"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ""
        i = 0
        while i < n:
            for num in range(1, 27):
                if num + (n - i - 1) * 26 >= k:
                    res += chr(ord('a') + num - 1)
                    k -= num
                    break

            i += 1
        return res




