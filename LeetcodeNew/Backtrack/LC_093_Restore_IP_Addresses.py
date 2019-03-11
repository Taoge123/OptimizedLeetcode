"""
Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

class Solution:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)


class SolutioinCaikehe2:
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return  # backtracking
        for i in range(1, 4):
            if i <= len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                if s[0] == "0":  # here should be careful
                    break

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def bt(start, current):
            if len(current) == 4:
                if start == len(s):
                    result.append('.'.join(current))
                return
            for i in xrange(start + 1, min(start + 4, len(s) + 1)):
                if i - 1 > start and s[start] == '0':
                    continue
                a = s[start:i]
                if 0 <= int(a) <= 255:
                    current.append(a)
                    bt(i, current)
                    current.pop()

        result = []
        bt(0, [])
        return result
