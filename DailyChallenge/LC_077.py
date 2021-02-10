
class Solution:
    def combine(self, n: int, k: int):

        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, n, k, pos, path, res):
        if len(path) == k:
            res.append(path)
            return res

        for i in range(pos, n + 1):
            self.dfs(n, k, i + 1, path + [i], res)


