
"""
https://leetcode-cn.com/problems/remove-invalid-parentheses/solution/shan-chu-wu-xiao-de-gua-hao-by-leetcode-9w8au/

"""

import collections


class SolutionRikaDFS:
    def removeInvalidParentheses(self, s: str):
        res = []
        # to remove
        left, right = 0, 0
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        self.dfs(s, 0, left, right, res)
        return res

    def dfs(self, s, i, left, right, res):
        n = len(s)
        if left == 0 and right == 0:
            if self.isValid(s):
                res.append(s)
            return

        if left <= 0 and right <= 0:
            return

        for j in range(i, n):
            if j > i and s[j] == s[j - 1]:
                continue
            # 如果剩余的字符无法满足去掉的数量要求，直接返回
            if left + right > n - j:
                break
            # 尝试去掉一个左括号
            if left > 0 and s[j] == '(':
                self.dfs(s[:j] + s[j + 1:], j, left - 1, right, res)
            # 尝试去掉一个右括号
            if right > 0 and s[j] == ')':
                self.dfs(s[:j] + s[j + 1:], j, left, right - 1, res)
            # 统计当前字符串中已有的括号数量

    def isValid(self, s):
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0


class SolutionBFS:
    def removeInvalidParentheses(self, s: str):
        if not s:
            return ['']

        queue = collections.deque([s])
        visited = {s}
        res = []
        found = False
        while queue:
            node = queue.popleft()
            if self.isValid(node):
                found = True
                res.append(node)
            elif not found:
                for i in range(len(node)):
                    if node[i] == '(' or node[i] == ')':
                        newNode = node[:i] + node[i + 1:]
                        if newNode not in visited:
                            queue.append(newNode)
                            visited.add(newNode)
        return res

    def isValid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count == 0:
                    return False
                count -= 1

        return count == 0


class SolutionEasy:
    def removeInvalidParentheses(self, s: str):
        level = [s]
        while level:
            valid = [sub_str for sub_str in level if self.is_valid(sub_str)]
            if valid:
                return valid

            new_level = set()
            for sub_str in level:
                for i in range(len(sub_str)):
                    if sub_str[i] not in ('(', ')'):
                        continue
                    new_level.add(sub_str[:i] + sub_str[i + 1:])

            level = new_level
        return ['']

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0



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





class Solution:
    def removeInvalidParentheses(self, s: str):
        level = [s]
        stack = self.search(s)
        step = 0
        while level:
            valid = [sub_str for sub_str in level if self.is_valid(sub_str)]
            if valid:
                return valid
            curr_delete = stack[step]
            step += 1
            new_level = set()
            for sub_str in level:
                for i in range(len(sub_str)):
                    if sub_str[i] != curr_delete:
                        continue
                    new_level.add(sub_str[:i] + sub_str[i + 1:])

            level = new_level
        return ['']

    def is_valid(self, s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def search(self, s):
        stack = []
        for char in s:
            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
            elif char in ('(', ')'):
                stack.append(char)
        return stack


s = "(a)())()"
a = SolutionBFS()
print(a.removeInvalidParentheses(s))






