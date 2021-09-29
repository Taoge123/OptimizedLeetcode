"""
https://leetcode.com/problems/tallest-billboard/discuss/219700/Python-DP-clean-solution(1D)
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/956.Tallest-Billboard
https://leetcode-cn.com/problems/tallest-billboard/solution/yi-quan-ji-ben-mei-shuo-ming-bai-de-zhe-pian-kan-l/


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

"""
https://leetcode.com/problems/tallest-billboard/discuss/278332/Concise-Python-DFS-%2B-Memo
https://leetcode.com/problems/tallest-billboard/discuss/219700/Python-DP-clean-solution(1D)
https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)

It is like a knapsack problem.
Consider this problem as:
Given a list of numbers, multiply each number with 1 or 0 or -1, make the sum of all numbers to 0. Find a combination which has the largest sum of all positive numbers.

We can consider the sum as the key and positive number sum as the value.
We initally have dp[0] = 0

We iterate through the numbers and calculate the pairs that we got. In the case that we have same sum but different postive number sum, we only keep the largest postive number sum.

Let's run through a example, [1,2,3]
First we have {0:0}.
After 1, we have {0: 0, 1: 1, -1: 0}
After 2, we have {0:0, 2:2, -2:0, 1:1, 3:3,-1:1, -1:0,1:2,-3:0}
we will drop 1:1 and -1:0 since they have smaller value with the same key[1]and [-1]. That left us with {0:0, 2:2, -2:0, 3:3,-1:1,1:2,-3:0}
Number 3 is doing pretty much the same.
Then we will get the final result with dp[0]


"""

import functools


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        @functools.lru_cache(None)
        def dfs(i, diff):
            if i >= len(rods):
                if diff:
                    return float('-inf')
                return 0

            long = dfs(i + 1, diff + rods[i])

            # short=dfs(i+1,abs(rods[i]-diff))+min(rods[i],diff)
            short = 0
            if rods[i] > diff:
                short = dfs(i + 1, rods[i] - diff) + diff
            else:
                short = dfs(i + 1, diff - rods[i]) + rods[i]
            skip = dfs(i + 1, diff)

            return max(long, short, skip)

        return dfs(0, 0)


class SolutionTLE:
    def tallestBillboard(self, rods) -> int:
        @functools.lru_cache(None)
        def dfs(i, s1, s2):
            if i >= len(rods):
                if s1 == s2:
                    return s1
                else:
                    return 0

            return max(dfs(i + 1, s1, s2), dfs(i + 1, s1 + rods[i], s2), dfs(i + 1, s1, s2 + rods[i]))

        return dfs(0, 0, 0)


class SolutionEasy1:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for i in rods:
            old_dp = dp.copy()
            for k in list(old_dp.keys()):
                dp[k + i] = max(dp.get(k + i, 0), old_dp[k] + i)
                dp[k - i] = max(dp.get(k - i, 0), old_dp[k])
        return dp[0]


class Solution11:
    def tallestBillboard(self, rods) -> int:
        table = {0: 0}
        for rod in rods:
            new_dp = collections.defaultdict(int)

            for curSum, leftHeight in table.items():
                # add rod to the left bucket. Sum will increase since left bucket is
                # represented by positive numbers. Left support beam is longer now
                new_dp[curSum + rod] = max(new_dp[curSum + rod], leftHeight + rod)
                # add rod to the right bucket. Sum will decrease since right bucket is
                # represented by negative numbers. Left support beam is unchanged.
                new_dp[curSum - rod] = max(new_dp[curSum - rod], leftHeight)
                # discard rod. Sum and left support beam is unchanged
                new_dp[curSum] = max(new_dp[curSum], leftHeight)

            table = new_dp

        return table[0]



class Solution:
    def tallestBillboard(self, rods) -> int:
        @lru_cache(None)
        def dp(i, summ):
            if i == len(rods):
                if summ == 0:
                    return 0
                else:
                    return float('-inf')
            return max(dp(i + 1, summ),
                       dp(i + 1, summ - rods[i]),
                       dp(i + 1, summ + rods[i]) + rods[i])

        return dp(0, 0)



class SolutionTD:
    def tallestBillboard(self, rods) -> int:
        self.memo = collections.defaultdict(int)
        return self.dp(rods, 0, 0)

    def dp(self, rods, i, summ):
        if i == len(rods):
            if summ == 0:
                return 0
            else:
                return float('-inf')

        elif self.memo[(i, summ)]:
            return self.memo[(i, summ)]

        else:
            res = max(self.dp(rods, i + 1, summ),
                      self.dp(rods, i + 1, summ - rods[i]),
                      rods[i] + self.dp(rods, i + 1, summ + rods[i]))
            self.memo[(i, summ)] = res
            return res


rods = [1,2,3,4,5,6]
a = Solution()
print(a.tallestBillboard(rods))