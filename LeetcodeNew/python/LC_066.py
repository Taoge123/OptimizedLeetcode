
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




