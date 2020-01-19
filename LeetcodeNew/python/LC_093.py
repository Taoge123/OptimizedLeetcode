"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

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
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)



class Solution2:
    def restoreIpAddresses(self, s: str):

        res = []
        self.helper(res, s, 0, "", 0)
        return res

    def helper(self, res, s, index, path, count):
        if count > 4:
            return

        if count == 4 and index == len(s):
            res.append(path)
            return

        for i in range(1, 4):
            if index + i > len(s):
                break
            temp = s[index:index + i]

            if temp.startswith("0") and len(temp) > 1 or (i == 3 and int(temp) >= 256):
                continue
            if count == 3:
                self.helper(res, s, index + i, path + temp + "", count + 1)
            else:
                self.helper(res, s, index + i, path + temp + ".", count + 1)




s = "25525511135"
a = Solution()
print(a.restoreIpAddresses(s))



