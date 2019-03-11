"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


If you have two stacks, one for n "(", the other for n ")",
you generate a binary tree from these two stacks of left/right parentheses to form an output string.

This means that whenever you traverse deeper, you pop one parentheses from one of stacks.
When two stacks are empty, you form an output string.

How to form a legal string? Here is the simple observation:

For the output string to be right, stack of ")" most be larger than stack of "(".
If not, it creates string like "())"
Since elements in each of stack are the same, we can simply express them with a number.
For example, left = 3 is like a stacks ["(", "(", "("]
So, here is my sample code in Python:

"""


class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")


class Solution(object):
    def generateParenthesis(self, n):
        s = ''
        res = []
        self.recur(res, n, n, s)
        return res

    def recur(self, res, left, right, s):
        if [left, right] == [0, 0]:
            res.append(s)
        if left > 0:
            self.recur(res, left - 1, right, s + '(')
        if left < right:
            self.recur(res, left, right - 1, s + ')')

#Solution 2

"""
n - how many parenthesis can still be opened
open - how many parenthesis are opened
"""

class Solution:
    def generateParenthesis(self, n, open=0):
        if n == 0: return [')'*open]
        if open == 0:
            return ['('+x for x in self.generateParenthesis(n-1, 1)]
        else:
            return [')'+x for x in self.generateParenthesis(n, open-1)] + ['('+x for x in self.generateParenthesis(n-1, open+1)]

#Solution 3 -- DP

"""
To generate all n-pair parentheses, we can do the following:

Generate one pair: ()

Generate 0 pair inside, n - 1 afterward: () (...)...

Generate 1 pair inside, n - 2 afterward: (()) (...)...

...

Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping subproblems here. Here is the code:

(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, 
and we are taking into account all possible of combinations of them)

"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
