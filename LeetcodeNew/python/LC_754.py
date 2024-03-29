"""
https://leetcode.com/problems/reach-a-number/solutions/1865182/solving-using-recursion/

754.Reach-a-Number
此题在数学方法上有巧妙的思路．

假设目标是11，我们自然会尝试+1+2+3+4+5...这样尝试下去，发现这样操作了５次，之后得到的是15，超过了目标11，多了4，该怎么办呢？其实策略非常简单，我们将刚才的操作里面的+2变成-2，一正一反就降了４．
也就是说+1-2+3+4+5，就能得到11．显然，这样的操作肯定是最简洁的了．所以我们的基本思路就是，+1+2+3...一路不停地加过去，一旦sum超过了target，
那么我们就将之前＂加上＂的(sum-target)/2这个数，改为＂减去＂即可．

那么我们自然会问，如果target是12，当我们将sum加到15的时候，相差是3，不是二的倍数怎么办呢？解决方法是：我们就继续累加+6+7，将sum积累到28．此时sum和target之间的差是16，看上去终于是偶数了。
但是，我们又发现，28是从1累加到7的结果，似乎没有办法再减去一个-8，怎么办呢？事实上，遇到这种情况下，我们不需要最后一步加上7，而是减去7，此时得到的sum是14，与target之间的差是2，
这就提示我们此时再将+2改动成-2即可。

综上可以分析得到，我们从+1,+2,...开始不断地往上累加，当sum恰超过target时，最多再多加两次，一定能保证sum-target是偶数。只要这个差是偶数，就一定保证能有一个解决方案（类似第一段或者第二段的方法）来实现．

"""

"""
target = 15
1 2 3 4 5 6 7
1 3 6 10 15-13 = 2, 所以可以调整1成为-1

1 -1 2 6 11
-1 1 4 8 13

if k is even -> good
if k is odd: -> no good


"""

import functools

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        summ = 0
        i = 0
        while not (summ >= target and (summ - target) % 2 == 0):
            i += 1
            summ += i
        return i


class SolutionTest:
    def reachNumber(self, target: int) -> int:
        self.count = 0
        @functools.lru_cache(None)
        def dfs(i, step, target):
            self.count += 1
            print(self.count)
            if i == target:
                return step
            # if abs(i) > target:
            #     return float('inf')
            if abs(i) > 2 * abs(target):
                return float('inf')
            step += 1
            print(i, step, target)
            if (i + step == target):
                return step
            right = dfs(i + step, step, target)
            left = dfs(i - step, step, target)
            return min(left, right)

        return dfs(0, 0, abs(target))


target = -1000000000
a = SolutionTest()
print(a.reachNumber(target))


