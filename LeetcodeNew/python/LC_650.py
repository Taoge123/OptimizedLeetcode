"""
题目大意
给定两种操作，复制和粘贴，每次复制只能复制写字板上存在的所有字符，每次粘贴也必须粘贴复制操作得到的所有字符。

给定一个初始的写字板上的字符’A’,问最少经过多少次操作（每次复制/粘贴分别算一次操作），写字板上’A’的个数才能为n。

解题方法
这道题可以转化成，给一个数字N，初始K=1，C=0然后只允许你有两种操作：

1、K = K + C （paste）
2 、C = K （copy all）

问，如何操作可以使得最快的得到N

N>1时，其实这道题就是将N分解为M个数字的乘积，且M个数字的和最小。

比如：

2 = 1 * 1 = 2
3 = 1 * 1 * 1 = 3
4 = 2 * 2 = 1 * 1 * 1 * 1 = 4


即求最快的把一个数分解为N个质数的和。

大神的解法，从小到大的去试探，尽量用小的数字去除就可以。
n = 6
A A A A A A
AA AA AA
AAA AAA

"""

"""
本题从题意上倾向于DP的解法。设计状态数组dp[n]表示恰好得到n个A的最小操作数。

我们思考dp[n]怎么得到。考虑到只有copy和paste两种模式，必然要求在得到n个A之前，纸面上必然是：有n/2个A，然后粘贴复制翻一番；或者有n/3个A，然后粘贴复制翻两番；
或者依次类推，直面上有n/j个A，然后粘贴复制翻倍j-1次。所以这就得到了dp[n]的更新表达式。dp[n] = min(dp[n/j]+j) for j=2,3,...,n.

当然，如果采用贪心的策略可以优化上面的解。例如，我们要得到6个A，直觉上通过3个A翻一番的方法，要比通过2个A翻两番的方法更高效，更是会比通过1个A拷贝粘贴翻五番更高效。
所以我们将j从小往大尝试，一旦遇到n/j整除的情况，就不再考虑其他j的可能性，取那样的j就能得到计算dp[n]的最优方案

https://leetcode-cn.com/problems/2-keys-keyboard/solution/cong-di-gui-dao-su-shu-fen-jie-by-fuxuemingzhu/

"""

import functools

"""
aaaaaa
"""

class Solution:
    def minSteps(self, n):
        @functools.lru_cache(None)
        def dfs(i, copied):
            if i == n:  # found a solution
                return 0
            if i > n or i + copied > n:  # won't lead to a solution, so we stop.
                return float('inf')

            # try pasting, if we have something to paste
            paste = 1 + dfs(i + copied, copied) if copied > 0 else float('inf')

            # try copying, if what we have on the board is > what we have copied
            copy_all = 1 + dfs(i, i) if i > copied else float('inf')

            return min(paste, copy_all)

        # start with 1 A on the board and 0 copied
        return dfs(1, 0)


class Solutionfuxuemingzhu:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        for i in range(2, n):
            if n % i == 0:
                return self.minSteps(n // i) + i
        return n



class SolutionDP:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[1] = 0
        for i in range(2, n+1):
            # 至少砍一半，最多砍成i份, j代表看成多少份， k代表每份多少个
            for j in range(2, i + 1):
                if i % j != 0:
                    continue
                k = i // j
                #需要另外(j-1)份，1是copy
                dp[i] = min(dp[i], dp[k]+1+j-1)
                break

        return dp[n]




class Solution2:
    def minSteps(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n //= i

        return res





class SolutionLee:
    def minSteps(self, n):
        if n == 1:
            return 0
        for i in range(2, n + 1):
            if n % i == 0:
                return self.minSteps(n // i) + i




"""
这道题只给了我们两个按键，如果只能选择两个按键，那么博主一定会要复制和粘贴，此二键在手，天下我有！！！果然，这道题就是给了复制和粘贴这两个按键，然后给了一个A，目标时利用这两个键来打印出n个A，注意复制的时候时全部复制，不能选择部分来复制，然后复制和粘贴都算操作步骤，问打印出n个A需要多少步操作。对于这种有明显的递推特征的题，要有隐约的感觉，一定要尝试递归和 DP。递归解法一般接近于暴力搜索，但是有时候是可以优化的，从而能够通过 OJ。而一旦递归不行的话，那么一般来说 DP 这个大杀器都能解的。还有一点，对于这种题，找规律最重要，DP 要找出状态转移方程，而如果无法发现内在的联系，那么状态转移方程就比较难写出来了。所以，从简单的例子开始分析，试图找规律：

当n = 1时，已经有一个A了，不需要其他操作，返回0

当n = 2时，需要复制一次，粘贴一次，返回2

当n = 3时，需要复制一次，粘贴两次，返回3

当n = 4时，这就有两种做法，一种是需要复制一次，粘贴三次，共4步，另一种是先复制一次，粘贴一次，得到 AA，然后再复制一次，粘贴一次，得到 AAAA，两种方法都是返回4

当n = 5时，需要复制一次，粘贴四次，返回5

当n = 6时，需要复制一次，粘贴两次，得到 AAA，再复制一次，粘贴一次，得到 AAAAAA，共5步，返回5

通过分析上面这6个简单的例子，已经可以总结出一些规律了，首先对于任意一个n(除了1以外)，最差的情况就是用n步，不会再多于n步，但是有可能是会小于n步的，比如 n=6 时，就只用了5步，仔细分析一下，发现时先拼成了 AAA，再复制粘贴成了 AAAAAA。那么什么情况下可以利用这种方法来减少步骤呢，分析发现，小模块的长度必须要能整除n，这样才能拆分。对于 n=6，我们其实还可先拼出 AA，然后再复制一次，粘贴两次，得到的还是5。分析到这里，解题的思路应该比较清晰了，找出n的所有因子，然后这个因子可以当作模块的个数，再算出模块的长度 n/i，调用递归，加上模块的个数i来更新结果 res 即可，参见代码如下：

"""
class SolutionSlow:
    def minSteps(self, n):
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i - 1, 0, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]


"""
下面这种方法是用 DP 来做的，我们可以看出来，其实就是上面递归解法的迭代形式，思路没有任何区别
"""
class SolutionSlow2:
    def minSteps(self, n):
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = i
            for j in range(i - 1, 0, -1):
                if i % j == 0:
                    dp[i] = dp[j] + i // j
                    break

        return dp[n]


"""
上面的解法其实可以做一丢丢的优化，在遍历j的时候，只要发现了第一个能整除i的j，直接可以用 dp[j] + i/j 来更新 dp[i]，然后直接 break 掉j的循环，之后的j就不用再考虑了，可能是因为因数越大，其需要的按键数就越少吧
"""
class SolutionFast:
    def minSteps(self, n):
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n //= i

        return res







