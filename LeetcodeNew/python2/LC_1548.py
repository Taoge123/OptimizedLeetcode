import collections
import functools


class SolutionTony1:
    def mostSimilar(self, n: int, roads, names, targetPath):
        graph = collections.defaultdict(list)

        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        @functools.lru_cache(None)
        def dfs(i, node):
            if i == len(targetPath):
                return (0, [])

            res = float('inf')
            final_path = []
            # dist = 1 if names[node] != targetPath[i] else 0
            for nei in graph[node]:
                dist, path = dfs(i + 1, nei)
                if (names[node] != targetPath[i]) + dist < res:
                    final_path = path
                    res = (names[node] != targetPath[i]) + dist

            return (res, [node] + final_path)

        res = float('inf')
        final_path = []
        for node in graph:
            dist, path = dfs(0, node)
            if res > dist:
                final_path = path
                res = dist

        return final_path


class SolutionTony:
    def mostSimilar(self, n, roads, names, targetPath):

        graph = collections.defaultdict(list)
        cities = set()
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            cities.add(u)
            cities.add(v)

        graph[-1] = list(cities)
        memo = {}
        return self.dfs(graph, roads, names, targetPath, 0, -1, memo)[1]

    def dfs(self, graph, roads, names, targetPath, i, node, memo):

        if (i, node) in memo:
            return memo[(i, node)]

        if i == len(targetPath):
            return [0, []]

        res = float('-inf')
        best_path = []

        for nei in graph[node]:
            match, path = self.dfs(graph, roads, names, targetPath, i + 1, nei, memo)
            if targetPath[i] == names[nei]:
                match += 1
            if match > res:
                res = match
                best_path = [nei] + path
        memo[(i, node)] = [res, best_path]
        return memo[(i, node)]



class Solution:
    def mostSimilar(self, n, roads, names, targetPath):

        # 1. Convert roads to a map from city x we can travel to cities a, b,c.  g[x] = [a,b,c]
        graph = collections.defaultdict(list)
        cities = set()
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            cities.add(u)
            cities.add(v)
        graph[-1] = list(cities)  # This allows us to start our journey at any city

        # 2. Search for the best path
        @functools.lru_cache(None)
        def dfs(i, node):
            if i == len(targetPath):
                return (0, tuple())

            best = float('-inf')
            best_path = tuple()

            # Find which nei produces a path closest to targetPath
            for nei in graph[node]:
                # best path from nei onwards
                points, path = dfs(i + 1, nei)
                # plus 1 point for matching targetPath
                if targetPath[i] == names[nei]:
                    points += 1
                if points > best:
                    best = points
                    # add nei to the best path
                    best_path = tuple([nei]) + path

            return (best, best_path)

        return dfs(0, -1)[1]

