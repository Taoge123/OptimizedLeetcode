
import heapq
import collections

class SolutionDijkstra:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        cost = [[float('inf')] * n for _ in range(n)]
        graph = collections.defaultdict(list)
        for u, v, c in edges:
            cost[u][v ] =cost[v][u] = c
            graph[u].append(v)
            graph[v].append(u)

        def dijkstra(i):
            distance = [float('inf')] * n
            distance[i] = 0
            heap = [(0, i)]
            heapq.heapify(heap)
            while heap:
                c, node = heapq.heappop(heap)
                if c > distance[node]:
                    continue
                for nei in graph[node]:
                    newC = c + cost[node][nei]
                    if newC < distance[nei]:
                        distance[nei] = newC
                        heapq.heappush(heap, (newC, nei))
            return sum(d <= distanceThreshold for d in distance) - 1

        table = {dijkstra(i) : i for i in range(n)}
        # print(table)
        return table[min(table)]


import heapq


class SolutionFloyWarshall:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        # def findTheCity(self, n, edges, distanceThreshold):
        dp = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dp[i][j] = dp[j][i] = w

        for i in range(n):
            dp[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        table = {sum(d <= distanceThreshold for d in dp[i]): i for i in range(n)}
        return table[min(table)]


