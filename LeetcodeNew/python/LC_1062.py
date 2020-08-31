"""
Identitcal to 1044

1062.Longest-Repeating-Substring
解法1： DP
此题和1044.Longest-Duplicate-Substring一模一样，唯一的区别是数据范围更小一些，因此可以用o(N^2)的DP算法。

我们将S分别看做S1和S2，那么此题就变成求两个字符串的longest common substring. 我们令dp[i][j]表示以S1[i]结尾、S2[j]结尾的最长的字符串的长度。则有状态转移方程：

if (S[i]==S[j]) dp[i][j] = dp[i-1][j-1] + 1;
特别注意，还要加上限制条件if (i!=j)

解法2： Rolling Hash
High Level是二分搜值，猜测这个longest repeating substring的长度是多少。如果我们找不到任何长度为len的substring在S中出现过多次，那么就往下猜len；否则就往上猜len。

对于上述的子问题，我们会考虑一个固定长度len的滑窗，掠过整个S。在每个位置上的滑窗，我们都将里面的字符串映射成一个26进制的数，当做hash key放入集合中。
如果发现这个key已经在集合中出现过，就意味着存在两个完全相同的子串。注意这个hash key会很大，所以需要取一个大数的模。当然，这肯定会有collision的风险。


s1 : XX[XXa] i
s2 : [YYb] j

the longest common substring

dp[i][j] : the longest common substring for s1[:i] and s2[:j]
if s1[i] == s2[j]:
    dp[i][j] = dp[i-1][j-1] + 1

"""


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        dp[0][0] = 1
        res = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and S[i - 1] == S[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])

        return res



class Solution2:
    def search(self, S, mid):
        n = len(S)
        base = 26
        MOD = 2 ** 32

        # compute the hash of string S[:mid]
        hash_ = 0
        for i in range(mid):
            hash_ = (hash_ * base + self.nums[i]) % MOD

        # already visited hashes of strings of length mid
        visited = {hash_}
        # const value to be used often : a**mid % mod
        for start in range(1, n - mid + 1):
            # compute rolling hash in O(1) time
            hash_ = (hash_ * base - self.nums[start - 1] * pow(base, mid, MOD) + self.nums[start + mid - 1]) % MOD
            if hash_ in visited:
                return start
            visited.add(hash_)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        self.nums = [ord(S[i]) - ord('a') for i in range(n)]

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if self.search(S, mid) != -1:
                left = mid + 1
            else:
                right = mid - 1

        start = self.search(S, left - 1)
        return len(S[start: start + left - 1])




