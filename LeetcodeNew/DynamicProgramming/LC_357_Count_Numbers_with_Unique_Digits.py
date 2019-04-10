
"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99
"""

"""
For the first (most left) digit, we have 9 options (no zero); 
for the second digit we used one but we can use 0 now, so 9 options; 
and we have 1 less option for each following digits. Number can not be longer than 10 digits.
"""

"""
        # n can not be greater than 10 as it must exist two of the digit share same number
        # f(n) = 1-digits unique num combination + 2-digits unique num combination + ...
        # f(n) = 10 + 9 * 9 + 9 * 9 * 8 + ...
        # f(n) = g(0) + g(1) + g(2) + ... + g(n)
        # g(0) = 10
        # g(1) = 9 * 9
        # g(2) = 9 * 9 * 8
        # g(k) = 9 * (10 - 1) * (10 - 2) * ... * (10 - k)
"""

class Solution1:
    def countNumbersWithUniqueDigits(self, n):
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(min(n, 10)):
            product *= choices[i]
            ans += product

        return ans


class Solution2:
    def countNumbersWithUniqueDigits(self, n):

        res = 0
        tmp = 1
        for i in range(1,min(n,10)+1):
            if i == 1:
                tmp *= 9
            else:
                tmp *= (10-i+1)
            res += tmp
        return res+1






