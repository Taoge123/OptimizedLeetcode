
"""

https://www.youtube.com/watch?v=zd20HrEb5dg&feature=youtu.be


类似的DP题目还有：
714.Best-Time-to-Buy-and-Sell-Stock-with-Transaction-Fee
487.Max Consecutive Ones II
376.Wiggle Subsequence
只不过用两个状态变量就够了.


Given a positive integer n, return the number of all possible attendance records with length n,
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
"""


# https://leetcode.com/problems/student-attendance-record-ii/discuss/101634/Python-DP-with-explanation

"""
552.Student-Attendance-Record-II
此题明显要用DP，但是如何设计状态和状态转移方程都非常难想。但最终的解法其实也非常巧妙，原来用到了多元状态的转移。

任何一种排列，可以归结为六种状态：dp00,dp01,dp02,dp10,dp11,dp12. 状态dp_ij的定义是：
其中i表示这个数列里absence出现的次数，显然对于一个valid的数列，i的范围只能是0和1；
j表示这个数列里末尾连续出现late的次数，显然对于一个valid的数列，i的范围只能是0，1，2。因此有六种状态的定义。

显然我们可以发现，随着record长度的增加，序列的状态就是在这六种之间转移。规律如下：

新状态       旧状态
dp02[i]  =  do01[i-1]  // 加'L'转变而来
dp01[i]  =  dp00[i-1]  // 加'L'转变而来
dp00[i]  =  dp00[i-1]+dp01[i-1]+dp02[i-1] // 分别加'P'转变而来
dp12[i]  =  dp11[i-1]  // 加'L'转变而来
dp11[i]  =  dp10[i-1]  // 加'L'转变而来
dp10[i]  =  dp10[i-1]+dp11[i-1]+dp12[i-1]+dp00[i-1]+dp01[i-1]+dp02[i-1] // 前三种加'P'转变而来，后三种加'A'转变而来
当然，因为dp**[i]的状态只取决于dp**[i-1]，所以也可以不用设置六个一位数组，节省一点空间。

另外，唯一需要需要注意的边界条件是dp00[0]=1
"""




class Solution:
    def checkRecord(self, n):
        M = 1000000007
        if n == 0:
            return 0
        if n == 1:
            return 3
        nums = [1, 1, 2]
        for i in range(2, n):
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % M)

        res = (nums[n] + nums[n - 1] + nums[n - 2]) % M
        for i in range(n):
            res += nums[i + 1] * nums[n - i] % M
            res %= M

        return res



class Solution2:
    def checkRecord(self, n: int) -> int:
        M = 1000000007
        PorL = [0] * (n + 1)
        P = [0] * (n + 1)
        PorL[0] = P[0] = 1
        # 只有一堂课
        PorL[1] = 2
        P[1] = 1

        for i in range(2, n + 1):
            P[i] = PorL[i - 1]
            # 上一个可以是P， LP, LLP
            PorL[i] = (P[i] + P[i - 1] + P[i - 2]) % M

        res = PorL[n]
        for i in range(n):
            insertA = (PorL[i] * PorL[n - 1 - i]) % M
            res = (res + insertA) % M

        return res




