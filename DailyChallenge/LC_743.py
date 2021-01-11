class Solution:
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


