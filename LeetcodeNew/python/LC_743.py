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
    def networkDelayTime(self, times, N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        heap = [(0, K)]
        dist = {}
        while heap:
            time, u = heapq.heappop(heap)
            if u not in dist:
                dist[u] = time
                for v in graph[u]:
                    heapq.heappush(heap, (dist[u] + graph[u][v], v))

        return max(dist.values()) if len(dist) == N else -1



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


