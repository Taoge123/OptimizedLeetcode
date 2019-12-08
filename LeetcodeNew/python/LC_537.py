
"""
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100].
And the output should be also in this form.
"""

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x1, y1 = a[:-1].split('+')
        x1, y1 = int(x1), int(y1)

        x2, y2 = b[:-1].split('+')
        x2, y2 = int(x2), int(y2)

        res = str(x1 * x2 - y1 * y2) + "+" + str(x1 * y2 + x2 * y1) + "i"

        return res


