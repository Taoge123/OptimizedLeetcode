
"""
https://leetcode.com/problems/smallest-good-base/discuss/96597/5-liner-3ms-really-TIGHT-search-bounds-with-time-complexity-analysis-O((logN)2)-(detailed-explanation)
https://leetcode.com/problems/smallest-good-base/discuss/96587/Python-solution-with-detailed-mathematical-explanation-and-derivation
https://yq.aliyun.com/articles/334324

For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:

Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.


Example 2:

Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
"""

"""
题目大意：
给定整数n，如果n的k进制表示全部为1，则称k为n的一个“良好基数”（good base），其中k≥2

给定字符串表示的n，以字符串形式返回n的最小的“良好基数”

注意：

n的取值范围是[3, 10^18]
字符串形式的n总是有效的并且不包含前导0
"""
"""
解题思路：
枚举法

记k的最高次幂为m，从上界 int(log(n)) 向下界 1 递减枚举m

问题转化为计算1 + k + k^2 + ... + k^m = n的正整数解

由n > k^m得： k < n ** 1/m

由n < (k + 1)^m得： k > n ** 1/m - 1，此处使用了二项式定理

因此k可能的解为：int(n ** 1/m)

最后验证1 + k + k^2 + ... + k^m 是否等于 n
"""
import math

class Solution1:
    def smallestGoodBase(self, n):

        n = int(n)
        for m in range(int(math.log(n, 2)), 1, -1):
            k = int(n ** (1.0 / m))
            if sum(k ** i for i in range(m + 1)) == n:
                return str(k)
        return str(n - 1)


"""
这道题目的基本思路是二分查找。注意到不同的k将会对应不同的长度d，使得11...1(一共d位)在k进制下表示n。
而最小的k就意味着最大的d。所以我们就让d从大到小循环，看看11...1(一共d位)是否可以在某个base k下构成n。

对于长度为d的这个数，k的最小值显然是1，最大值则是power(tn, 1.0 / d) + 1。
于是我们在这个区间内二分查找合适的k，并返回即可。
"""

"""
本题是寻找一个数最小的good base。其定义是对于一个数y，其x进制表示为全1，则称x是y的good base。
应该比较好理解，其实就是将y写成1+x+x^2+...+x^(n-1)，就是一个等比数列求和，
于是我们可以将其转化为y = (x^n - 1)/(x - 1)，其中x>=2, 3<y<10^18,为了寻找最小的x，我们可以先来确定一下n的取值范围，
很明显x越小n越大，所以当x=2时，n最大为log2(y+1)。从第三个例子可以看出来，当x=y-1时，n最小为2。
所以有了n的取值范围我们就可以遍历所有可能的n，然后每次循环中y和n都是确定值，在对x使用二叉搜索确定其值即可。

另外一个需要注意的问题就是，因为本题中的数都比较大，所以要注意溢出问题，之前也做过一到这种题，
可以使用java内置的BigInteger类进行处理
"""

"""
First things first. Let's see the math behind it.

From given information, we can say one thing- Numbers will be of form-

n = k^m + k^(m-1) + ... + k + 1
=> n-1 = k^m + k^(m-1) + ... + k
=> n-1 = k (k^(m-1) + k^(m-2) + ... + k + 1) ...... [1]

Also, from n = k^m + k^(m-1) + ... + k + 1, we can say,
n-k^m = k^(m-1) + k^(m-2) + ... + k + 1 ...... [2]

from [1] and [2],

n-1 = k (n - k^m)
=>k^(m+1) = nk - n + 1

if you shuffle sides you will end up getting following form,

(k^(m+1) - 1)/(k - 1) = n .... [3]

Also from [1] note that, (n - 1) must be divisible by k.

We know that, n = k^m + k^(m-1) + ... + k + 1

=> n > k^m
=> m-th root of n > k .... [4]

[EDIT] -->

With inputs from @StefanPochmann we can also say, from binomial thorem, n = k^m + ... + 1 < (k+1)^m .... [5]
Therefore, k+1 > m-th root of n > k. .... from [4] and [5]
Thus ⌊m-th root of n⌋ is the only candidate that needs to be tested. [6]

<--

So our number should satisfy this equation where k will be our base and m will be (number of 1s - 1)

This brings us to the search problem where we need to find k and m.

Linear search from 1 to n does not work. it gives us TLE. So it leaves us with performing some optimization on search space.

From [6] we know that the only candidate that needs to be tested is, ⌊m-th root of n⌋

We also know that the smallest base is 2 so we can find our m must be between 2 and log2n else m is (n-1) [7]


"""


class Solution2:
    def smallestGoodBase(self, n):

        n = int(n)
        max_m = int(math.log(n, 2))  # Refer [7]
        for m in range(max_m, 1, -1):
            k = int(n ** m ** -1)  # Refer [6]
            if (k ** (m + 1) - 1) // (k - 1) == n:
                # Refer [3]
                return str(k)

        return str(n - 1)


class Solution3:
    def smallestGoodBase(self, n):
        n = int(n)
        max_len = len(bin(n)) - 2     # the longest possible representation "11111....1" based on k
        for m in range(max_len, 1, -1):
            lo = 2
            hi = n - 1     # or hi = int(pow(n, pow(m - 1, -1))) and only need check hi
            while lo <= hi:
                mid = (lo + hi) / 2
                num = (pow(mid, m) - 1) // (mid - 1)
                if num < n:
                    lo = mid + 1
                elif num > n:
                    hi = mid - 1
                else:
                    return str(mid)
        return str(n - 1)
