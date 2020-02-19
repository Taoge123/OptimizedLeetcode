
"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.

https://blog.csdn.net/baidu_23318869/article/details/50386323

解题思路：
数学题，答案等于int(math.sqrt(n))

对于第i栈灯泡，当i的因子个数为奇数时，最终会保持点亮状态，例如9的因子为1，3，9
而当i的因子个数为偶数时，最终会保持熄灭状态，例如8的因子为：1，2，4，8
当且仅当i为完全平方数时，其因子个数为奇数
为什么只有完全平方数的因子个数为奇数呢？

因为除了完全平方数，其余数字的因子都是成对出现的，而完全平方数的平方根只会统计一次。

前10盏灯泡的开闭过程如下所示：

0 0 0 0 0 0 0 0 0 0    0
1 1 1 1 1 1 1 1 1 1    1
1 0 1 0 1 0 1 0 1 0    2
1 0 0 0 1 1 1 0 0 0    3
1 0 0 1 1 1 1 1 0 0    4
1 0 0 1 0 1 1 1 0 1    5
1 0 0 1 0 0 1 1 0 1    6
1 0 0 1 0 0 0 1 0 1    7
1 0 0 1 0 0 0 0 0 1    8
1 0 0 1 0 0 0 0 1 1    9
1 0 0 1 0 0 0 0 1 0    10

"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** (1/2))


class Solution2:
    def bulbSwitch(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            numSwitch = self.helper(i)
            if numSwitch % 2 == 1:
                count += 1
        return count

    def helper(self, n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        return count



n = 10
a = Solution2()
print(a.bulbSwitch(n))



