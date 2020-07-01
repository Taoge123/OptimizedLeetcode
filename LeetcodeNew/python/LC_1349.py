"""
https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/c-qiao-yong-wei-yun-suan-zhuang-tai-ya-suo-dp-by-e/
https://leetcode-cn.com/problems/maximum-students-taking-exam/solution/xiang-jie-ya-suo-zhuang-tai-dong-tai-gui-hua-jie-f/

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




seats = [["#",".","#","#",".","#"],
        [".","#","#","#","#","."],
        ["#",".","#","#",".","#"]]

a = Solution()
print(a.maxStudents(seats))



