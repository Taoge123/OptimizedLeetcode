
class Solution:
    def partition(self, s):

        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return

        for i in range(1, len(s ) +1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)


    def isPar(self, s):
        return s == s[::-1]






