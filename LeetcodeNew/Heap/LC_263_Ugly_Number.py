"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
"""

class Solution1:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1

class Solution2:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num == 0):
            return False
        elif(num == 1):
            return True
        else:
            if(num % 5 == 0):
                num //= 5
            elif(num % 3 == 0):
                num //= 3
            elif(num % 2 == 0):
                num //= 2
            else:
                return False
            return self.isUgly(num)


class Solution3:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return num == 1
        elif num % 5 == 0:
            return self.isUgly(num / 5)
        elif num % 3 == 0:
            return self.isUgly(num / 3)
        elif num % 2 == 0:
            return self.isUgly(num / 2)
        else:
            return False




