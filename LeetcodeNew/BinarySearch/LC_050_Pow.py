
"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

# 使用一个Helper
class Solution1:
    def myPow(self, a, b):
        if b < 0:
            return 1 / self.helper(a, -b)
        else:
            return self.helper(a, b)

    def helper(self, a, b):
        if b == 0:
            return 1
        half = self.helper(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a


# 不使用Helper
class Solution2:
    def myPow(self, a, b):
        if b == 0: return 1
        if b < 0: return 1.0 / self.myPow(a, -b)
        half = self.myPow(a, b // 2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a

"""
Leetcode中被人讨厌最多的题目之一。
但其实是个很好的Recursion入门题目。

> Base Case:  b == 0
> Function: F(a ^ b) = F(a ^ b // 2) *  F(a ^ b // 2)

不论我们返回时候如何，我们执行第一步，先设立Base Case:
if b == 0: return 1

完了以后，我们要对大问题进行拆分，也就是不断的对b的值折半

拆分：
half = self.myPow(a, b // 2)

当拆分到了最小的问题，满足base case b == 0 的时候，我们则进行返回，返回时候有三种可能

Function的三种可能性：

当b为偶数的时候，比如 2 ^ 100，拆分的时候就变成 (2 ^ 50) * (2 ^ 50)
当b为基数的时候，比如 2 ^ 25，拆分的时候就变成 (2 ^12) * (2 ^ 12) * 2
当b为负数的时候，返回 1.0 / self.myPow(a, -b)

时间复杂度 = 一叉树里面每层的时间复杂度 * 层数 = 1 * log(b) = log(b)
空间复杂度 = O(h) 也就是一叉树的层数 = log(b)

"""


class Solution:

    def pow(self, x, n):
        if(n==0):
            return 1
        elif(n==1):
            return x;
        if(n<0):
            return self.pow(1/x,-n)
        else:
            if(n%2==0):
                return self.pow(x*x,n/2)
            else:
                return self.pow(x*x,(n-1)/2) * x



