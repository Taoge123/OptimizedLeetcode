import collections
import functools


class SolutionMemo:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        @functools.lru_cache(None)
        def dfs(node, target):
            if node == target:
                return True

            for nei in graph[node]:
                if dfs(nei, target):
                    return True
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res




class SolutionDP:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        dp = [[False] * n for i in range(n)]

        for i, j in prerequisites:
            dp[i][j] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])

        return [dp[i][j] for i, j in queries]




class SolutionTopo:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        table = collections.defaultdict(set)
        inDegree = [0] * n
        preSet = [set() for i in range(n)]

        for u, v in prerequisites:
            table[u].add(v)
            inDegree[v] += 1

        queue = collections.deque()
        for i in range(n):
            preSet[i].add(i)
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for nei in table[node]:
                for x in preSet[node]:
                    preSet[nei].add(x)

                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        res = []
        for u, v in queries:
            if u in preSet[v]:
                res.append(True)
            else:
                res.append(False)
        return res


