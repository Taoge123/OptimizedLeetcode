
"""
Remove Boxes and 664. Strange Printer are very similar :
https://leetcode.com/problems/strange-printer/discuss/106803/Python-iterative-DP-O(n3)-Solution.-BUT-GOT-AN-TLE


omg!!!!!!
https://leetcode.com/problems/strange-printer/discuss/168121/546.-Remove-Boxes-and-664.-Strange-Printer%3A-See-the-similarity

There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places,
and will cover the original existing characters.
Given a string consists of lower English letters only,
your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string,
which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""
"""
We want to maximize the number and length of continuous subsequences of the same value. 
If dp(l, r) represents the optimal value for array[ l : r+1 ], 
If there is a point array[m] in 1< m < r that is the same as array[r], it will improve the result. 
Then we recur on array[l : m + 1] and array[ m + 1 : r - 1].
The following recursions for the two problems are almost the same. 
Once you realize that a problem is actually asking you to optimize the number 
and length of continuous subsequence, you can just use the formula.

546
    for k in range(l+1, r-1):
        if boxes[k] == boxes[r]:
            res = max(res, dfs(l, k, k+1) + dfs(k+1, r-1, 0))
664
      for k in range(l, r):
            if s[k] == s[r]:
                result = min(result, dp(l, k) + dp(k + 1, r - 1))



"""
class SolutionCompare1:
    def strangePrinter(self, s):

        memo = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) not in memo:
                result = dp(i, j - 1) + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        result = min(result, dp(i, k) + dp(k + 1, j - 1))
                memo[(i, j)] = result
            return memo[(i, j)]
        return dp(0, len(s) - 1)


class SolutionCompare2:
    def removeBoxes(self, boxes):
        def dfs(l, r, k):
            if l > r:
                return 0
            if (l, r, k) not in memo:
                while r > l and boxes[r] == boxes[r-1]:
                    k += 1
                    r -= 1
                while l < r and boxes[l] == boxes[r]:
                    k += 1
                    l += 1
                res = (k+1)**2 + dfs(l, r-1, 0)
                for i in range(l+1, r-1):
                    if boxes[i] == boxes[r]:
                        res = max(res, dfs(l, i, k+1) + dfs(i+1, r-1, 0))
                memo[l, r, k] = res
            return memo[l, r, k]
        memo = {}
        return dfs(0, len(boxes) - 1, 0)


"""
Approach #1: Dynamic Programming [Accepted]
Intuition

It is natural to consider letting dp(i, j) be the answer for printing S[i], S[i+1], ..., S[j], 
but proceeding from here is difficult. We need the following sequence of deductions:

Whatever turn creates the final print of S[i] might as well be the first turn, 
and also there might as well only be one print, 
since any later prints on interval [i, k] could just be on [i+1, k].

Say the first print is on [i, k]. We can assume S[i] == S[k], 
because if it wasn't, we could print up to the last occurrence of S[i] in [i, k] for the same result.

When correctly printing everything in [i, k] (with S[i] == S[k]), 
it will take the same amount of steps as correctly printing everything in [i, k-1]. 
This is because if S[i] and S[k] get completed in separate steps, 
we might as well print them first in one step instead.

Algorithm

With the above deductions, the algorithm is straightforward.

To compute a recursion for dp(i, j), for every i <= k <= j with S[i] == S[k], 
we have some candidate answer dp(i, k-1) + dp(k+1, j), and we take the minimum of these candidates. 
Of course, when k = i, the candidate is just 1 + dp(i+1, j).

To avoid repeating work, we memoize our intermediate answers dp(i, j).
"""
class Solution0:
    def strangePrinter(self, S):
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if S[k] == S[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(S) - 1)


"""
I suggest to do this treatment, before go directly DP.

Shorten the original string, like reduce aaabbb to ab.

The same consecutive characters won't change the result and this really help improve the efficiency.

Besides, in python, it takes only 1 line to do it:

s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
or use regex

s = re.sub(r'(.)\1*', r'\1', s)
"""

"""
Lets insert one character at a time. The cost to insert is 1 
if we can not reuse anything from previous step or 0 
if some prevous step can provide us with this character for free.
"""
class Solution1:
    def strangePrinter(self, s):
        cache = dict()

        def solve(s):
            if not s:
                return 0
            if s in cache:
                return cache[s]
            # cost to simply insert last character
            cost = solve(s[0:-1]) + 1
            # what if last character could be inserted for free just by reusing previous step that already prints it?
            char_to_insert = s[-1]
            for i, c in enumerate(s[:-1]):
                if c == char_to_insert:
                    cost = min(cost, solve(s[0:i + 1]) + solve(s[i + 1:-1]))
            cache[s] = cost
            return cost

        return solve(s)


"""
Let dp(i, j) be the number of turns needed to print S[i:j+1].

Note that whichever turn creates the final print of S[i], 
might as well be the first turn, and also there might as well only be one print, 
since any later prints on interval [i, k] could just be on [i+1, k].

So suppose our first print was on [i, k]. We only need to consider prints where S[i] == S[k], 
because we could instead take our first turn by printing up to the last printed index 
where S[k] == S[i] to get the same result.

Then, when trying to complete the printing of interval [i, k] (with S[i] == S[k]), 
the job will take the same number of turns as painting [i, k-1]. 
This is because it is always at least as good to print [i, k] first 
in one turn rather than separately.

Also, we would need to complete [k+1, j]. So in total, 
our candidate answer is dp(i, k-1) + dp(k+1, j). Of course, when k == i, 
our candidate is 1 + dp(i+1, j): we paint S[i] in one turn, 
then paint the rest in dp(i+1, j) turns.
"""

class Solution3:
    def strangePrinter(self, s):
        n = len(s)
        dp = [[0] * n for i in range(n + 1)]
        for i in range(n):
            dp[i][i] = 1
        for step in range(1, n):
            for i in range(n-step):
                k = i+step
                dp[i][k] = dp[i+1][k] + 1
                for j in range(i+1, k+1):
                    if s[i] == s[j]:
                        dp[i][k] = min(dp[i][k], dp[i][j-1] + dp[j+1][k])
        return dp[0][-1] if s else 0



class Solution4:
    def strangePrinter(self, s):

        self.string = s
        n = len(self.string)
        self.dp = [[-1] * n for _ in range(n)]
        return self.helper(0, n - 1)

    def helper(self, s, e):
        if s > e:
            return 0
        if self.dp[s][e] >= 0:
            return self.dp[s][e]
        self.dp[s][e] = self.helper(s, e - 1) + 1
        for i in range(s, e):
            if self.string[i] == self.string[e]:
                self.dp[s][e] = min(self.dp[s][e], self.helper(s, i) + self.helper(i + 1, e - 1))
        return self.dp[s][e]


"""
题目大意：
打印机支持两种操作：

一次打印某字符重复若干次
从字符串的任意位置开始打印字符，覆盖原始字符
求得到目标串所需的最少打印次数

解题思路：
动态规划（Dynamic Programming）

dp[i][j]表示打印下标[i .. j]的子串所需的最少打印次数；记目标串为s

状态转移方程为：

dp[y][x] = min(dp[y][x], dp[y][z-1] + dp[z][x-1] + k)   
当s[x-1] != s[z-1]时k取值1，否则k取值0
"""
"""
dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j]       
(s[k] == s[i] and i + 1 <= k <= j)
"""
"""
分析
二维DP问题 
1、dp[i][j] 表示范围 [i, j) 内的最小轮次. 运用memoization 和 DFS来避免计算不必要的子问题. 
2、贪婪的选择: 对于任意一个序列, 首先打印首字符. 比如 s[0] = ‘a’. 如果存在最优的解决方案, 
不是将s[0] 打印的范围是 [0, k)作为第一步, 我们可以将这一个移到第一步，并且保证其他步为原来的顺序. 
如果有字符在s[0]的原来的顺序之前打印了，且范围在k之前，我们将该字符的打印开始位置移动到k开始.

根据不同的方法将 s[0]= ‘a’ 和其他部分的 ‘a’结合起来，我们有：

dp[i][j] = min(dp[i][j], dp[start][k]+dp[k][end]), 对于每个 k 有 s[k] == s[i]，
1
这里的start和end分别是开始的一个字符和最后的一个字符，不是s[i].
例如
给定一个序列 "aaa bcd aaa def aaa ccd aaa", 我们有三种选择来结合 s[0] = 'a' 和其他部分的 'a'.
bcd + aaa aaa def aaa ccd aaa,与之一样的是 bcd + aaa def aaa ccd
bcd aaa def + aaa ccd
bcd aaa def aaa ccd + aaa
"""


