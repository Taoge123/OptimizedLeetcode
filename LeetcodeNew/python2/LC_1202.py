import collections


class SolutionDFS:
    def smallestStringWithSwaps(self, s: str, pairs):
        def dfs(node):
            visited.add(node)
            component.append(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                dfs(nei)

        n = len(s)
        graph = collections.defaultdict(list)
        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        res = list(s)
        for node in range(n):
            if node in visited:
                continue
            component = []
            dfs(node)
            component.sort()
            chars = [res[num] for num in component]
            chars.sort()
            for i in range(len(component)):
                res[component[i]] = chars[i]
        return "".join(res)




class Solution:
    def find(self, i):
        if i== self.parent[i]:
            return self.parent[i]
        return self.find(self.parent[i])

    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        self.parent[x] = y

    def smallestStringWithSwaps(self, s, pairs):
        self.parent = list(range(len(s)))
        for a, b in pairs:
            self.union(a, b)
        table = collections.defaultdict(list)
        for i in range(len(s)):
            table[self.find(i)].append(i)
        res = [''] * len(s)
        for k in table:
            ps = sorted(''.join([s[i] for i in table[k]]))
            for i, p in zip(table[k], ps):
                res[i] = p
        return ''.join(res)


s = "dcab"
pairs = [[0,3],[1,2]]

a = Solution()
print(a.smallestStringWithSwaps(s, pairs))

