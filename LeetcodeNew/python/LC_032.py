
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        res = 0
        start = -1

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            else:
                # (((((
                if not stack:
                    start = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - start)
                    else:
                        res = max(res, i - stack[-1])

        return res


"""
" ( ) (  ( ) )"
  0 1 2  3 4 5
    2      2 2+2+2

" )  (    )   (  (  )   ) "
  0  1  2  3  4  5  6
[ 0, 0, 2, 0, 0, 2, 4]
i = 6 
Dp[5]
6 - 2 - 1
Max_to_now = 2


===
0  1 2  3  4  5  6 7
 (   (   )   (    (   )    )   )

0   0  2   0   0  2   6  
"""
class Solution2:
    def longestValidParentheses(self, s):
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]

                max_to_now = max(max_to_now, dp[i])
        return max_to_now


s1 = "()()"
s2 = "((()))"

a = Solution()
print(a.longestValidParentheses(s1))




