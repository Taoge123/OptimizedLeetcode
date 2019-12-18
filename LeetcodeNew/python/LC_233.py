"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
"""
 For example:
 Given n = 13,
 Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
 10 : 1    个位
 100 : 10  十位
 1000: 100 百位
 例子:
 以算百位上1为例子:   假设百位上是0, 1, 和 >=2 三种情况:
 case 1: n=3141092, a= 31410, b=92. 计算百位上1的个数应该为 3141 *100 次.
 case 2: n=3141192, a= 31411, b=92. 计算百位上1的个数应该为 3141 *100 + (92+1) 次.
 case 3: n=3141592, a= 31415, b=92. 计算百位上1的个数应该为 (3141+1) *100 次.
 http://blog.csdn.net/xudli/article/details/46798619
 time : < O(n)
 space : O(1)
 
    """


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count, num, base, highBase = 0, n, 1, 10
        while num:
            num, mod = divmod(num, 10)

            if mod == 0:
                count += (n // highBase) * base
            elif mod == 1:
                count += (n // highBase) * base + (n % base + 1)
            else:
                count += (n // highBase + 1) * base

            base *= 10
            highBase *= 10

        return count


n = 13
a = Solution()
print(a.countDigitOne(n))




