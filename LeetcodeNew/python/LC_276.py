"""

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1

"""

"""
https://leetcode.com/problems/paint-fence/solution/

276.Paint-Fence
这种排列组合的题，可能会想到是否有数学的解析方法．但解析方法往往也是由递归得到．所以不妨我们直接考虑递归或者ＤＰ的方法．

如果思考f(n)和f(n-1)的关系，那么解法就呼之欲出了．我们喷涂第ｎ个柱子，就是两种方案：和n-1的颜色一致，和n-1的颜色不一致．
对于前者，我们必须保证n-2和n-1的颜色已经不能相同了，而对于后者，我们允许n-2和n-1的颜色相同．
于是可以考虑dual status的ＤＰ方案，用same表示最近的两个柱子颜色一致的方案总数，diff表示最近的两个柱子颜色不一致的方案总数．

对于n，如果想喷涂和n-1一样的颜色，那么same(n)就要更新为diff(n-1)，颜色没有选择的余地

对于n，如果想喷涂和n-1不一样的颜色，那么diff(n)就要更新为[diff(n-1)+same(n-1)]*(k-1)，其中k-1表示颜色的选择种类．

上述的递归公式显示，我们只要不断更新两个状态变量same和diff即可．最后的答案就是两者之和．
"""


class SolutionTony:
    def numWays(self, n: int, k: int) -> int:
        memo = {}
        return self.dfs(n, k, memo)

    def dfs(self, n, k, memo):
        if n in memo:
            return memo[n]

        if n == 1:
            return k
        if n == 2:
            return k * k

        memo[n] = (k - 1) * (self.dfs(n - 1, k, memo) + self.dfs(n - 2, k, memo))
        return memo[n]




class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        same = [0] * n
        diff = [0] * n
        diff[0] = k

        for i in range(1, n):
            same[i] = diff[i - 1] * 1
            diff[i] = (same[i - 1] + diff[i - 1]) * (k - 1)

        return same[-1] + diff[-1]


class Solution1:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        same = 0
        diff = k
        total = k

        for i in range(2, n + 1):
            same = diff
            diff = (k - 1) * total
            total = same + diff
        return total




