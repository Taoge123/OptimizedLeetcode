
"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.
"""
import heapq

class SOlutionDP1:
    def nthUglyNumber(self, n):
        if n <= 0:
            return 0
        ugly = [1] * n
        i2 = i3 = i5 = 0
        for i in xrange(1, n):
            ugly[i] = min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5)
            if ugly[i] == ugly[i2] * 2:
                i2 += 1
            if ugly[i] == ugly[i3] * 3:
                i3 += 1
            if ugly[i] == ugly[i5] * 5:
                i5 += 1
        return ugly[-1]

"""
方法二
所有的ugly number都是由1开始，乘以2/3/5生成的。

只要将这些生成的数排序即可获得，自动排序可以使用set

这样每次取出的第一个元素就是最小元素，由此再继续生成新的ugly number.

可以分成如下三组：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …

(2) 1×3, 2×3, 3×3, 4×3, 5×3, …

(3) 1×5, 2×5, 3×5, 4×5, 5×5, …

使每个组已经用过的数字删除掉，这样列表中只有一个元素，获取三个组的最小值之后就计算下一个丑数。
"""
class SolutionDP2:
    def nthUglyNumber(self, n):

        if n < 0:
            return 0
        dp = [1] * n
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
            if dp[i] == 2 * dp[index2]: index2 += 1
            if dp[i] == 3 * dp[index3]: index3 += 1
            if dp[i] == 5 * dp[index5]: index5 += 1
        return dp[n - 1]

"""
问题分析：
（1）这个可以考虑动态规划的思想，要求第n个丑数，思考一下，第n个丑数是怎么来的？
它一定是在第n个丑数之前的n-1个丑数中的一个，乘以2、3、5得来的。现在的问题就是，
如何从前n-1个丑数中选出那个丑数来，然后又如何确定是乘以2那，还是3 或者是5那？
（2）解决办法，用一个ugly[i]表示第i+1个丑数，维护一系列丑数。
（3）用变量i2记录在ugly[]中出现的第一个丑数，且，这个丑数乘以2 大于ugly[]中最后一个丑数。 
此时，很显然ugly[i2] * 2就是下一个丑数的备选值，同理选出ugly[i3] * 3、ugly[i5] * 5，
然后从这三个值里面选择最小的作为下一个丑数。以此类推，直到选出n个来。
"""
class SolutionDP3:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
        return ugly[-1]


"""
解题思路：
参考：http://www.geeksforgeeks.org/ugly-numbers/

丑陋数序列可以拆分为下面3个子列表：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5

接下来我们使用与归并排序相似的合并方法，从3个子列表中获取丑陋数。每一步我们从中选出最小的一个，然后向后移动一步。
"""

class Solution:

    def nthUglyNumber(self, n):
        q = [1]
        i2 = i3 = i5 = 0
        while len(q) < n:
            m2, m3, m5 = q[i2] * 2, q[i3] * 3, q[i5] * 5
            m = min(m2, m3, m5)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
            q += m,
        return q[-1]




class Solution1:
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]


class Solution2:
    def nthUglyNumber(self, n):
        h = [(1, 1)]
        for _ in range(n):
            val, fact = heapq.heappop(h)
            heapq.heappush(h, (val * 5, 5))
            if fact <= 3:
                heapq.heappush(h, (val * 3, 3))
            if fact <= 2:
                heapq.heappush(h, (val * 2, 2))
        return val


class Solution22:
    def nthUglyNumber(self, n):
        h = [(1, 1)]
        for _ in range(n):
            val, fact = heapq.heappop(h)
            for x in 2, 3, 5:
                if fact <= x:
                    heapq.heappush(h, (val * x, x))
        return val


