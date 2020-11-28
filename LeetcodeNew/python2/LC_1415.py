
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []  # list storing all the strings of size n
        self.dfs(['a', 'b', 'c'], "", n, res)
        res = sorted(res)
        return res[k - 1] if k <= len(res) else ""

    def dfs(self, s, path, n, res):  # recurisve function for finding all strings
        if n == 0:
            res.append(path)
            return
        # checking whether the currently buildup string's last charachter matches to the new charachter we are appending
        for i in range(3):
            if path and path[-1] == s[i]:
                continue
            self.dfs(s, path + s[i], n - 1, res)


