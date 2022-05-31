"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


class Solution2:
    def isHappy(self, n):

        visited = set()

        while n not in visited:
            visited.add(n)
            n = sum([int(i) ** 2 for i in str(n)])

        return n == 1


class SolutionTony:
    def isHappy(self, n: int) -> bool:

        visited = set()
        while n not in visited:
            count = 0
            visited.add(n)
            for num in str(n):
                count += int(num) ** 2

            n = count
        return n == 1

