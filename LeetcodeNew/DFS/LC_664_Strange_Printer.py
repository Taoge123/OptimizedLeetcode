"""

The problem wants us to find the number of ways to do something without giving specific steps like how to achieve it.
This can be a typical signal that dynamic programming may come to help.

dp[i][j] stands for the minimal turns we need for string from index i to index j.
So we have

dp[i][i] = 1: we need 1 turn to paint a single character.
dp[i][i + 1]
dp[i][i + 1] = 1 if s.chartAt(i) == s.charAt(i + 1)
dp[i][i + 1] = 2 if s.chartAt(i) != s.charAt(i + 1)
Then we can iteration len from 2 to possibly n.
For each iteration, we iteration start index from 0 to the farthest possible.

The maximum turns for dp[start][start + len] is len + 1, i.e. print one character each time.
We can further divide the substring to two parts: start -> start+k and start+k+1 -> start+len.
It is something as following:

index |start  ...  start + k| |start + k + 1 ... start + len|
char  |  a    ...       b   | |      c       ...      b     |

As shown above, if we have s.charAt(start + k) == s.charAt(start + len),
we can make it in one turn when we print this character (i.e. b here)
This case we can reduce our turns to dp[start][start + k] + dp[start + k + 1][start + len] - 1

https://leetcode.com/problems/strange-printer/discuss/168121/546.-Remove-Boxes-and-664.-Strange-Printer%3A-See-the-similarity



"""


"""
OMG
Remove Boxes and 664. Strange Printer are very similar :
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
                result = min(result, dp(l, k) + dp(k + 1, r - 1)
"""

class Solution:
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
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


class Solution2:

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



