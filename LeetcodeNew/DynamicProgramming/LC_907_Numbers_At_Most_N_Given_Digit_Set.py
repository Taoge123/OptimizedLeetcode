
"""
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/

We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.
For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.

Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
"""

"""
Here is my explanation:

N has n digits, so all numbers less than n digits are valid, which are: sum(len(D) ** i for i in range(1, n))
The loop is to deal with all numbers with n digits, 
considering from N[0], N[1] back to N[n-1]. For example, N[0] is valid only for c in D if c <= N[0]. 
If c < N[0], then N[1], ..., N[n-1] can take any number in D but if c == N[0], 
then we need consider N[1], and the iteration repeats. 
That's why if N[i] not in D, then we don't need to repeat the loop anymore.
Finally i==n is addressed at the end when there exists all c in D that matches N
"""

class SolutionLee:
    def atMostNGivenDigitSet(self, D, N):
        N = str(N)
        n = len(N)
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)



class Solution1:
    def atMostNGivenDigitSet(self, D, N):
        def less(c):
            return len([char for char in D if char < c])
        d, cnt, l = len(D), 0, len(str(N))
        # For numbers which have less digits than N, simply len(D) ** digits_length different numbers can be created
        for i in range(1, l):
            cnt += d ** i
        """
        We should also consider edge cases where previous digits match with related digits in N. 
        In this case, we can make a number with previous digits + (digits less than N[i]) + D ** remaining length
        If current digit, N[i] not in D, we should break because we cannot continue for further edge cases
        """
        for i, c in enumerate(str(N)):
            cnt += less(c) * (d ** (l - i - 1))
            if c not in D: break
            if i == l - 1: cnt += 1
        return cnt







