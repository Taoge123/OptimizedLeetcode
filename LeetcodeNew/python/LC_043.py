"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = [0] * (len(num1) + len(num2))

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                res[i + j] += int(n1) * int(n2)
                res[i + j] %= 10
                res[i + j + 1] += res[i+j] // 10

        return str(int("".join([str(i) for i in res][::-1])))


num1 = "123"
num2 = "456"
a = Solution()
print(a.multiply(num1, num2))