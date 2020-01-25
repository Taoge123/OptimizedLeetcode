
"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

import collections


class SolutionCspiration:
    def removeInvalidParentheses(self, s: str):
        res = []
        self.helper(res, s, 0, 0, ['(', ')'])
        return res

    def helper(self, res, s, last_i, last_j, pair):
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == pair[0]:
                count += 1
            if s[i] == pair[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == pair[1] and (j == last_j or s[j - 1] != pair[1]):
                    self.helper(res, s[0:j] + s[j + 1:], i, j, pair)

            return

        reverse = s[::-1]

        if pair[0] == '(':
            self.helper(res, reverse, 0, 0, [')', '('])
        else:
            res.append(reverse)





class Solution0:
    def removeInvalidParentheses(self, s):
        removed = 0
        results = {s}
        count = {"(": 0, ")": 0}
        for i, c in enumerate(s):
            if c == ")" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(i - removed + 1):
                        if result[j] == ")":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                removed += 1
            else:
                if c in count:
                    count[c] += 1
        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed
        for ii in range(ll - 1, -1, -1):
            i -= 1
            c = s[i]
            if c == "(" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(ii, ll):
                        if result[j] == "(":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
        return list(results)


class Solution:
    def removeInvalidParentheses(self, s):

        visited = set([s])
        return self.dfs(s, visited)

    def dfs(self, s, visited):
        miss = self.calc(s)
        if miss == 0:
            return [s]
        res = []
        for i in range(len(s)):
            if s[i] in ('(', ')'):
                new = s[:i] + s[i + 1:]
                if new not in visited and self.calc(new) < miss:
                    visited.add(new)
                    res.extend(self.dfs(new, visited))
        return res

    def calc(self, s):
        a = b = 0
        for c in s:
            a += {'(': 1, ')': -1}.get(c, 0)
            b += (a < 0)
            a = max(a, 0)
        return a + b


class SolutionBFS:
    def removeInvalidParentheses(self, s):

        if not s:
            return ['']
        queue = collections.deque([s])
        res, visited = [], set([s])
        found = False
        while queue:
            cur = queue.popleft()
            if self.isValidParentheses(cur):
                found = True
                res.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        new = cur[:i] + cur[i + 1:]
                        if new not in visited:
                            queue.append(new)
                            visited.add(new)
        return res

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0



s = "(a)())()"
a = SolutionBFS()
print(a.removeInvalidParentheses(s))






