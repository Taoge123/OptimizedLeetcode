
"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.


Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”


Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""

"""
本题本质就是0-1背包问题，只不过cost变成了两个量。0-1背包问题已经有非常成熟的套路了。dp[i][j]表示用i个0和j个1最多可以拼出多少个完整的字符串。

        for (int k=0; k<strs.size(); k++)  //遍历所有的字符串
        {
            检查当前字符串strs[k]，得到有zeros个0，ones个1;
                            
            auto temp=dp;
            for (int i=zeros; i<=m; i++)
             for (int j=ones; j<=n; j++)
             {
                 dp[i][j]=max(temp[i][j],temp[i-zeros][j-ones]+1);
                 //在循环体里更新所有的dp[i][j]。
                 //这里用了一个temp来保存上一轮（即处理上一个字符串时）的dp
                 //对于当前的字符串，有两种选择，要么不加入，则dp[i][j]不变；要么加入，则更新为temp[i-zeros][j-ones]+1                
             }            
        }
这里用temp的原因是方便起见，以免更新dp时使用了这一轮的新dp值。当然，也有取巧的办法省下temp的开辟，
即在两个内存for循环里将i，j都按从大到小遍历，那么更新dp时就不会与新值冲突。

Leetcode Link
"""


import copy
import collections



class SolutionTD:
    def findMaxForm(self, strs, m, n):

        N = len(strs)
        memo = collections.defaultdict(lambda: -1)
        count = [(s.count('0'), s.count('1')) for s in strs]

        def dfs(i, m, n):
            if m < 0 or n < 0:
                return float('-inf')
            if i >= N:
                return 0
            if memo[(i, m, n)] == -1:
                a, b = count[i]
                val = max(dfs(i + 1, m, n), 1 + dfs(i + 1, m - a, n - b))
                memo[(i, m, n)] = val
            return val

        return dfs(0, m, n)


class SolutionTLE:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for i in range(m + 1)]
        newDP = copy.deepcopy(dp)

        for k in range(len(strs)):
            ones, zeros = 0, 0
            for char in strs[k]:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1
            for i in range(zeros, m + 1):
                for j in range(ones, n + 1):
                    newDP[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

            dp = copy.deepcopy(newDP)
        return dp[m][n]



class Solution:
    def findMaxForm(self, strs, m, n):

        dp = [[0] * (n+1) for i in range(m+1)]

        for s in strs:
            zero, one = self.count(s)
            print(zero, one)
            for x in range(m, -1, -1):
                for y in range(n, -1, -1):
                    if x >= zero and y >= one:
                        dp[x][y] = max(dp[x][y], dp[x - zero][y - one] + 1)

        return dp[m][n]

    def count(self, s):
        return sum(1 for char in s if char == '0'), sum(1 for char in s if char == '1')




strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3

a = Solution()
print(a.findMaxForm(strs, m, n))




