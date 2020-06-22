
import collections
import heapq

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
        for k in range( K +1):
            prevDP = dp[:]
            for a, b, cost in flights:
                dp[b] = min(dp[b], prevDP[a] + cost)

        return dp[dst] if dp[dst] != float('inf') else -1




