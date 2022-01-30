"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/discuss/661774/Python3-Easy-Short-DFS
https://www.youtube.com/watch?v=96xJAHhOIo4



"""


import collections


class SolutionDFS2:
    def minReorder(self, n: int, connections):

        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)

        for u, v in connections:
            roads.add((u, v))
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                if (node, nei) in roads:
                    self.res += 1
                dfs(nei)

        visited = set()
        dfs(0)
        return self.res




class SolutionDFS:
    def minReorder(self, n: int, connections):

        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)

        for u, v in connections:
            roads.add((u, v))
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            if (parent, node) in roads:
                self.res += 1

            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        dfs(0, -1)
        return self.res



class SolutionBFS:
    def minReorder(self, n: int, connections) -> int:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        connections = set(map(tuple, connections))
        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)

        res = 0
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    if (node, nei) in connections:
                        res += 1
                    queue.append(nei)
                    visited.add(nei)
        return res



