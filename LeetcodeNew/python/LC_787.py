
import collections
import heapq
import functools




class SolutionMemo:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        @functools.lru_cache(maxsize=None)
        def dfs(node, k):
            if node == dst:
                return 0
            if k <= 0:
                return float("inf")

            res = float("inf")
            for nei in graph[node]:
                res = min(res, graph[node][nei] + dfs(nei, k - 1))
            return res

        res = dfs(src, k + 1)
        return res if res != float("inf") else -1




class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        memo = {}
        res = self.dfs(graph, src, dst, k + 1, memo)
        return res if res != float("inf") else -1

    def dfs(self, graph, node, dest, k, memo):
        if (node, k) in memo:
            return memo[(node, k)]

        if node == dest:
            return 0
        if k <= 0:
            return float("inf")

        res = float("inf")
        for nei in graph[node]:
            res = min(res, graph[node][nei] + self.dfs(graph, nei, dest, k - 1, memo))

        memo[(node, k)] = res
        return res


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        table = collections.defaultdict(dict)
        for a, b, cost in flights:
            table[a][b] = cost

        heap = [(0, src, k + 1)]
        while heap:
            cost, i, k = heapq.heappop(heap)
            if i == dst:
                return cost
            if k > 0:
                for nei in table[i]:
                    heapq.heappush(heap, (cost + table[i][nei], nei, k - 1))
        return -1





class SolutionFloyd:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:
        dp = [float('inf') for i in range(n)]

        dp[src] = 0
        for k in range(K+1):
            prevDP = dp[:]
            for a, b, cost in flights:
                dp[b] = min(dp[b], prevDP[a] + cost)

        return dp[dst] if dp[dst] != float('inf') else -1




