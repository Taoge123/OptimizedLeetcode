
"""
https://leetcode.com/problems/nth-magical-number/solution/

A positive integer is magical if it is divisible by either A or B.

Return the N-th magical number.  Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: N = 1, A = 2, B = 3
Output: 2
Example 2:

Input: N = 4, A = 2, B = 3
Output: 6
Example 3:

Input: N = 5, A = 2, B = 4
Output: 10
Example 4:

Input: N = 3, A = 6, B = 4
Output: 8
"""

import math

class Solution1:
    def nthMagicalNumber(self, N, A, B):
        from fractions import gcd
        MOD = 10**9 + 7

        L = A / gcd(A, B) * B
        M = L / A + L / B - 1
        q, r = divmod(N, M)

        if r == 0:
            return q * L % MOD

        heads = [A, B]
        for _ in range(r - 1):
            if heads[0] <= heads[1]:
                heads[0] += A
            else:
                heads[1] += B

        return (q * L + min(heads)) % MOD


class Solution2:
    def nthMagicalNumber(self, N, A, B):
        from fractions import gcd
        MOD = 10**9 + 7
        L = A / gcd(A,B) * B

        def magic_below_x(x):
            #How many magical numbers are <= x?
            return x / A + x / B - x / L

        lo = 0
        hi = 10**15
        while lo < hi:
            mi = (lo + hi) / 2
            if magic_below_x(mi) < N:
                lo = mi + 1
            else:
                hi = mi

        return lo % MOD


"""
4 points to figure out:

1. Get gcd (greatest common divisor) and lcm (least common multiple) of (A, B).
   (a, b) = (A, B) while b > 0: (a, b) = (b, a % b)
   then, gcd = a and lcm = A * B / a

2. How many magic numbers <= x ?
   By inclusion exclusion principle, we have:
   x / A + x / B - x / lcm

3. Set our binary search range
   Lower bound is min(A, B), I just set left = 2.
   Upper bound is N * min(A, B), I just set right = 10 ^ 14.

4. binary search, find the smallest x that x / A + x / B - x / lcm = N

while (l < r) {
    m = (l + r) / 2;
    if (m / A + m / B - m / (A * B / a) < N) // m too small
        l = m + 1;
    else // m may be too big
        r = m;
}
Time Complexity:
O(log(10**14))

"""

class Solution3:
    def nthMagicalNumber(self, N, A, B):
        a, b = A, B
        while b: a, b = b, a % b
        l, r, lcm = 2, 10**14, A * B / a
        while l < r:
            m = (l + r) / 2
            if m / A + m / B - m / lcm < N: l = m + 1
            else: r = m
        return l % (10**9 + 7)

"""
Suppose A =2 and B = 3, then the lcm is 6. The list of magical number less or equal to 6 is [2,3,4,6].
Then, the 1st to 4th magical number to [2,3,4,6], the 5th to 8th number is 6 added to [2,3,4,6] 
respectively, the 9th to 12nd number is 6*2 added to [2,3,4,6] respectively, and so on.

So, the key here is to get all the magical number less or equal to the lcm of A and B. 
Then, the Nth number can be obtained immediately.
"""

class Solution4:
    class Solution(object):
        def gcd(self, x, y):
            while y > 0:
                x, y = y, x % y
            return x

        def lcm(self, x, y):
            return x * y // self.gcd(x, y)

        def nthMagicalNumber(self, N, A, B):
            temp = self.lcm(A, B)
            seq = {}
            for i in range(1, temp // A + 1):
                seq[i * A] = 1
            for i in range(1, temp // B + 1):
                seq[i * B] = 1
            cand = sorted([key for key, value in seq.items()])
            ans = ((N - 1) // len(cand)) * cand[-1] + cand[N % len(cand) - 1]
            return ans % (10 ** 9 + 7)


class Solution5:

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def count(self, num, A, B, lcm):
        return num // A + num // B - num // lcm

    def nthMagicalNumber(self, N, A, B):
        l, r, lcm = 2, 2 ** 63 - 1, A * B // self.gcd(A, B)
        while l < r:
            mid = (l + r) // 2
            if self.count(mid, A, B, lcm) < N:
                l = mid + 1
            else:
                r = mid
        return l % (10 ** 9 + 7)


class Solution6:
    def nthMagicalNumber(self, N, a,b):
        lcm = a * b / math.gcd(a,b)
        l,r = min(a,b), min(a,b) * N
        while l < r:
            m = l + r >> 1
            s = m // a + m // b - m // lcm
            if s < N:
                l = m + 1
            else:
                r = m
        return l % (10 ** 9 + 7)

