"""

Given an input string (s) and a pattern (p),
implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false


I probably could have combined some clauses, but it works.
The idea is that we need to go through all of the characters in the string,
and the pattern and end up with true path at the end for it to return true.
This means the current cell is true in the following cases:

the current cell's letters i-1th letter from the string and j-1th letter from the string match
and the dp[i-1][j-1] is true which means the previous two letter's compared was true.
if the current i-1th letter is * then we let all of the cases pass and the future cases pass
so if dp[i-1][j] or dp[i][j-1] is true we mark dp[i][j] as true,
this means all values ahead of this column will be marked as true
if the current i-1th letter is ? then we just copy dp[i-1][j-1] (if the last letter matched was true)
The branches are just to make sure we don't have an out of range error
since there's a variety cases of i-1 and j-1s that can be less than 0
or that cases that we don't have enough characters to get the i-1th or j-1th character,
and probably can be cleaned up.

Visual Example:
s="adceb"
p="*a*b"

     0       a       d    c         e     b
0  [true,  false,  false, false,  false, false]
*  [true,  true,   true,  true,   true,  true ]
a  [false, true,   false, false,  false, false]
*  [false, true,   true,  true,   true,  true ]
b  [false,  false, false, false,  false, true ]

"""


class Solution(object):
    def isMatch(self, s, p):
        N1 = len(p)
        N2 = len(s)
        dp = [[False for j in range(N2+1)] for i in range(N1+1)]
        for i in range(N1+1):
            for j in range(N2+1):
                if(i==0 and j==0):
                    dp[i][j]=True
                elif(j==0):
                    dp[i][j]= (N1>0 and i>0 and p[i-1]=='*' and (dp[i-1][j]));
                elif(i==0):
                    dp[i][j]= (N1>0 and i>0 and p[i-1]=='*' and (dp[i][j-1]));
                else:
                    dp[i][j]=((dp[i-1][j-1] and (N1>0 and N2>0 and p[i-1]==s[j-1]))or
                              (N1>0 and p[i-1]=='*' and (dp[i-1][j] or dp[i][j-1])) or
                              (N1>0 and p[i-1]=='?' and dp[i-1][j-1]))
        return dp[N1][N2]


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls = len(s)
        lp = len(p)
        dp = [[False] * (lp + 1) for i in range(ls + 1)]

        dp[0][0] = True

        for i in range(1, lp + 1):
            if p[i - 1] == '*' and dp[0][i - 1]:
                dp[0][i] = True

        for row in range(1, ls + 1):
            for col in range(1, lp + 1):
                if s[row - 1] == p[col - 1] or p[col - 1] == '?':
                    dp[row][col] = True and dp[row - 1][col - 1]
                elif p[col - 1] == '*':
                    dp[row][col] = dp[row][col - 1] or dp[row - 1][col - 1] or dp[row - 1][col]
        return dp[ls][lp]


