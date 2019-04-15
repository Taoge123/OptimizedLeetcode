
"""
dp[i][j] = dp[i - 1][j] +( dp[i - 1][j - 1] if s[i - 1] == s[j - 1])

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
"""
"""
Step 2: initialize other values in row 0

for j in range(1, l2):
        dp[0][j] = 0

If there are more chars in t and s is an empty string then except matrix[0][0]
 being 1 the rest all will be zero right? for example there are no distinct common subsequence 
 for s="" to t="ui"; thats the main idea behind the dp[0][j] ( pay attention to the loop starting 
 from 1 index -> which signifies if any charecter in t)

Step3: Meat part

for i in range(1, l1):
        for j in range(1, l2):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
            

Now iterate from matrix[1][1], you have to check if there is a match from t charecter and s charecter
if there is a match: record the number of ways to the prev charecter dp[i-1][j-1] 
(which is obvious, its like a jump game, if you can step here, 
how many ways can you come to the prev step) + dp[i-1][j] (how many ways have you been here before ?)

and in the end you will have the output at dp[-1][-1]

"""
import collections

class SolutionCaikehe:
    # O(m*n) space
    def numDistinct1(self, s, t):
        l1, l2 = len(s) + 1, len(t) + 1
        dp = [[1] * l2 for _ in range(l1)]
        for j in range(1, l2):
            dp[0][j] = 0
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])
        return dp[-1][-1]

    # O(n) space
    def numDistinct(self, s, t):
        l1, l2 = len(s) + 1, len(t) + 1
        cur = [0] * l2
        cur[0] = 1
        for i in range(1, l1):
            pre = cur[:]
            for j in range(1, l2):
                cur[j] = pre[j] + pre[j - 1] * (s[i - 1] == t[j - 1])
        return cur[-1]


"""
- We create set of t for O(1) check of characters in s, whether they are in t or not
- We create index dictionary for every index of every character in t
- We create dp list, where every previous character, dp[i - 1], will accumulate into dp[i]
- In other words, different number of ways to constitute word[:i-1] will be added on word[:i] or dp[i] in our case
- Critical point is we accumulate in reverse order for i in indexes of the character, 
- because we should accumulate previous ways before seeing this new character, 
  or before updating previous indexes on this round
"""
class Solution1:
    def numDistinct(self, s, t):
        chars = set(t)
        index = collections.defaultdict(list)
        dp = [0] * len(t)
        for i, c in enumerate(t): index[c].append(i)
        for c in s:
            if c in chars:
                for i in index[c][::-1]: dp[i] += dp[i - 1] if i > 0 else 1
        return dp[-1]


class Solution2:
    def numDistinct1(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1 ,m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]

    def numDistinct(self, s: str, t: str) -> int:
        # O(mn) space

        # O(n) space
        m, n = len(s), len(t)
        dp = [1] + [0] * n
        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]


"""
When I read the question again, I found the phrase cited may be wrong. 
The question asks us to find distinct subsequence of S == T. 
If we count the number of distinct subsequences of T in S and S = "rabbbit" and T = "rabbit", 
then "r" is a subsequence of T and will be counted too. That is obviously not what we want.

Then, we can write the relation which is very similar to LCS. 
I just remove one state transition from LCS and sum them up.
Because T could not be subsequence so dp[i][j] can only come from dp[i - 1][j - 1] and dp[i - 1][j - 1]. 
dp[i][j - 1] cannot be counted because it will lead to miss some letters in T (becoming subsequence).

Recurrence relation:

dp[i][j] = dp[i - 1][j] +( dp[i - 1][j - 1] if s[i - 1] == s[j - 1])

"""
class Solution3:
    def numDistinct(self, s, t):

        dp = [[0 for j in range(0, len(t) + 1)] for i in range(0, len(s) + 1)]
        for j in range(1, len(t) + 1):
            dp[0][j] = 0
        for i in range(1, len(s) + 1):
            dp[i][0] = 1

        dp[0][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] * (s[i - 1] == t[j - 1])

        return dp[-1][-1]

"""
Space optimization:
The states are only from top and left-top. Thus, 1-D array is enough and uses some temp variables to roll the array all the way down.
"""
"""
解题思路：这道题使用动态规划来解决。题的意思是：S的所有子串中，有多少子串是T。下面来看看状态转移方程。dp[i][j]表示S[0...i-1]中有多少子串是T[0...j-1]。

　　　　　当S[i-1]=T[j-1]时：dp[i][j]=dp[i-1][j-1]+dp[i-1][j]；S[0...i-1]中有多少子串是T[0...j-1]包含：
        {S[0...i-2]中有多少子串是T[0...j-2]}+{S[0...i-2]中有多少子串是T[0...j-1]}

　　　　   当S[i-1]!=T[j-1]时：dp[i][j]=dp[i-1][j-1]

　　　　   那么初始化状态如何确定呢：dp[i][0]=1；S[0...i-1]只有一个子串是空串。

"""
class Solution33:
    def numDistinct(self, s, t):

        dp = [0 for _ in range(0, len(t) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            pre = dp[0]
            for j in range(1, len(t) + 1):
                tmp = dp[j]
                dp[j] = dp[j] + pre * (s[i - 1] == t[j - 1])
                pre = tmp
        return dp[-1]


"""
解题方法
动态规划
这个题一看就是DP。向字符串序列问题确实有很多都是用DP求解的。

设dp数组dp[i][j]表示S的前j个字符是T的前i个字符的子序列的个数为dp[i][j]。

那么有dp[0][*] == 1，因为这个情况下，只能使用s的空字符串进行匹配t。

如果s[j - 1] == t[i - 1]，那么，dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]，
原因是t的前j个字符可以由s的前[i - 1]个字符和t的前[j - 1]个匹配的同时最后一个字符匹配，
加上s的前[j - 1]个字符和t的前[i]个字符匹配同时丢弃s的第[j]个字符。

如果s[j - 1] != t[i - 1]，那么dp[i][j] = dp[i][j - 1]，因为只能是前面的匹配，
最后一个字符不能匹配，所以丢弃了。
"""
"""
算法2：动态规划，
设dp[i][j]是从字符串S[0...i]中删除几个字符得到字符串T[0...j]的不同的删除方法种类，
有上面递归的分析可知，动态规划方程如下

如果S[i] = T[j], dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
如果S[i] 不等于 T[j], dp[i][j] = dp[i-1][j]
初始条件：当T为空字符串时，从任意的S删除几个字符得到T的方法为1
"""



