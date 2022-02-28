
"""
89. Gray Code
"""


class SolutionRika:
    def circularPermutation(self, n: int, start: int):
        res = []
        res.append(start)

        visited = set()
        visited.add(start)

        self.dfs(n, visited, start, res)
        return res

    def dfs(self, n, visited, code, res):

        if len(res) == 1 << n:
            return True

        mask = 1
        for i in range(n):
            new_code = code ^ (mask << i)
            if new_code in visited:
                continue
            visited.add(new_code)
            res.append(new_code)
            if self.dfs(n, visited, new_code, res):
                return True
            visited.remove(new_code)
            res.pop()

        return False



class Solution:
    def circularPermutation(self, n: int, start: int):
        res = []
        res.append(0)

        for i in range(n):
            step = len(res)
            for j in range(step - 1, -1, -1):
                res.append(res[j] | (1 << i))

        i = res.index(start)
        return res[i:] + res[:i]



