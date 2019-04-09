
"""
Given a positive integer n, break it into the sum of at least two positive integers
and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

"""
The key for this problem is that we need to break the number to 2s, 3s and 4s.
First we need to know a fact that,if a,b > 3, |a-b| <= 1, then a*b>=a+b.

So, if n = a + b, a = a1+a2, b=b1+b2, we should break n to a1+a2+b1+b2, |a1-a2|<1 and |b1-b2|<1 
instead of a + b, because a1*a2>a, b1*b2>b. However, we shall stop when we get a 3 or 2, 
so what we shall do is to find the list of 3 and 2.

You may have noticed why the 4 appeared. 'Cause if we break 4, we get 2+2, and 2+2 = 2*2, 
so it's the same with the condition that we get two 2s.
"""
import math

class Solution1:
    def integerBreak(self, n):

        if n == 2:
            return 1
        if n == 3:
            return 2
        list_3 = [3] * (n/3) # generate a list of 3
        mod_3 = n%3
        if mod_3 == 1: # if a 1 is left, then add it to the first element to get a 4
            list_3[0] += 1
        if mod_3 == 2: # if a 2 is left, then put it into the list
            list_3.append(2)
        return reduce(lambda a, b: a*b, list_3)


class Solution2:
    def integerBreak(self, n):

        if n == 2:
            return 1
        if n == 3:
            return 2
        t = n % 3
        if t == 0:
            return int(math.pow(3,n/3))
        if t == 1:
            return int(math.pow(3,(n-4)/3) * 4)
        if t == 2:
            return int(math.pow(3,(n-2)/3) * 2)


"""
So, assume we have C as given number and trying to divide it to n chunks.

Q. How many chunks we can divide to?
A. Obviously from 2 to C.

Q. Ok, suppose we have n chunks (from range 2 - C) what the properties of max chunk?
A. As we can check from math - combination of most closest (nearby) ints gives max product. For example
9 = 3 x 3 x 3 or 10 = 3 x 3 x 4 or 11 = 3 x 4 x 4

Q. So how to select numbers for chunks?
A. Max product chunks are always contain only 2 number which are neighbors. 3 and 4 in example above.

Q. How many each?
A. So, C %n of bigger number and n - C % n of smaller.

Q. Are we ready to implementation
A. Yes!
"""


class Solution3:
    def integerBreak(self, C):

        if C == 1:
            return 1

        vmax = 0
        for i in range(C, 1, -1):
            a, bt = divmod(C, i)
            b, at = (a + 1, i - bt)
            vmax = max(vmax, a ** at * b ** bt)

        return vmax


class Solution4:
    def integerBreak(self, n):
        if n == 2:
            return 1
        dp = [1] * (n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                _max = max(j * dp[i-j], j * (i-j))
                dp[i] = max(dp[i], _max)
        return dp[n]

class Solution44:
    def integerBreak(self, n):

        dp = [0 for i in range(n+1)]
        dp[1] = 1
        for i in range(2, n+1):
            a = [j* max(i-j, dp[i-j]) for j in range(1,i)]
            dp[i] = max(a)
        return dp[n]

class Solution444:
    def integerBreak(self, n):

        if n < 2:
            return 0
        dp = [0 for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,(i//2)+1):
                dp[i] = max(dp[i],max(dp[i-j],i-j)*max(dp[j],j))
        return dp[n]

class Solution4444:
    def integerBreak(self, n):
        dp = [1] * n
        for total in range(2, n + 1):
            for i in range(1, total//2 + 1):
                dp[total - 1] = max(dp[total - 1], max(dp[i - 1], i) * max(dp[total - i - 1], total - i))
        return dp[-1]

class Solution5:
    def integerBreak(self, n):
        dp = [0, 0, 1]
        for i in range(3, n + 1):
            dp += [max(3 * max(dp[i - 3], i - 3), 2 * max(dp[i - 2], i - 2), 1 * max(dp[i - 1], i - 1))]
        return dp[n]


"""
From the hint:

7 = 3 + 4 = 12

8 = 3 + 3 + 2 = 18

9 = 3 + 3 + 3 = 27

10 = 3 + 3 + 4 = 36

11 = 3 + 3 + 3 + 2 = 54

12 = 3 + 3 + 3 + 3 = 81

Three is a magic number.
"""
class Solution6:
    def integerBreak(self, n):
        if n == 2 or n == 3:
            return n - 1
        if n % 3 == 0:
            return 3**(n/3)
        if n % 3 == 1:
            return 3**(n/3 - 1)*4
        if n % 3 == 2:
            return 3**(n/3)*2

