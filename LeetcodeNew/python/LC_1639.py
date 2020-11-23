"""
https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/928794/python-simple-recursive-with-memo-and-dp-iterative-solution

1621. Number of Sets of K Non-Overlapping Line Segments


word    X X k X  k' X X X
target  Y Y i i' Y  Y Y

dp[i][k] : how many ways to form target[0:i] using word[0:k]
dp[i][k] : how many ways to form valid target[0:i] and target[i] must use work[k]

1. we do not word[k] to form target[i]
dp[i][k] = dp[i][k-1]

2. we use word[k] to form target[i]
if (can do that)
    dp[i][k] += dp[i-1][k-1] * count(how many word[k] == target[i])

n = len(target)
m = len(word)
return dp[n][m]


dp(i,j) means number of words[..i],target[..j] match.
dp(i,j)=dp(i-1,j)+dp(i-1,j-1)*counter_i[target[j]], simple Knapsack logic.
use one dimensional: dp(j)+=dp(j-1)*counter_i[target[j]], iterate from len(target) to 0.
corner case:
for i=0, only dp[0][0] should be calculated, move forward one bit,dp[1][1]+=dp[0][0]*cnt[...]
just set dp[0][0]=1,dp[0][j]=0

"""

import collections
import functools

"""
The state is i,j the index we are currently in for words and target. We can just have one index i for all words in words array because of constraint. Using one index in words nullifies all previous indices. Only look forwards. At each state, two choices, use the index if possible, and don't use the index.

Top Down DP w/ memoization doesn't work by itself. Too slow to iterate through all words and check if index of each word matches index at target. So instead, keep array of dictionaries indexLetters[i][elem] which tells you the count of letters at index i in words. i.e. words = ["acca","bbbb","caca"] -> [i=0:{a:2,c:2},i=1:{b:4},i=2:{a:2,c:2}].

O(n^2),O(n^2) time and space.

Memoization with the help of lru_cache.
Positions store number of occurences of a character c at position k in all of the words of the list.

"""
class Solution:
    def numWays(self, words, target: str) -> int:
        mod = 10 ** 9 + 7
        n = len(words[0])
        m = len(target)
        table = collections.defaultdict(collections.Counter)
        # table2 = [Counter([words[i][j] for i in range(len(words))]) for j in range(m)]
        for i in range(len(words)):
            for j in range(n):
                table[j][words[i][j]] += 1

        @functools.lru_cache(None)
        def dfs(i, j):
            if i == m:
                return 1
            if j == n:
                return 0
            res = 0
            res += dfs(i, j + 1) % mod
            if table[j][target[i]]:
                res += table[j][target[i]] * dfs(i + 1, j + 1) % mod
            return res

        return dfs(0, 0) % mod



class Solution11:
    def numWays(self, words, target: str) -> int:
        n = len(words[0])
        m = len(target)
        mod = 10 ** 9 + 7
        table = [collections.Counter(word[i] for word in words) for i in range(n)]

        # print(table)
        @functools.lru_cache(None)
        def dfs(i, j):
            if j == 0:
                res = 0
                for k in range(i + 1):
                    res += table[k][target[j]]
                return res
            elif i == 0:
                return 0
            return dfs(i - 1, j) + dfs(i - 1, j - 1) * table[i][target[j]]

        return dfs(n - 1, m - 1) % mod




















