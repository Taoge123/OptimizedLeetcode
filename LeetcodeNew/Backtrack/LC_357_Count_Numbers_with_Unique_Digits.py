"""
For the first (most left) digit, we have 9 options (no zero);
for the second digit we used one but we can use 0 now,
so 9 options; and we have 1 less option for each following digits.
Number can not be longer than 10 digits.


Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
             excluding 11,22,33,44,55,66,77,88,99


"""




class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.counter = 0
        self.n = n
        ran = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if n == 0:
            return 1
        if n == 1:
            return len(ran)
        self.helper(n, ran, [])
        return self.counter + 10

    def helper(self, n, r, c):
        if len(c) > 1 and c[0] != 0:
            self.counter += 1
        if n == 0:
            return
        for j in range(len(r)):
            self.helper(n-1, r[:j]+r[j+1:], c+[r[j]])



class Solution3:
    def countNumbersWithUniqueDigits(self, n):
        # n can not be greater than 10 as it must exist two of the digit share same number
        # f(n) = 1-digits unique num combination + 2-digits unique num combination + ...
        # f(n) = 10 + 9 * 9 + 9 * 9 * 8 + ...
        # f(n) = g(0) + g(1) + g(2) + ... + g(n)
        # g(0) = 10
        # g(1) = 9 * 9
        # g(2) = 9 * 9 * 8
        # g(k) = 9 * (10 - 1) * (10 - 2) * ... * (10 - k)
        if n == 0: return 1
        if n == 1: return 10
        n = min(10, n)
        res = 10
        for n in range(1, n):
            g = 9
            for i in range(1, n + 1):
                g *= (10 - i)
            res += g
        return res

"""
There are only 9 test cases for this solution (n = 0 to n = 8) 
anything greater than that is overflowing the integer size in most of the languages. 
But, we can still solve the case where n >= 10.
Integers of length greater than 10 cannot be made without repeating digits. 
So, for any n >= 10 answer will be countNumbersWithUniqueDigits(10).

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            n = 10

        return 1 + sum([9,
                        9 * 9,
                        9 * 9 * 8,
                        9 * 9 * 8 * 7,
                        9 * 9 * 8 * 7 * 6,
                        9 * 9 * 8 * 7 * 6 * 5,
                        9 * 9 * 8 * 7 * 6 * 5 * 4,
                        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3,
                        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2,
                        9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1][:n])



"""
The variable tmp at iteration i denotes the number of i-digit integers with unique digits.
 It's easy to see that tmp = 9 when i = 1 (excluding 0), 
 tmp = 9 * 9 when i = 2, tmp = 9 * 9 * 8 when i = 3, ..., 
 tmp = 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 when i = 10. 
 When i > 10, every integer with i digits must have duplicated digits. 
 The solution res can be constructed iteratively by adding up the tmp from each iteration. 
 Finally we return res + 1 to include 0.


"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        tmp = 1
        for i in range(1,min(n,10)+1):
            if i == 1:
                tmp *= 9
            else:
                tmp *= 10-i+1
            res += tmp
        return res+1


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            n = 10

        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            return 9 * reduce(lambda x, y: x * y, range(11 - n, 10)) + self.countNumbersWithUniqueDigits(n - 1)


class SolutionTony:
    def countNumbersWithUniqueDigits(self, n):
        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n if n <= 10 else 10):

            product = product * choices[i]
            ans += product

        return ans

a = SolutionTony()
print(a.countNumbersWithUniqueDigits(2))


