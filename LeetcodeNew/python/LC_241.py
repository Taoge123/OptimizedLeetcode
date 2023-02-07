"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

"""

import functools

class SolutionTony:
    def diffWaysToCompute(self, s: str):
        def compute(x, y, op):
            if op == '+':
                return x + y
            if op == '-':
                return x - y
            if op == '*':
                return x * y

        @functools.lru_cache(None)
        def dfs(i, j):
            if s[i:j].isdigit():
                return [int(s[i:j])]

            res = []
            for k in range(i, j):
                if s[k] == '+' or s[k] == '-' or s[k] == '*':
                    op = s[k]
                    left = dfs(i, k)
                    right = dfs(k + 1, j)
                    for x in left:
                        for y in right:
                            res.append(compute(x, y, op))
            return res

        return dfs(0, len(s))


class SolutionTony2:
    def diffWaysToCompute(self, expression: str):
        def compute(x, y, operator):
            if operator == '+':
                return x + y
            if operator == '-':
                return x - y
            if operator == '*':
                return x * y

        @functools.lru_cache(None)
        def dfs(s):
            if s.isdigit():
                return [int(s)]

            res = []
            for i in range(len(s)):
                if s[i] == '+' or s[i] == '-' or s[i] == '*':
                    operator = s[i]
                    left = dfs(s[:i])
                    right = dfs(s[i + 1:])
                    for x in left:
                        for y in right:
                            res.append(compute(x, y, operator))
            return res

        return dfs(expression)

input = "2-1-1"
a = Solution()
print(a.diffWaysToCompute(input))



