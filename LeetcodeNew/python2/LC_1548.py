import collections
import functools


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

