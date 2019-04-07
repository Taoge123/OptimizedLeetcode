
"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 231 − 1
when the division result overflows.
"""
"""
The description note that:
"Assume we are dealing with an environment,
which could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]."

But most of solution use "long" integer.
So I share my solution here.

Solution 1
Only one corner case is -2^31 / 1 and I deal with it at the first line.

This solution has O(logN^2) time complexity."""

class SolutionLee:

    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res


class SolutionBest:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


class GeeksForGeeks:
    def divide(self, dividend, divisor):
        # Calculate sign of divisor i.e.,
        # sign will be negative only iff
        # either one of them is negative
        # otherwise it will be positive
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

        # Update both divisor and
        # dividend positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        # Initialize the quotient
        quotient = 0
        while (dividend >= divisor):
            dividend -= divisor
            quotient += 1

        return sign * quotient


"""
分析：
不能用乘、除和取模，那剩下的，还有加、减和位运算。

会想到的就是一次次去减，不过这样会超时。
在 1 的基础上优化下，跟快速幂一样，每次把除数翻倍（用位运算即可）。
这里有坑，就是结果可能超 int 范围，所以最好用 long long 处理，之后再转 int
"""

"""
题目要求
除法运算，但是不能用编程语言提供的乘法、除法和取模运算，即只能用加法和减法实现。

解题思路
为了加速运算，可以依次将被除数减去1，2，4，8，..倍的除数。
所以这里可以用移位来进一步加速。本方法参考了kitt的博文。另外需要注意的是溢出问题。因为Python本身是没有溢出问题的，
所以需要在最后判断，结果是否溢出，如果溢出则要返回MAX_INT
"""
"""
一开始我用被除数一次一次地减除数，这样太慢了，遇到被除数为2147483648除数为1的情况就挂了。
可以用被除数不断地减除数的1倍、2倍、4倍、8倍...这样就快了。使用位运算，被除数与除数同号时商为正，异号时商为负。
"""

class Solution2:
    def divide(self, dividend, divisor):
        """ :type dividend: int :type divisor: int :rtype: int """
        MAX_INT = 2147483647
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                quotient += 1 << k
                tmp <<= 1
                k += 1
        quotient  = sign * quotient
        if quotient > MAX_INT:
            quotient = MAX_INT
        return quotient



a = SolutionBest()
print(a.divide(10, 3))








