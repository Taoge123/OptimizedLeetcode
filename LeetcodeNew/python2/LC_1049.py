
"""
Similar to 494. Target Sum
https://www.youtube.com/watch?v=oPgLkIwq9l0


[2,7,4,1,8,1]


1049.Last-Stone-Weight-II
任何对石块的操作，都可以表示成一系列包含绝对值的操作，比如 ||||a-b|-c|-d| - |e-f||，那么下一步就是根据每个绝对值符号内的正负情况，脱去绝对值改成括号，
并在前面相应地添加正负号，比如(((a-b)-c)-d)-(e-f)或者-(-(-(a-b)-c)-d)+(e-f)等等。然后再下一步就是脱去括号，必然会在每个单项式的前面标记一个正号或者负号，
比如+a-b+c+d-e+f之类的。


所以我们很容易想到，任何一种“对消石头”的操作，最终都会转换成一种给数组元素 a b c d e f前面添加正负号的策略。于是这就和494.Target-Sum非常相似了。
我们可以用DP找出所有正负号策略所能达到的target sum，最终答案就是求那个最小的且比零大的target sum.

需要特别注意的是，并不是所有的“添加正负号”的策略，都会有对应的“对消石头”的操作。比如+a+b+c+d+e+f就没有意义。但是我们所求的是最小的target （同时是正数），
这是可以证明一定存在对应的“对消石头”的操作的。

我们可以这么想：因为这样的target一定存在，假设是通过某一个序列XaXbXcXdXeYf得到的，其中X表示特定的正负号（我们不关心），
而最后一步的符号Y（就是元素f之前的那个）会是什么呢？如果是减号，岂不是说明这个target是可以通过两个正整数A-B相减得到的吗？其中A=XaXbXcXdXe，B=f，
这就意味着其实存在一种对消策略，可以通过最终的两块石头A和B再做一步对撞得到target。再看第二种情况，如果最后一步的符号Y是正号，
那说明其实存在一种对消策略可以得到最终的两块石头A和B，然后A+B=target，但再转念一想，我们此时做|A-B|的话岂不是能得到更小的结果吗？
这就和我们约定的那个target是最小的正数相矛盾了。所以结论是，对于我们所关注的最小的target，一定存在一系列操作XaXbXcXdXe-f=target，
即最后的结果一定是两个石头对撞实现的。


"""

import functools

class Solution:
    def lastStoneWeightII(self, stones) -> int:
        @functools.lru_cache(None)
        def dfs(i, sum1, sum2):
            if i >= len(stones):
                return abs(sum1 - sum2)

            left = dfs(i + 1, sum1 + stones[i], sum2)
            right = dfs(i + 1, sum1, sum2 + stones[i])

            return min(left, right)

        return dfs(0, 0, 0)



class Solution2D:
    def lastStoneWeightII(self, stones):
        @functools.lru_cache(None)
        def dfs(i, s):  # arguments are stone index and current sum
            if i == len(stones):  # end of array, return the current sum (abs)
                return abs(s)

            # try summing or subtracting each stone value
            add = dfs(i + 1, s + stones[i])
            minus = dfs(i + 1, s - stones[i])

            return min(add, minus)

        return dfs(0, 0)


class Solution2:
    def lastStoneWeightII(self, stones) -> int:

        dp = {0}
        for node in stones:
            newDP = dp
            dp = set()
            for x in newDP:
                dp.add(x + node)
                dp.add(x - node)

        res = float('inf')
        for num in dp:
            if num >= 0 and res > num:
                res = num

        return res






