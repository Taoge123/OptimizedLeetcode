"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""

class Solution:
    def countPrimes(self, n):

        if n<= 2:
            return 0

        ans = [True] * n
        ans[0] = ans[1] = False

        for i in range(2, n):
            if ans[i] == True:
                for j in range(2, (n - 1) // i + 1):
                    ans[i * j] = False

        return sum(ans)


