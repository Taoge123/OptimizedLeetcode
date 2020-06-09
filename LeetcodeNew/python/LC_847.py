"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/discuss/147123/Python-8-lines-Heapq-and-BFS-and-Deque-solutions
"""

import collections


class Solution:
    def shortestPathLength(self, graph) -> int:
        if not graph or not graph[0]:
            return 0

        n = len(graph)
        # {node, state}
        finalState = 0
        for i in range(n):
            finalState |= (1 << i)

        queue = collections.deque()
        visited = set()
        for i in range(n):
            queue.append([i, 1 << i])
            visited.add((i, 1 << i))

        step = -1
        while queue:
            step += 1
            size = len(queue)
            for i in range(size):
                node, state = queue.popleft()
                for nextNode in graph[node]:
                    nextState = state | (1 << nextNode)
                    if nextState == finalState:
                        return step + 1

                    if (nextNode, nextState) in visited:
                        continue
                    queue.append([nextNode, nextState])
                    visited.add((nextNode, nextState))

        return -1



