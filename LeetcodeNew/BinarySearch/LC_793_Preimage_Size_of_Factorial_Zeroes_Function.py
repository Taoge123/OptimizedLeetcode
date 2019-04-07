
"""
http://www.cnblogs.com/grandyang/p/9214055.html
LeetCode 172. Factorial Trailing Zeroes

求阶乘得数末尾连续0的个数为K的所有整数的个数。

Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x,
and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2
because 11! = 39916800 has 2 zeroes at the end. Given K,
find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].
"""
"""
这道题的题目名称非常的难懂，但是读了题目内容以后，就不难理解了，定义函数f(x)为x!的末尾0的个数，
现在给了我们一个非负整数K，问使得f(x)=K成立的非负整数的个数。我们之前做过一道有关阶乘末尾零的个数的题Factorial Trailing Zeroes，
从那道里我们知道了末尾0其实是由2和5相乘为10得到的，而阶乘中2的数量远多于5的个数，所以10的个数就只取决于5的个数。
需要注意的一点就是，像25，125，这样的不只含有一个5的数字需要考虑进去。比如，24的阶乘末尾有4个0，
分别是5，10，15，20中的四个5组成的，而25的阶乘末尾就有6个0，分别是5，10，15，20中的各一个5，还有25中的两个5，
所以共有六个5，那么就不存在其阶乘数末尾有5个0的数。还有一个很重要的规律需要发现，我们知道20，21，22，23，24，
这五个数的阶乘数末尾零的个数其实是相同的，都是有4个，因为它们包含的5的个数相同。而19，18，17，16，15，
这五个数末尾零个数相同，均为3。那么我们其实可以发现，每五个数，必会至少多出1个5，有可能更多。
所以阶乘末尾零个数均为K个的x值，只有两种情况，要么是5，要么是0，这个规律得出来后，我们继续向着正确的解题方向前进。

基于之前那道题Factorial Trailing Zeroes的解法，我们知道了如何快速求一个给定的数字阶乘末尾零的个数，
那么我们只要找到了一个这样的数，其阶乘末尾零的个数等于K的话，那么就说明总共有5个这样的数，返回5，反之，
如果找不到这样的数字，就返回0。那么像这种选一个candidate数字，再进行验证的操作，用二分搜索法就是极好的，
属于博主的总结帖中LeetCode Binary Search Summary 二分搜索法小结的第四类，用子函数当作判断关系。
我们首先要确定二分搜索法的范围，左边界很好确定，为0就行了，关键是来确定右边界，我们来分析一下，
一个数字的阶乘末尾零个数为K，那么这个数字能有多大，就拿前面举的例子来说吧，末尾有4个0的最大数字是24，
有六个0的最大是29，那么我们发现它们都不会超过5*(K+1)这个范围，所以这就是我们的右边界，
注意右边界可能会超过整型数范围，所以要用长整型来表示。那么之后就是经典的二分搜索法的步骤了，
确定一个中间值mid，然后调用子函数来计算mid的阶乘数末尾零的个数，用来和K比较大小，如果想等了，直接返回5，
如果小于K，那么更新left为mid+1，反之，更新right为mid即可，最终没找到的话，返回0即可
"""
"""
解题思路：
n!后缀0的个数K，等于不大于n的所有乘数中，因子5的个数。

计算公式为：K = (n / 5) + (n / 25) + (n / 125) + ... + n / (5^k)

由等比数列前N项和公式得不等式：K <= n / 4

n从4 * K开始递增枚举 + 验证即可
"""
class Solution1 :
    def preimageSizeFZF(self, K):

        n = 4 * K
        t = 0
        while t <= K:
            t = self.trailingZeroes(n)
            n += 1
            if t == K: return 5
        return 0

    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans += n / x
            x *= 5
        return ans

"""
考虑125!有多少个0？实际上是求1 * 2 * 3 * … * 125 有多少个5。

1, 2, 3, 4, 5, ..., 125

考虑5的倍数，有
5, 10, 15, 20, ..., 125
可以得到125 / 5 = 25个5
此时剩下：
1, 2, 3, 5, ..., 25
还有5的倍数，同理得到25 / 5 = 5个5
依次类推，能够得到1 * 2 * 3 * ... * 125中5的个数。

于是：
可以求出<=K的上界 upper1
及<= K - 1的上界 upper2

ans = upper1 - upper2

"""


class Solution2:

    def count(self, num):
        cnt = 0
        while num:
            cnt += num // 5
            num //= 5
        return cnt

    def preimageSizeFZF(self, K):
        l, r = 0, 2 ** 63 - 1
        while l < r:
            mid = (l + r) // 2
            if self.count(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - l % 5 if self.count(l) == K else 0






