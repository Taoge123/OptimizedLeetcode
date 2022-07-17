"""
https://leetcode.com/problems/frog-position-after-t-seconds/discuss/532486/Python-DFS-in-a-Tree
https://www.youtube.com/watch?v=B5nDIxkoEyo

"""

import collections

class SolutionTony:
    def frogPosition(self, n: int, edges, t: int, target: int):
        graph = collections.defaultdict(list)
        # fake parent for node 1
        graph[1].append(-1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0

        def dfs(node, parent, t, prob):
            # not enough t
            if t < 0:
                return

            # match target
            if node == target:
                # no more t or no more nei
                if t == 0 or len(graph[node]) == 1:
                    self.res = prob
                return

            # no nei, return
            if len(graph[node]) == 1:
                return

            # calculate new prob
            for nei in graph[node]:
                if nei != parent:
                    dfs(nei, node, t - 1, prob / (len(graph[node]) - 1))

        dfs(1, -1, t, 1.0)
        return self.res




class SolutionBFS:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1

        graph = collections.defaultdict(list)
        graph[1].append(1)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue = collections.deque([(1, 0, 1, 2)])
        visited = set([1])

        while queue:
            node, time, prob, seen = queue.popleft()
            nei = 0  # Number of unvisited neighbors
            for adj in graph[node]:
                if (1 << adj) & seen == 0:  # checks if adj has been visited, seen is just an integer to store visited nodes
                    nei += 1

            if node == target:
                if time == t or (time < t and nei == 0):
                    return prob
                else:
                    return 0
            prob_nei = 1 / nei if nei else 0

            for adj in graph[node]:
                if (1 << adj) & seen == 0:  # if neighbor is unvisited
                    queue.append([adj, time + 1, prob * prob_nei, seen ^ (1 << adj)])
        return 0


class SolutionDFS:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1.0
        graph = [[] for i in range(n + 1)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = [0] * (n + 1)
        return self.dfs(graph, 1, t, visited, target)

    def dfs(self, graph, node, t, visited, target):
        if node != 1 and len(graph[node]) == 1 or t == 0:
            return node == target
        visited[node] = 1
        res = sum(self.dfs(graph, nei, t - 1, visited, target) for nei in graph[node] if not visited[nei])
        return res * 1.0 / (len(graph[node]) - (node != 1))


class SolutionDFS2:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        graph = collections.defaultdict(list)
        # fake parent for node 1
        graph[1].append(-1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        self.dfs(1.0, 1, -1, graph, t, target)
        return self.res

    def dfs(self, prob, node, parent, graph, t, target):
        # not enough t
        if t < 0:
            return

        # match target
        if node == target:
            # no more t or no more nei
            if t == 0 or len(graph[node]) == 1:
                self.res = prob
            return

        # no nei, return
        if len(graph[node]) == 1:
            return

        # calculate new prob
        prob /= (len(graph[node]) - 1)
        for nei in graph[node]:
            if nei != parent:
                self.dfs(prob, nei, node, graph, t - 1, target)




