"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        base = ord('A')
        while n:
            n, remain = divmod(n - 1, 26)
            res = '{}{}'.format(chr(base + remain), res)

        return res

n = 98
a = Solution()
print(a.convertToTitle(n))

