
"""Intuition
Write some example, you find all even length palindromes are divisible by 11.
So we need to search only palindrome with odd length.

We can prove as follow:
11 % 11 = 0
1111 % 11 = 0
111111 % 11 = 0
11111111 % 11 = 0

So:
1001 % 11 = (1111 - 11 * 10) % 11 = 0
100001 % 11 = (111111 - 1111 * 10) % 11 = 0
10000001 % 11 = (11111111 - 111111 * 10) % 11 = 0

For any palindrome with even length:
abcddcba % 11
= (a * 10000001 + b * 100001 * 10 + c * 1001 * 100 + d * 11 * 1000) % 11
= 0

All palindrome with even length is multiple of 11.
So among them, 11 is the only one prime
if (8 <= N <= 11) return 11

For other cases, we consider only palindrome with odd dights.


More Generally
Explanation from @chuan-chih:
A number is divisible by 11 if sum(even digits) - sum(odd digits) is divisible by 11.
Base case: 0
Inductive step:
If there is no carry when we add 11 to a number, both sums +1.
Whenever carry happens, one sum -10 and the other +1.
The invariant holds in both cases.


Time Complexity
O(10000) to check all numbers 1 - 10000.
isPrime function is O(sqrt(x)) in worst case.
But only sqrt(N) worst cases for 1 <= x <= N
In general it's O(logx)

"""

"""
XXXXXX
YYYZZZ

XXXXX
YYYZZ

o(N) * (sqrt(N)) = o(N)

10000

10   -> 10 01
9999 => 9999 9999
XYZ - XYZZYX % 11 == 0 肯定不是质数
X * (10^5 + 10^1) % 11 = 10 + 1
Y * (10^4 + 10^2) % 11 = 10 + 1
Z * (10^3) % 11 = 10 + 1


161896423

6016 6106 106 6016106
6017 7106 106 6017106
6018 8106 106 6018106

"""


class Solution:
    def primePalindrome(self, N):
        def isPrime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        if 8 <= N <= 11:
            return 11

        for x in range(1, 100000):
            s = str(x)
            r = s[::-1]
            y = int(s + r[1:])
            print(s, r, r[1:], y)
            if y >= N and isPrime(y):
                return y
        return -1


N = 161896423
a = Solution()
print(a.primePalindrome(N))






