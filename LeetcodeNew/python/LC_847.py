"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/147123/Python-8-lines-Heapq-and-BFS-and-Deque-solutions
"""

import collections

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

