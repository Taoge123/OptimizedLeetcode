
"""
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.



Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987



Note:

The range of n is [1,8].
"""


class Solution:
    def largestPalindrome(self, n: int) -> int:

        if n == 1:
            return 9
        if n == 2:
            return 987
        for i in range(2, 9 * 10 ** (n - 1)):
            hi = (10 ** n) - i
            lo = int(str(hi)[::-1])

            temp = i ** 2 - 4 * lo
            if temp < 0:
                continue
            if (temp) ** 0.5 == int((temp) ** 0.5):
                return (lo + 10 ** n * (10 ** n - i)) % 1337



class Solution2:
    def largestPalindrome(self, n):

        maxi = 10 ** n - 1
        mini = maxi // 10
        for left in range(maxi, mini, -1):
            right = str(left)[::-1]
            target = int(str(left) + right)
            i = maxi
            while i * i > target:
                if target % i == 0:
                    return target % 1337
                i -= 1
        return 9





