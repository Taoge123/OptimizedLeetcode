import collections
import heapq


class SolutionFloydWarshall:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        dp = [[float('inf') for i in range(N)] for j in range(N)]
        for u, v, w in times:
            dp[u - 1][v - 1] = w

        for i in range(N):
            dp[i][i] = 0

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

        res = 0
        for i in range(N):
            #需要达到所有的nodes, 所以需要取最大值
            res = max(res, dp[K - 1][i])

        return res if res < float('inf') else -1
        # return max(dp[K-1]) if max(dp[K-1]) < float("inf") else -1



class SolutionBellmanFord:
    def networkDelayTime(self, times, N: int, K: int) -> int:
        dp = [float('inf') for i in range(N)]
        dp[K - 1] = 0
        for i in range(N - 1):
            for u, v, w in times:
                if dp[u - 1] + w < dp[v - 1]:
                    dp[v - 1] = dp[u - 1] + w

        return max(dp) if max(dp) < float('inf') else -1



class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:

        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        heap = []
        heapq.heappush(heap, (0, k))
        distance = collections.defaultdict(int)

        while heap:
            time, node = heapq.heappop(heap)
            if node not in distance:
                distance[node] = time
                for nei in graph[node]:
                    heapq.heappush(heap, (distance[node] + graph[node][nei], nei))

        if len(distance) != n:
            return -1
        return max(distance.values())


class SolutionDFS:
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((w, v))

        dist = {node: float('inf') for node in range(1, N + 1)}

        def dfs(node, elapsed):
            if elapsed >= dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1



class SolutionDFSTony:
    def networkDelayTime(self, times, n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        dist = {node: float('inf') for node in range(1, n + 1)}

        for u, v, t in times:
            graph[u].append([t, v])

        def dfs(node, steps):
            if steps >= dist[node]:
                return
            dist[node] = steps
            for time, nei in sorted(graph[node]):
                dfs(nei, steps + time)

        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1


