"""
https://leetcode.com/problems/tallest-billboard/discuss/219700/Python-DP-clean-solution(1D)
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/956.Tallest-Billboard

背包解法:
dp[left][right]

for i in range(n):
    leg = rod[i]
    for left in in range(2500):
        for right in range(2500):
        if dp[left][right] == True:
            dp[left+len][right] = True
            dp[left][right+len] = True
            if left+len == right:
                res = left + len
            if left == right+len:
                res = right + len

Since we just wanna see if left ~== right, we can track their diff and see if its close to 0

Optimization
dp[diff] = max{ Left | s.t Left-Right = diff}

也就是说，我们在当前这一轮中，dp[diff]表示当前所有left-right==diff的配对中，最大的那个Left（相应Right其实也可以确定下来）

如何更新状态呢？假设我们已经有了dp[diff]=left，现在要考察rods[i]，这个棍子有三种选择：

1.我们不使用这根棍子，所有的diff都不受影响，故dp[diff]不变。

2.我们将这根棍子加在left上，那么diff就会变大，我们就可能需要更新diff+rods[i]对应的dp,而这个对应的dp值就是left+rods[i]。

3.我们将这根棍子加在right上，那么diff就会变小，我们就可能需要更新diff-rods[i]对应的dp,而这个对应的dp值依然是left（因为左棍的长度不变）。

需要注意的是，以上的更新只有在left存在的情况下进行。也就是说，需要保证dp[diff]=left有意义。
初始化时，只有dp[0]=0,表示初始状态下高度差为0的方案就是left=0,right=0; 其他所有的dp[diff]都标记为-1，表示目前非法。

另外，需要注意，diff的范围是[-5000,5000]，但是dp[diff]数组的index不能是负数。我们在处理下标时需要一个偏移量5000。

"""

from functools import lru_cache
import collections


class Solution:
    def tallestBillboard(self, rods) -> int:
        @lru_cache(None)
        def dp(i, summ):
            if i == len(rods):
                if summ == 0:
                    return 0
                else:
                    return float('-inf')
            return max(dp(i + 1, summ), dp(i + 1, summ - rods[i]), dp(i + 1, summ + rods[i]) + rods[i])

        return dp(0, 0)




class SolutionTD:
    memo = collections.defaultdict(int)
    def tallestBillboard(self, rods) -> int:
        n = len(rods)
        return self.dp(rods, 0, 5000)

    def dp(self, rods, i, summ):
        if i == len(rods):
            if summ == 5000:
                return 0
            else:
                return float('-inf')

        elif self.memo[(i, summ)]:
            return self.memo[(i, summ)]

        else:
            res = self.dp(rods, i + 1, summ)
            res = max(res, self.dp(rods, i + 1, summ - rods[i]))
            res = max(res, rods[i] + self.dp(rods, i + 1, summ + rods[i]))
            self.memo[(i, summ)] = res
            return res


rods = [1,2,3,4,5,6]
a = Solution()
print(a.tallestBillboard(rods))