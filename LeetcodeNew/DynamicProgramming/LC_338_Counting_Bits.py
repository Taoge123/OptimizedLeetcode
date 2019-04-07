
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

"""
这道题给我们一个整数n，然我们统计从0到n每个数的二进制写法的1的个数，存入一个一维数组中返回，题目中明确表示不希望我们一个数字一个数字，
一位一位的傻算，而是希望我们找出规律，而且题目中也提示了我们注意[2-3], [4-7], [8-15]这些区间的规律，那么我们写出0到15的数的二进制和1的个数如下：

复制代码
0    0000    0
-------------
1    0001    1
-------------
2    0010    1
3    0011    2
-------------
4    0100    1
5    0101    2
6    0110    2
7    0111    3
-------------
8    1000    1
9    1001    2
10   1010    2
11   1011    3
12   1100    2
13   1101    3
14   1110    3
15   1111    4
复制代码

我最先看出的规律是这样的，除去前两个数字0个1，从2开始，2和3，是[21, 22)区间的，值为1和2。而4到7属于[22, 23)区间的，
值为1,2,2,3，前半部分1和2和上一区间相同，2和3是上面的基础上每个数字加1。再看8到15，属于[23, 24)区间的，同样满足上述规律 
"""
"""
下面这种方法就更加巧妙了，巧妙的利用了i&(i - 1)， 这个本来是用来判断一个数是否是2的指数的快捷方法，比如8，二进制位1000, 那么8&(8-1)为0，只要为0就是2的指数, 那么我们现在来看一下0到15的数字和其对应的i&(i - 1)值：

复制代码
i    bin       '1'    i&(i-1)
0    0000    0
-----------------------
1    0001    1    0000
-----------------------
2    0010    1    0000
3    0011    2    0010
-----------------------
4    0100    1    0000
5    0101    2    0100
6    0110    2    0100
7    0111    3    0110
-----------------------
8    1000    1    0000
9    1001    2    1000
10   1010    2    1000
11   1011    3    1010
12   1100    2    1000
13   1101    3    1100
14   1110    3    1100
15   1111    4    1110

"""
import math

class Solution1:
    class Solution(object):
        def countBits(self, num):

            res = [0]
            for i in range(1, num + 1):
                res.append(res[i >> 1] + (i & 1))
            return res

class Solution2:
    def countBits(self, num):
        r = [0];
        a = 1
        for i in range(1, num + 1):
            r.append(r[i - a] + 1)
            if i == 2 * a - 1: a *= 2
        return r


class Solution3:
    def countBits(self, num):
        r = [0] * (num + 1)
        a = 1
        for i in range(1, num + 1):
            r[i] = r[i - a] + 1
            if i == 2 * a - 1:
                a *= 2
        return r


class Solution4:
    def countBits(self, num):

        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        bitcount = [0] * (num + 1)
        bitcount[0] = 0
        bitcount[1] = 1
        b = 1 # left most significant bit
        for i in range(2, num+1):
            if i >= 2**(b+1):
                b += 1
            bitcount[i] = bitcount[i-2**b] + 1
        return bitcount


"""
题目大意：
给定一个非负整数num。对于每一个满足0 ≤ i ≤ num的数字i，计算其数字的二进制表示中1的个数，并以数组形式返回。

测试用例如题目描述。

进一步思考：

很容易想到运行时间 O(n*sizeof(integer)) 的解法。但你可以用线性时间O(n)的一趟算法完成吗？

空间复杂度应当为O(n)。

你可以像老板那样吗？不要使用任何内建函数（比如C++的__builtin_popcount）。

提示：

你应当利用已经生成的结果。
将数字拆分为诸如 [2-3], [4-7], [8-15] 之类的范围。并且尝试根据已经生成的范围产生新的范围。
数字的奇偶性可以帮助你计算1的个数吗？
"""

"""
解法I 利用移位运算：

递推式：ans[n] = ans[n >> 1] + (n & 1)
"""
class Solution11:
    def countBits(self, num):

        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x >> 1] + (x & 1),
        return ans

"""
解法II 利用highbits运算：

递推式：ans[n] = ans[n - highbits(n)] + 1
其中highbits(n)表示只保留n的最高位得到的数字。

highbits(n) = 1<<int(math.log(x,2))
例如：

highbits(7) = 4   （7的二进制形式为111）

highbits(10) = 8 （10的二进制形式为1010）
"""
class Solution22:
    def countBits(self, num):

        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x - (1<<int(math.log(x,2)))] + 1,
        return ans

"""
解法II的优化：

highbits运算可以不必每次都执行，用变量pow记录当前数字i的highbits

当i == pow时，令pow左移一位
"""
class Solution33:
    def countBits(self, num):

        ans = [0]
        pow = 1
        for x in range(1, num + 1):
            ans += ans[x - pow] + 1,
            pow <<= x == pow
        return ans


"""
解法III 利用按位与运算：

递推式：ans[n] = ans[n & (n - 1)] + 1
"""

class Solution44:
    def countBits(self, num):

        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x & (x - 1)] + 1,
        return ans



