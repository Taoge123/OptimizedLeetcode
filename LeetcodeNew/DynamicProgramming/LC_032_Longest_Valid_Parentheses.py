
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

"""
let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, 
then we have the following relationship:
dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.
"""

class Solution1:
    def longestValidParentheses(self, s):
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + i - p + 1
        return max(dp)


class Solution2:
    def longestValidParentheses(self, s):
        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in xrange(len(s))]
        max_to_now = 0
        for i in xrange(1,len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i-1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i-2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0: # content within current matching pair is valid
                    # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                    # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now


class Solution3:
    def longestValidParentheses(self, s):
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest

# https://blog.csdn.net/Koala_Tree/article/details/81385559

class Solution4:
    def longestValidParentheses(self, s):

        from collections import defaultdict

        dp = defaultdict(lambda: 0)
        res = 0
        for i, elem in enumerate(s):
            if elem == ')':
                idx = i - dp[i - 1] - 1
                if idx >= 0 and s[idx] == '(':
                    dp[i] = dp[i - 1] + 2
                    dp[i] += dp[i - dp[i]]
                    res = max(res, dp[i])

        return res



