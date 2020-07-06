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

"""
[1, n]

1. 
345 [1] XX
000     00
001     01
...     ..
344     99
345  *  100


2.1 digit > 1:
345 => 1 * 100

2.2 digit == 1:
345 => 1 * 79 (i.e. 00-78)

2.2 digit == 0:
345 => 0


"""

"""
233.Number-of-Digit-One
本题的想法有很多，其中比较清晰容易实现的思路是：逐位查看，看该位上为1的符合条件的整数有多少个，然后将该整数的个数累加进最后的答案。
这样虽然看上去是在数整数的个数，但其实最终得到的就是digit为1的总个数。

举个例子。考虑n=345Y78，（Y是任意的数，待定），我们想考察有多少个符合要求的整数，使得其百位上可以是1.

(1) 如果前三位任取000-344之一（共345种可能），那么最低两位可以任意取00-99（共100种可能）都不会超过n。这样的数有345*100=34500个。
第一个乘数就是n的前三位，第二个乘数就是10的二次方。

(2) 如果前三位取345 (不可能更大了)，我们就要考虑Y的影响。

a. 如果Y>1，那么最低两位可以任意取00-99（共100种可能）都不会超过n。这样的数有100个。

b. 如果Y==1，那么最低两位不可以随便取，只能取00-78（共79种可能）。这个数字就是n的末两位加上1.

c. 如果Y<1，那么最低两位如论取什么，都会导致这个数大于n，不符合条件。

综合整理上述的分类讨论方案，可以将它适用于任何一个数位（个位、十位、千位、万位...），将这些数的统计全部加起来就是答案。
"""

import math

"""
[1, n]

1. 
345 [1] XX
000     00
001     01
...     ..
344     99
345  *  100


2.1 digit > 1:
345 => 1 * 100

2.2 digit == 1:
345 => 1 * 79 (i.e. 00-78)

2.2 digit == 0:
345 => 0


"""

"""
      3 5 8 7  6
  s = 6 7 8 5  3

  i = 1
  a = 3587
  count += 3587 * 10^0

  i = 2
  a = 358
  count += 358 * 10^1

  i = 3
  a = 35
  count += 35 ^ 10^2

  i = 4
  a = 3
  count += 3 ^ 10^3


"""


class SolutionWisdom:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0
        count = 0
        s = str(n)[::-1]
        m = len(s)
        print(s)
        for i in range(1, m + 1):
            a = n // math.pow(10, i)
            count += a * math.pow(10, i - 1)
            # 从后往前看digit
            digit = int(s[i - 1])
            if digit > 1:
                # 后面随便取
                count += math.pow(10, i - 1)
            elif digit == 1:
                # + 1 代表0
                count += n % math.pow(10, i - 1) + 1

        return int(count)


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


class Solution2:
    def countDigitOne(self, n: int) -> int:

        res = 0
        m = 1
        while m <= n:
            print(m, n)
            a = n // m
            b = n % m
            res += (a + 8) // 10 * m
            if a % 10 == 1:
                res += b + 1

            m *= 10
        return res




n = 13
a = Solution()
print(a.countDigitOne(n))




