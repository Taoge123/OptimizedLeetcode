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


