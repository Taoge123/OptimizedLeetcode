
"""
https://www.cnblogs.com/grandyang/p/8684817.html

Given strings S and T, find the minimum (contiguous) substring W of S,
so that T is a subsequence of W.

If there is no such window in S that covers all characters in T,
return the empty string "". If there are multiple such minimum-length windows,
return the one with the left-most starting index.

Example 1:

Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:

All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
"""

"""
Very brief explannation : m = len(T), n = len(S), 
scan string S and maintain a up to date list of start index of matching T in list dp(size of m), 
dp[i] denotes the start index when i+1 chars of T are matched. 
When T[i] appears in S, we simply update dp[i] = dp[i-1], when T[0] appears in S with index, 
we update dp[0] = index. Whenever dp[m-1] is updated, we have a new window that T is sub-sequence of, 
and we keep a running minimum of this window width

We scan S once, and each update depends the number of same char in T. 
The worst case is O(mn) when all position of T are identical. 
When the char in T doesn't have much repetition, O(n) time complexity is achieved.

Space complexity O(m)

The dp list is where you build up possible answers. 
It has the same length as the subsequence you are searching for (T). 
At first it has all -1's. You start scanning the search string S. 
The code you highlighted occurs if you hit a character in S that is also in T. 
The first if says "if you hit the first character in the subsequence T, 
update dp[0] to be its index in S." This is like starting a new potential answer. 
The else says "if I come across another character in T besides the first character, 
then set the spot in dp corresponding to that character to be equal to the entry before it in dp. 
Let's say it's the third character in S and I have previously come across the first two. 
Then the update entry for dp[3] will record the location of the start of a possible solution."...
it's like your percolating up possible answers. 
The last if statement says "if you come across the last character in T, 
it's dp entry is nonzero (meaning we percolated up an answer through the entire dp array 
and therefore have seen every character in order in the subsequence), 
and the length of this new window is less than the best we have found so far, 
then update the length of this window (named count here) and update the start of this window...
aka we found a new window".
^I know that isn't perfectly worded, but I hope this helps others later.
"""


class Solution1:
    def minWindow(self, S, T):

        n = len(S)
        m = len(T)

        dic = dict()
        for i, s in enumerate(T):
            dic.setdefault(s, []).append(i)

        dp = [-1 for i in range(m)]

        count = n + 1
        start = -1

        for index, c in enumerate(S):
            if c in dic:
                for i in dic[c][::-1]:
                    if i == 0:
                        dp[i] = index
                    else:
                        dp[i] = dp[i - 1]
                    if i == m - 1 and dp[i] >= 0 and index - dp[i] + 1 < count:
                        count = index - dp[i] + 1
                        start = dp[i]
        if dp[-1] < 0:
            return ""
        return S[start:start + count]

"""
Different from other DP solution (but share the same idea I guess), my

dp[i][j] = minimum substring length end at S[j] which contains subsequence of T[:i]
"""

class Solution2:
    def minWindow(self, S, T):

        m,n = len(S), len(T)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if S[j-1] == T[i-1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]+1
        res = min(dp[-1])
        if res == float('inf'):return ''
        for i in range(1,m+1):
            if dp[-1][i] == res:
                return S[i-res:i]


class Solution3:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T): return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]

        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res


"""
给定字符串S和T，在S中寻找最小连续子串W，使得T是W的子序列。如果没有找到返回""，
如果找到多个最小长度的子串，返回左 index 最小的。

解法1：暴力搜索brute force，对于每一个s[i]，从s[0]到s[i]扫描，看是否按顺序满足目标字符。 
      显然要超时，不是题目要求的。

解法2： 动态规划DP,  二维数组dp[i][j]表示T[0...i]在S中找到的起始下标index，
使得S[index, j]满足目前T[0...i]。首先找到能满足满足T中第一个字符T[0]的S中的字符下标存入dp[0][j]，
也就是满足第一个字符要求一定是从这些找到的字符开始的。
然后在开始找第二个字符T[1]，扫到的字符dp[j]存有index，说明可以从这里记录的index开始，
找到等于T[1]的S[j]就把之前那个index存进来，说明从这个index到j满足T[0..1]，一直循环，
直到T中的i个字符找完。如果此时dp[i][j]中有index，说明S[index, j]满足条件，如有多个输出最先找到的。

State: dp[i][j]，表示在S中找到的起始下标 index ，使得 S[index...j] 满足目前 T[0...i] 是其子序列。

function: dp[i+1][k] = dp[i][j]  if S[k] = T[i+1] , 如果查看到第i+1行（也就是第 T[i+1]  的字符），
如果满足S[k] = T[i+1]，就把上一行找到的index赋给它。

Initialize: dp[0][j] = j if S[j] = T[0] , 二维数组的第一行，如果字符S[j] = T[0]，
就把S[j]的index(就是j)付给它。其他元素均为 None 或者 -1。

Return:  dp[len(T) - 1][j], if  dp[len(T) - 1][j] != None， 返回最小的。如果没有返回 ""

由于我们只用到前一行的值，所以可以只用2行的二维数组，每一个循环更新其中的一行。
可以用 j % 2 来往复使用。
"""
"""
解题思路：
动态规划（Dynamic Programming）

数组dp[i]存储当T[0 .. i]在S中找到子序列匹配时，对应的最大起点下标

初始令dp[0 .. len(T) - 1] = -1

状态转移方程见代码
"""
class Solution4:
    def minWindow(self, S, T):

        ans = ''
        ls, lt = len(S), len(T)
        dp = [-1] * lt
        for x in range(ls):
            for y in range(lt - 1, -1, -1):
                if T[y] == S[x]:
                    dp[y] = dp[y - 1] if y else x
                    if y == lt - 1 and dp[-1] > -1:
                        nlen = x - dp[-1] + 1
                        if not ans or nlen < len(ans):
                            ans = S[dp[-1] : x+1]
        return ans


"""
思路：

动态规划问题。我们定义dp[i][j]表示S的前缀S[0,i]中的起始索引k，使得T[0,j]是S[k,i]的子串。
这样如果S[i] == T[0]，则dp[i][0] = i，否则dp[i][0] = -1。
而递推公式为：
    如果S[i] == T[j]，那么dp[i][j] = max(dp[k][j-1]), 0 <= k < i。
    否则dp[i][j] = -1。而我们的目标则是找到min(i - dp[i][n-1])，其中n是T的长度。
"""
"""
题解：
找到S中的substring, T中的字符保持它们的order, 也在substring中出现。
对substring的限制条件是：最短的，如果有几个长度相同的，取第一个。
用dynamic programing来做，dp[i][j]表示T[0, j]是S[0,i]的subsequence, 
所以我们的目标函数就是min(i-dp[i][n-1]) for all i < m

"""



