"""
https://leetcode.com/problems/maximize-grid-happiness/discuss/936081/C%2B%2B-5D-DP


1659.Maximize-Grid-Happiness
我们看到这题里的维度m和n出奇地小，竟然不超过5，就有预感算法可能和暴力枚举有关，必然不用考虑去人工设计最优解。

分析矩阵的每个位置有三种可能：不放人、内向人、外向人，因此25个格子的话就会有3^25种可能，这个数据量仍然太大。这个时候我发现3^5=243很小，立刻想到了类似1349. Maximum Students Taking Exam的做法，就是以整行为状态进行枚举，似乎是个可行的思路：因为当前行某种状态对应的最优值，只与上一行状态有关（也就是内向人、外向人的各种相邻关系），而与再前一行就无关了。

于是首先就能想到设计dp[i][state]，表示第i行的安排为state时能够得到的最优值，其中state是一个三进制的整数，每个bit上为0时表示不放人，为1时表示放外向人，为2时表示放内向人。状态转移方程就是考察当前行状态state与上一行状态prevState之间的制约关系。即

for (int i=1; i<=m; i++)
  for (int state = 0; state < (1<<m); state++)
  {
      for (int prevState = 0; prevState < (1<<m); prevState++)
        dp[i][state] = max(dp[i][state] + addVal(prevState, state);
  }
其中addVal(prevState, state)表示在前一行是prevState的方案的基础上，当前行安排为state的话，可以增加多少价值。这些价值的来源产生自这些：

当前行的外向人基本分，如果左、上、右有人相邻的话，额外加分
当前行的内向人基本分，如果左、上、右有人相邻的话，额外减分
上一行的外向人如果下邻居有人，那么要额外加分
上一行的内向人如果下邻居有人，那么要额外减分
但是以上的算法有一个漏洞，那就是我们有外向人、内向人总人数的制约。dp[i][state]并不能看出外向人、内向人的总人数是否已经爆了。所以我们要额外增加两个维度x,y，用dp[i][x][y][state]表示当前第i行采用state的方案，并且截止目前外向人总数是x、内向人总数是y时，能够收获的最大值。因此更新dp[i][x][y][state]时，要先计算出当前行的外向人和内向人的人数a与b，仅枚举合法的dp[i-1][x-a][y-b][prevState]来更新dp[i][x][y][state]。其中要求x>=a，y>=b。

最终的答案是遍历到最后一行时dp[m][x][x][x]的最大值，其中x都可以任意。
"""

"""
3 ^ 5 = 243
dp[i][state] : the maximum value if you arrange the ith row as state

for i in range(m+1):
    for state in range(3^n):
        for preState in range(3^n):
            dp[i][state] = max(dp[i][state], dp[i-1][prevState] + addVal(preState, state))

addVal(preState, state)
1. extra base + additional gain due to neighbors
2. intro base - additional gain due to neighbors
3. additional gain for the extra in last row
4. additional loss for the intro in last row

dp[i][x][y][state] : the maximum value if you arrange the ith row as state, & used intro as x, used extro as y

for i in range(1, m+1):
    for x in range(introvertsCount):
        for y in range(extrovertCount):
            for state in (3^n):
                for preState in (3^n):
                    dp[i][x][y][state] = max(dp[i][x][y][state], dp[i-1][x-a][y-b][prevState]) + addVal(preState, state)

OK, tracking people in the grid is costly, and you will get TLE if you do not use memoisation.

I saw several solutions that cheat on large test cases.

Fortunately, to calculate the happiness balance - how placing a person subtracts or adds to the overall happiness - we only need to know last m cells we processed.

We can use bit masks to track introverts and extroverts in the last m cells, and shift them as we go. Thus, we have here 5D DP:

Position in the grid (p = i * m + j) -> up to 25.
Remaining introverts -> up to 6.
Remaining extroverts -> up to 6.
Introverts mask -> up to 2 ^ (m + 1) - 1 = 63 combinations.
Extroverts mask -> up to 2 ^ (m + 1) - 1 = 63 combinations.



great solution. took me quite a while to understand. for those who also have trouble, there's more explanation:

we search all possible placements of introvert, extrovert or empty of each cell in the grid
we place people from top to bottom, left to right. each position can be identified by p, which is [0,24]. The row(i) and column(j) is therefore i = p / n, j = p % n
first we consider leaving current cell empty int res = dfs(m, n, p + 1, in, ex, n_mask_in, n_mask_ex);
3.1 if current cell is empty, then the score is simply decided by what we do in next cell
second, we consider placing introvert at current cell if there's still introvert people left (if (in > 0) {...})
4.1 (see below)
last, similar to #4, we consider extrovert people (if (ex > 0) {...})
5.1 (see below)
in the process, we use max to keep the max happiness score
let's discuss 4.1 (5.1 is very similar). if we place introvert people at (i, j), we get 120 but also need to subtract 30 for any people surrounding. This is what nCost does.

First, mask_in is the placement of introvert people in the last m cells. For example, if we have m=3, n=3, i=1, j=0, then mask_in=101 means

i 0 i
x ? ?
? ? ?
x is where we're currently at.
? is cell we haven't processed yet.
i is we place introvert people there.

so nCost is basically to check if the left or up cell of current cell is empty or not. If empty, then we d-30 if we place introvert people at current cell (need to double the penalty due to mutual repulsion).

once we calculate the cost of placing, we just need to add on top of it the cost of placing for the rest cells. we just need to increment position index p+1, decrement introvert people number, and then shift the bitmask by accounting for current placement diff + dfs(m, n, p + 1, in - 1, ex, n_mask_in + 1, n_mask_ex)

That's all.

"""

import functools


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        def cost(row, col, in_state, ex_state, val):
            res = 0
            up = 1 << (n - 1)
            if col > 0 and (in_state & 1):
                res += val - 30
            if row > 0 and (in_state & up):
                res += val - 30
            if col > 0 and (ex_state & 1):
                res += val + 20
            if row > 0 and (ex_state & up):
                res += val + 20
            return res

        N = (1 << n) - 1

        @functools.lru_cache(None)
        def dfs(pos, i, j, in_state, ex_state):
            row = pos // n
            col = pos % n
            if row >= m:
                return 0

            in_newState = (in_state << 1) & N
            ex_newState = (ex_state << 1) & N
            res = dfs(pos + 1, i, j, in_newState, ex_newState)
            if i < introvertsCount:
                res = max(res, dfs(pos + 1, i + 1, j, in_newState + 1, ex_newState)
                          + cost(row, col, in_state, ex_state, -30) + 120)
            if j < extrovertsCount:
                res = max(res, dfs(pos + 1, i, j + 1, in_newState, ex_newState + 1)
                          + cost(row, col, in_state, ex_state, 20) + 40)
            return res

        return dfs(0, 0, 0, 0, 0)

















