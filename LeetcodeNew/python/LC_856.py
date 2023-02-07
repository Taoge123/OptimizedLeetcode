"""
https://leetcode.com/problems/score-of-parentheses/solutions/141828/python-javascript-simple-and-readable-stack-solution/

"""

import functools


class SolutionTony:
    def scoreOfParentheses(self, s: str) -> int:

        stack = [0]
        for ch in s:
            # new valid paranthesis cluster
            if ch == "(":
                stack.append(0)
            else:
                last = stack.pop()
                # stack[-1] += 2 * last or 1
                if last == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * last
        return stack.pop()



class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        stack = []
        cur = 0
        for char in S:
            if char == ')':
                if cur != 0:
                    cur *= 2
                else:
                    cur = 1
                cur += stack.pop()
            else:
                stack.append(cur)
                cur = 0
        return cur



class SolutionMemo:
    def scoreOfParentheses(self, s: str) -> int:
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == j - 1:
                return 1

            balance = 0
            for k in range(i, j):
                if s[k] == '(':
                    balance += 1
                if s[k] == ')':
                    balance -= 1
                if balance == 0:
                    return dfs(i, k) + dfs(k + 1, j)

            return 2 * dfs(i + 1, j - 1)

        return dfs(0, len(s) - 1)
