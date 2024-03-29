"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits):

        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0

        if carry == 1:
            digits.insert(0, 1)

        return digits


class Solution2:
    def plusOne(self, digits):

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry > 9:
                digits[i] = 0
                carry = 1
            else:
                #We can return here, no need to go further
                digits[i] += carry
                return digits

        if carry == 1:
            digits.insert(0, 1)

        return digits



