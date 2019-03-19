
"""
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115500/Adapted-Dijkstra-python


There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.


"""
import collections
import heapq

class SolutionLee:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = collections.defaultdict(dict)

        for u, v, cost in flights:
            graph[u][v] = cost

        heap = [(0, src, k + 1)]
        while heap:
            cost, i, k = heapq.heappop(heap)
            if i == dst:
                return cost
            if k > 0:
                for j in graph[i]:
                    heapq.heappush(heap, (cost + graph[i][j], j, k - 1))
        return -1


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):

        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        min_heap = [(0, src, K+1)]
        while min_heap:
            result, u, k = heapq.heappop(min_heap)
            if u == dst:
                return result
            if k > 0:
                for v, w in adj[u]:
                    heapq.heappush(min_heap, (result+w, v, k-1))


class Solution2:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        INF = float('inf')
        mn = [INF] * n
        mn[src] = 0

        for k in range(K + 1):
            newmn = mn[:]
            for (a, b, cost) in flights:
                newmn[b] = min(newmn[b], mn[a] + cost)
            mn = newmn

        return mn[dst] if mn[dst] != INF else -1



"""
Intuition and Algorithm

Say pre[node] is the smallest distance to that node within T stops. 
Let's try to find the smallest distance dis[node] to that node within T+1 rounds. 
For every edge in flights that connects places u and v with cost w, 
the new distance would be dis[v] = min(dis[v], pre[u] + w).

Actually, we'll use dis = dist[0] and pre = dist[1] initially. 
That will let us reuse the arrays dis = dist[1] 
and pre = dist[0] for the next iteration (i = 1) in our loop, and so on.
"""


class SolutionBellmanFord:
    def findCheapestPrice(self, n, flights, src, dst, K):

        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        for k in range(K + 1):
            newDist = dist[:]
            for (a, b, cost) in flights:
                newDist[b] = min(newDist[b], dist[a] + cost)
            dist = newDist

        return dist[dst] if dist[dst] != INF else -1


class SolutionDJ:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w

        best = {}
        pq = [(0, 0, src)]
        while pq:
            cost, k, place = heapq.heappop(pq)
            if k > K+1 or cost > best.get((k, place), float('inf')): continue
            if place == dst: return cost

            for nei, wt in graph[place].iteritems():
                newcost = cost + wt
                if newcost < best.get((k+1, nei), float('inf')):
                    heapq.heappush(pq, (newcost, k+1, nei))
                    best[k+1, nei] = newcost

        return -1

