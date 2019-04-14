
"""
https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/196939/Easy-to-understand-solution-with-detailed-explanation
https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/168289/Share-my-O(N3)-greater-O(N2)-C%2B%2B-DP-solution.-Including-the-thoughts-of-improvement.
https://leetcode.com/problems/valid-permutations-for-di-sequence/discuss/186571/Python-O(N3)O(N2)-time-O(N)-space-DP-solution-with-clear-explanation-(no-%22relative-rank%22-stuff)
https://zhanghuimeng.github.io/post/leetcode-903-valid-permutations-for-di-sequence/



if(S[i-1] == 'D')
   dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + ... + dp[i-1][i-1]

if(S[i-1] == 'I')
   dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]


We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.

Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.

"""

"""
Intuition:

This the only problem this week that I feel like writing a solution.
But don't know how to explain.

dp[i][j] means the number of possible permutations of first i + 1 digits,
where the i + 1th digit is j + 1th smallest in the rest of digits.

Ok, may not make sense ... Let's see the following diagram.

I take the example of S = "DID".
The permutation can start from 1, 2, 3, 4.
So dp[0][0] = dp[0][1] = dp[0][2] = dp[0][3] = 1.
In the parenthesis, I list all possible permutations.

We decrese from the first digit to the second,
the down arrow show the all possibile decresing pathes.

The same, cause we increase from the second digit to the third,
the up arrow show the all possibile increasing pathes.

dp[2][1] = 5, mean the number of permutations
where the third digitis the second smallest of the rest.
We have 413,314,214,423,324.
Fow example 413, where 2,3 are left and 3 the second smallest of them.

Explanation:
As shown in the diagram,
for "I", we calculate prefix sum of the array,
for "D", we calculate sufixsum of the array.

Time Complexity:
O(N^2)
"""
"""
Here is how to come up with this solution from the question.

Consider using dynamic programming to solve this problem.Thus we need to find how to trans a problem to a sub-problem:
In a naive way, dp[i]:the total possible permutations count of first i+1 digits
how can dp[i] relate with dp[i-1]? what is the relationship between them? we couldn't find. So try to add some parameter.
denote j as the i+1th digit is the j+1th smallest number in the rest not-yet-select digits.
so :dp[i][j]:the total possible numbers of first i+1 digits, where i+1th digit is the jth smallest number in the rest not-yet-select digits.
In such way, we can find out the relationship between problem and its sub-problem: if we add a digit k as the first ith digit, and S[i]=='I', 
we know that we can only add those digit which bigger than k as the first i+1th digit, i.e., dp[i][j] can only form those dp[i][w], where w>=j.
example: S="DID", and we choose digit 2 as the first digit, then when choosing the second digit, 
we can only choose those bigger than 2 because we need "increase". 
So we choose 3 and 4, noticing that 3 and 4 is the 2nd smallest and 3rd smallest in the rest non-select-yet digit [1,3,4].
"""
"""
其中dp[i][j]表示从{0,1,2,3}中取i+1个数字时（即排列序列的前i+1个数），
第i+1个数为剩余的数字中第j+1小的数字的排列方法数量。括号内为排列方式。

观察上图中的连线，可以总结规律：
当第i个数对应的字符为D时，dp[i+1][j]=dp[i][j+1]+dp[i][j+2]+...+dp[i][n-1-i]；
当第i个数对应的字符为I时，dp[i+1][j]=dp[i][j]+dp[i][j-1]+...+dp[i][0]；
当i=0时，dp[i][j]=1；

"""

class SolutionLee:
    def numPermsDISequence(self, S):
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)

class Solution1:
    def numPermsDISequence(self, S):
        def dp(i, j):
            if (i, j) in self.dic:
                return self.dic[(i, j)]

            if i == n:
                return 1

            if S[i] == 'D':
                self.dic[(i, j)] = sum([dp(i + 1, k) for k in range(j)])

            if S[i] == 'I':
                self.dic[(i, j)] = sum([dp(i + 1, k) for k in range(j, n - i)])

            return self.dic[(i, j)]

        n = len(S)
        self.dic = dict()
        return sum([dp(0, i) for i in range(n + 1)]) % (10 ** 9 + 7)


"""
Before diving into the state transition function, let us first start with a simple example.

1. a simple example
In the following discussion, for simplification, I will use both notation DI-seq and DI-rule instead of DI sequence.

Consider a permutation 1032, which is based on a DI-seq "DID", how to use it to construct a new instance ending at 2 and based on DI-seq "DIDD"?

Method:
step 1.
for the original permutation 1032, we add 1 to the digits that are larger than or equal to 2.

    1032->1043
      ^^
step 2.
then directly append 2 to 1043, i.e., 1043 -> 10432

Remark on step 1:
(1) By performing add operation, 2 in the original permutation now becomes 3, and thus there is no duplicate element for the new arrival 2.
(2) More importantly, such operation on the digits will not break the original DI-rule. e.g., 1043 still keeps its old DI-rule, i.e., "DID". 
The proof is straight-forward, you can validate yourself.

Now a new permutation with DI-rule "DIDD" and ending at 2 has been constructed from 1032, namely 10432.

With the same spirit, using 1032("DID"), we can construct instances with DI-rule "DIDD": 20431(ending with 1), 21430(ending with 0).
(Note that the instance(based on "DIDD") which ends with 3 can not be constructed.)

Similarly, from 1032("DID"), we can construct instances with DI-rule "DIDI": 10423(ending with 3), 10324(ending with 4).
(Note that the instance(based on "DIDI") which ends with 1 or 2 can not be constructed.)

2. state transition function
With the example above in mind, the transition function seems to be clear.

Given a string DI-seq S, let dp[i][j] represents the number of permutation of number 0, 1, ... , i, satisfying DI-rule S.substr(0, i), and ending with digit j.

if(S[i-1] == 'D')
   dp[i][j] = dp[i-1][j] + dp[i-1][j+1] + ... + dp[i-1][i-1]

if(S[i-1] == 'I') 
   dp[i][j] = dp[i-1][0] + dp[i-1][1] + ... + dp[i-1][j-1]
   
   
class Solution {
public:
    int numPermsDISequence(string S) {
        int n = S.size(), m = 1e9 + 7;
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        dp[0][0] = 1;
        for(int i = 1; i <= n; i++)
            for(int j = 0; j <= i; j++)
                if(S[i-1] == 'D')
                    for(int k = j; k <= i-1; k++)
                        dp[i][j] = dp[i][j]%m + dp[i-1][k]%m;
                else
                    for(int k = 0; k <= j-1; k++)
                        dp[i][j] = dp[i][j]%m + dp[i-1][k]%m;
        int res = 0;
        for(int i = 0; i <= n; i++)
            res = res%m + dp[n][i]%m;
        return res%m;
    }
};
   
   
"""
class Solution2:
    def numPermsDISequence(self, S):
        l, r = 0, len(S)+1
        dp =  [1] * r
        for j in S:
            new = [0] * r
            if j == 'D':
                r -= 1
                for u in range(r-1,l-1,-1):
                    new[u] = new[u+1] + dp[u+1]
            elif j == 'I':
                l += 1
                for u in range(l,r):
                    new[u] = new[u-1] + dp[u-1]
            dp = new
        return dp[l] % (10 ** 9 + 7)


class Solution3:
    def numPermsDISequence(self, S):
        dp = [1 for c in range(len(S) + 1)]
        dp2 = [0 for c in range(len(S) + 1)]

        for i in range(1, len(S) + 1):
            if S[i - 1] == 'D':
                for j in range(i + 1):
                    dp2[j] = sum(dp[j:i])
            else:
                for j in range(i + 1):
                    dp2[j] = sum(dp[:j])
            dp, dp2 = dp2, dp

        return sum(dp) % 1000000007


"""
思路：

猜到了有O(N^3)的DP解法，

注意到了用1-3填和用2-4填的个数是一样

但还是没有想到状态转移方程（也就是DP数组的含义）

为了能进行状态转移，定义dp[i][j]表示：使用1-i这些数字的情况下，以j结尾的合理数组个数，计算dp[i][j]的过程如下：

1. 如果s[i-2]=='D'，说明第i-1位的数要比j大，第i-1位的数据范围是[j+1,i]，j在第i位上，
   所以就把大于等于j的数都往左shift一位（这样2者是等价的，满足A一定满足B，满足B一定满足A），
   这样前i-1位就又是连续的[1,i-1]，就可以继续用DP数组的含义。具体到代码就是，k的范围是range(j,i)，而不是range(j+1,i)

2. 如果s[i-2]=='I'，数字i不在前i-1位，不用shift
"""


class Solution4:
    def numPermsDISequence(self, s):
        mod = 10 ** 9 + 7
        n = len(s) + 1
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        dp[1][1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                if s[i - 2] == 'D':
                    for k in range(j,
                                   i):  # here start from j, regard as swap value j with i, then shift all values no larger than j
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
                else:
                    for k in range(1, j):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
        #        print(dp)
        return sum(dp[n]) % mod


"""
二、题目分析
  根据题意，我们需要对从0开始的连续整数 { 0, 1, ..., n } 进行排列，使之符合输入的 DI 字符串（长度为 n ），输出总的符合要求的排列数，这里先把关于长度为 n 的 DI 字符串的问题记作 nDI 。

  这道题我们可以用动态规划的思想，从分解原问题着手，来看看 (i-1)DI 和 iDI 的关系。下面使用 res[i][j] ( j <= i ) 表示 { 0, 1, ..., i } 中长度为 i+1 ，并以数字 j 作为最后一个数字的排列的数量。

 

当下一个即第 i 个字符为 D 时，首先显然，某个数字 j 只能排在 j+1、j+2 … i-1 之后，
故我们有 res[i][j] = res[i-1][j+1] + res[i-1][j+2] + ... + res[i-1][i-1] 。
当然这可能会出现数字重复的问题，但由于增加了新的数字 i ，所以在原来的排列的基础上我们能够对数字做出一些调整，即将大于等于 j 的数字全部加一，
就可以在末尾再放上数字 j 。如此一来， res[i-1][j] 所代表的排列也能够算到这里，所以最后我们有

  res[i][j] = res[i-1][j] + res[i-1][j+1] + res[i-1][j+2] + ... + res[i-1][i-1]
1
e.g. 排列 1, 4, 2, 0, 3 ，下一个字符为 D ，当要在末尾加上 3 的时候，我们将原排列中大于等于 3 的数加一，再加上 3 ，可得排列 1, 5, 2, 0, 4, 3 。
e.g. 排列 0, 3, 2, 1, 4 ，下一个字符为 D ，当要在末尾加上 0 的时候，我们将原排列中大于等于 0 的数加一，再加上 0 ，可得排列 1, 4, 3, 2, 5, 0 。
 

当下一个即第 i 个字符为 I 时，与 D 的情况相反，某个数字 j 只能排在 j-1、j+2 … 0 之后，故我们有 res[i][j] = res[i-1][j-1] + res[i-1][j-2] + ... + res[i-1][0] 。
同样，当数字重复出现时将大于等于 j 的数字加一再在末尾放上数字 j 。当然，若 j = 0 ，res[i][j] = 0 。所以排除0的情况我们有

  res[i][j] = res[i-1][j-1] + res[i-1][j-2] + ... + res[i-1][0]
1
e.g. 排列 1, 4, 2, 0, 3 ，下一个字符为 I ，当要在末尾加上 4 的时候，我们将原排列中大于等于 4 的数加一，再加上 4 ，可得排列 1, 5, 2, 0, 3, 4 。
最后再说明一下，当下一个字符为 I 时，是无法在末尾加上与上一个排列末尾相同的数字的。即 res[i-1][j] 在下一个字符为 I 的情况下是不能算到 res[i][j] 中的 。
"""



