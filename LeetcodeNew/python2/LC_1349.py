"""
https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/c-qiao-yong-wei-yun-suan-zhuang-tai-ya-suo-dp-by-e/
https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/xiang-jie-ya-suo-zhuang-tai-dong-tai-gui-hua-jie-f/
https://leetcode.com/problems/maximum-students-taking-exam/discuss/503686/A-simple-tutorial-on-this-bitmasking-problem

"""
"""
dp状态转移方程：
dp[i][j]表示第i行第j个状态下的最大学生数目,在该状态j满足一下情况的时候进行比较存储：
    1. j状态和题目所给的好坏座位不冲突(与运算为0)
    2. j状态下没有相邻的1(左右有人)(j本身和左、右移一位的结果与运算为0)
    3. j状态和上一行的k状态不冲突(j和k状态左、右移一位的结果与运算为0)
     这三点pumpkin大佬题解里画的图很好理解
    方程：dp[i][j]=max(dp[i][j],dp[i-1][k]+cnt1[j])上一行的k状态与本行1的个数(安排学生个数)的和
参数说明：
    1. dp[m+1][n],多一个虚拟的第0行,不用特例判断实际的第一行
    2. bit_seats[m+1],将1-m行的题目给出的好的座位转换为按位计算的数字，比如["#",".","#","#",".","#"]表示的就是二进制101101十进制45
    3. cnt1[] 储存1-最大可能状态的二进制中1的个数，比如101101中就有4个1
位运算解释：
    1.if(seats[i-1][j]=='#') bit_seats[i]|=1<<j; 如果当前i行第j个座位是#,那么第i行的二进制结果|=1<<j即加上1<<j
    2. cnt1[i]=cnt1[i>>1]+(i&1); 当前1的个数=除去最后一位(右移1)的1的个数+最后一位是否为1
"""

import functools

class SolutionTony:
    def maxStudents(self, seats) -> int:
        m, n = len(seats), len(seats[0])
        valid_seat = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    valid_seat[i] |= (1 << j)

        @functools.lru_cache(None)
        def dfs(state, i):
            m, n = len(seats), len(seats[0])
            if i == m:
                return 0

            res = 0
            for newState in range(1 << n):
                # 如果 cur座位 & valid座位 == cur座位， 说明都为1，都是valid座位，可以坐
                # 如果 cur座位 & cur座位左移一位 == 0， 说明cur座位没有相邻的
                # 如果 pre座位 & cur座位左移一位 == 0， pre座位 & cur座位右移一位 == 0 ， 说明cur没有和prev对角座位
                # check if there is no adjancent students in the row
                if (newState & valid_seat[i]) == newState and newState & (newState << 1) == 0:
                    # no students in the upper left positions and upper right positions
                    if (state << 1) & newState == 0 and (newState << 1) & state == 0:
                        res = max(res, self.count(newState) + dfs(newState, i + 1))
            return res
        return dfs(0, 0)

    def count(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


class Solution:
    def maxStudents(self, seats) -> int:
        m, n = len(seats), len(seats[0])
        dp = [[0 for i in range(1 << n)] for j in range(m + 1)]
        bit_seats = [0 for i in range(m + 1)]
        # count = [0 for i in range(1 << n)]

        # for i in range(1, 1<<n):
        #     count[i] = count[i>>1] + (i&1)

        for i in range(1, m + 1):
            for j in range(n):
                if seats[i - 1][j] == '#':
                    bit_seats[i] |= 1 << j

        for i in range(1, m + 1):
            for j in range(1 << n):
                if not (j & bit_seats[i]) and not (j & j << 1) and not (j & j >> 1):
                    for k in range(1 << n):
                        if not (j & k >> 1) and not (j & k << 1):
                            dp[i][j] = max(dp[i][j], dp[i - 1][k] + bin(j).count('1'))

        return max(dp[m])


class SolutionDFS:
    def maxStudents(self, seats) -> int:
        m, n = len(seats), len(seats[0])
        table = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    table[i] |= (1 << j)
                else:
                    table[i] |= 0
        memo = {}
        return self.dfs(seats, 0, 0, table, memo)

    def dfs(self, seats, state, pos, table, memo):
        m, n = len(seats), len(seats[0])
        if (state, pos) in memo:
            return memo[(state, pos)]

        if pos == m:
            return 0

        res = 0
        for newState in range(1 << n):
            # check if there is no adjancent students in the row
            if (newState & table[pos]) == newState and newState & (newState << 1) == 0:
                # no students in the upper left positions and upper right positions
                if (state << 1) & newState == 0 and (newState << 1) & state == 0:
                    res = max(res, self.count(newState) + self.dfs(seats, newState, pos + 1, table, memo))
        memo[(state, pos)] = res
        return memo[(state, pos)]

    def count(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count




seats = [["#",".","#","#",".","#"],
        [".","#","#","#","#","."],
        ["#",".","#","#",".","#"]]

a = Solution()
print(a.maxStudents(seats))



