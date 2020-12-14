
import heapq
import collections


class Solution:
    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        heap = [(0, 0)]
        dist = {0: 0}
        visited = {}
        res = 0

        while heap:
            step, node = heapq.heappop(heap)
            if step > dist[node]:
                continue
            res += 1
            for nei, w in graph[node].items():
                v = min(w, M - step)
                visited[node, nei] = v

                newStep = step + w + 1
                if newStep < dist.get(nei, M + 1):
                    heapq.heappush(heap, (newStep, nei))
                    dist[nei] = newStep

        for u, v, w in edges:
            res += min(w, visited.get((u, v), 0) + visited.get((v, u), 0))

        return res




class SolutionComments:
    def reachableNodes(self, edges, M, N):
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        heap = [(0, 0)]
        dist = {0 : 0}
        visited = {}
        res = 0

        while heap:
            step, node = heapq.heappop(heap)
            if step > dist[node]:
                continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            res += 1
            for nei, w in graph[node].items():
                # M - d is how much further we can walk from this node;
                # w is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(w, M - step)
                visited[node, nei] = v

                # newStep is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                newStep = step + w + 1
                if newStep < dist.get(nei, M+ 1):
                    heapq.heappush(heap, (newStep, nei))
                    dist[nei] = newStep

        # At the end, each edge (u, v, w) can be visited with a maximum
        # of w new nodes: a max of visited[u, v] nodes from one side,
        # and visited[v, u] nodes from the other.
        for u, v, w in edges:
            res += min(w, visited.get((u, v), 0) + visited.get((v, u), 0))

        return res

