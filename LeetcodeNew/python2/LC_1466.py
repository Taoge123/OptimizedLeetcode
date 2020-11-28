import collections


class Solution:
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



