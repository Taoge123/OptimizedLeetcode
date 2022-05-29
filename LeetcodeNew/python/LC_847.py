"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/147123/Python-8-lines-Heapq-and-BFS-and-Deque-solutions
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/605161/Python-DFS-with-memoization-accepted
"""

import collections


class SolutionBFSTOny:
    def shortestPathLength(self, graph):
        if not graph or not graph[0]:
            return 0
        n = len(graph)
        full_mask = (1 << n) - 1

        queue = collections.deque()
        visited = set()
        for node in range(n):
            queue.append([node, 1 << node])
            visited.add((node, 1 << node))
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node, mask = queue.popleft()
                if mask == full_mask:
                    return step
                for nei in graph[node]:
                    new_mask = mask
                    new_mask |= (1 << nei)
                    if (nei, new_mask) in visited:
                        continue
                    queue.append([nei, new_mask])
                    visited.add((nei, new_mask))
            step += 1
        return step


class SolutionDFSMemo:
    def shortestPathLength(self, graph):

        def dfs(node, mask):
            if (node, mask) in memo:
                return memo[(node, mask)]
            if mask & (mask - 1) == 0:
                # Base case - mask only has a single "1", which means
                # that only one node has been visited (the current node)
                return 0

            memo[(node, mask)] = float("inf")  # Avoid infinite loop in recursion
            for nei in graph[node]:
                if mask & (1 << nei):
                    no_pick = 1 + dfs(nei, mask)
                    pick = 1 + dfs(nei, mask ^ (1 << node))
                    memo[(node, mask)] = min(memo[(node, mask)], pick, no_pick)

            return memo[(node, mask)]

        n = len(graph)
        full_mask = (1 << n) - 1
        memo = {}
        return min(dfs(node, full_mask) for node in range(n))



class Solution:
    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        finalState = (1 << n) - 1
        print(bin(finalState), finalState)
        queue = collections.deque()
        visited = set()

        for node in range(n):
            queue.append([node, 1 << node])
            visited.add((node, 1 << node))

        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node, state = queue.popleft()
                if state == finalState:
                    return step

                for nei in graph[node]:
                    nextState = state | (1 << nei)

                    if (nei, nextState) in visited:
                        continue

                    queue.append([nei, nextState])
                    visited.add((nei, nextState))
            step += 1

        return -1




class SolutionCS:
    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        fullMask = (1 << n) - 1

        visited = set()
        queue = collections.deque()
        for i in range(len(graph)):
            node = (i, 1 << i)
            queue.append(node)
            visited.add(node)

        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node[1] == fullMask:
                    return res
                for nei in graph[node[0]]:
                    nxt = (nei, node[1] | (1 << nei))
                    if tuple(nxt) not in visited:
                        queue.append(nxt)
                        visited.add(nxt)
            res += 1
        return -1

