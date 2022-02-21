class SolutionTony:
    def maxUniqueSplit(self, s: str) -> int:

        n = len(s)
        self.res = 0

        def dfs(s, i, path, visited):
            # print(i, path, len(path))
            if i >= n:
                self.res = max(self.res, len(path))
                return

            for j in range(i + 1, n + 1):
                if s[i:j] in visited:
                    continue
                visited.add(s[i:j])
                dfs(s, j, path + [s[i:j]], visited)
                visited.remove(s[i:j])

        visited = set()
        dfs(s, 0, [], visited)
        return self.res




class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.visited = set()
        self.res = 0
        self.dfs(s, 0, 0)
        return self.res

    def dfs(self, s, pos, count):
        n = len(s)
        if pos == n:
            self.res = max(self.res, count)
            return

        # optimization
        if count + (n - pos) <= self.res:
            return

        for i in range(pos, n):
            if s[pos: i+1] not in self.visited:
                self.visited.add(s[pos:i + 1])
                self.dfs(s, i + 1, count + 1)
                self.visited.remove(s[pos:i + 1])


