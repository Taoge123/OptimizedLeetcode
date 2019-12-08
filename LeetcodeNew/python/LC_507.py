

"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""

import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num < 2:
            return False
        res = 1
        sqrt = int(math.sqrt(num) + 1)

        for i in range(2, sqrt):
            if num % i == 0:
                res += i + num // i
        return res == num




