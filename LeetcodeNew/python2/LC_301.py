
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


s = "(a)())()"
a = Solution()
print(a.removeInvalidParentheses(s))






