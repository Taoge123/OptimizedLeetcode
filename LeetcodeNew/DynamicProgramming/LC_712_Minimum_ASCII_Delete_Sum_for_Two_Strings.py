
"""
Similar to 72 Edit Distance

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""

"""
This reduces the problem to greatest common subsequence. 
"""
class Solution1:
    def minimumDeleteSum(self, s1, s2):

        l1, l2 = len(s1), len(s2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        result = sum(map(ord, s1 + s2)) - dp[l1][l2] * 2
        return result


"""
to get the minimal cost, we need to find the common subsequences, 
and among all the common subsequences, we need to find the minimal cost.

it is very like to find the longest common subsequence, but this time, 
we need to find the max ascii common subsequence, 
then the minimal cost is the two fixed ascii sum of two origin strings, 
minus the max ascii common subsequence we have found.
"""

class Solution2:
    def minimumDeleteSum(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        for i in range(l1):
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s1[i]) * 2
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        n1 = sum(ord(c) for c in s1)
        n2 = sum(ord(c) for c in s2)
        return n1 + n2 - dp[l1][l2]


class Solution3:
    def minimumDeleteSum(self, s1, s2):

        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i + j == 0:  continue
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j - 1] + ord(s2[j - 1])
                elif i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + ord(s1[i - 1])
                elif s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

        return dp[m][n]


"""
Same as implementing edit distance solution. Only difference is cost is ASCII value instead of 1.
"""
class SolutionBest:
    def minimumDeleteSum(self, s1, s2):
        l1, l2 = len(s1) + 1, len(s2) + 1
        d = [[0] * l2 for i in range(l1)]
        for i in range(l1):
            for j in range(l2):
                c1, c2 = ord(s1[i - 1]), ord(s2[j - 1])
                if not i * j:
                    d[i][j] = d[i - 1][j] + c1 if i else d[i][j - 1] + c2 if j else 0
                elif s1[i - 1] == s2[j - 1]:
                    d[i][j] = d[i - 1][j - 1]
                else:
                    d[i][j] = min(d[i - 1][j] + c1, d[i][j - 1] + c2, d[i - 1][j - 1] + c1 + c2)
        return d[-1][-1]

