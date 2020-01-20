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

        prime = [True] * n
        prime[0] = prime[1] = False

        for i in range(2, n):
            if prime[i] == True:
                for j in range(2, (n - 1) // i + 1):
                    prime[i * j] = False

        return sum(prime)


class Solution2:
    def countPrimes(self, n):

        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i*i:n:i] = [False] * len(primes[i*i:n:i])
        return sum(primes)


class Solution3:
    def countPrimes(self, n):

        if n < 3:
            return 0
        digits = [1] * n
        digits[0] = digits[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if digits[i] == 1:
                for j in range(i + i, n, i):
                    digits[j] = 0

        return sum(digits)


n = 10
a = Solution2()
print(a.countPrimes(n))


