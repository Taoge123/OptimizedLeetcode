
"""
https://blog.csdn.net/fuxuemingzhu/article/details/83307822

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops.
If there is no such route, output -1.

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
"""
Idea
It happen to be the same idea of Dijkstra's algorithm, but we need to keep the path.
More
More helpful and detailed explanation here:
https://en.wikipedia.org/wiki/Dijkstra's_algorithm
"""
import collections
import heapq

class SolutionLee:
    def findCheapestPrice(self, n, flights, src, dst, k):
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1


class Solution2:
    def findCheapestPrice(self, n, flights, src, dst, K):

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
题目大意
有N个城市，m个航班，他们之间的连接是个有向图。现在已知最多可以中转k次，求从srt到dst的最小花费。

解题方法
图的遍历的基础上加上了一个限制条件：最多中转k次，即最多只能访问k+1个节点。可以用DFS和BFS两者方法去解决。

方法一：DFS
这个其实就是回溯法，先从起点开始向后搜索，如果搜索到了dst或者没有步数了，那么换下一条路进行搜索。
需要使用一个visited数组表示已经搜索过的节点，这样可以防止走成一个环。

另外这个题需要一个强剪枝，就是当某条路径的花费大于了我们当前到达dst需要花费的最小值的时候，后面的路径都不需要走了，
这个是由于题目给出的路费都是整数，向下走哪怕走到了dst花费也会更高。

时间复杂度是O(N^2)，空间复杂度是O(1).打败了6%的提交。
"""
class Solution3:
    def findCheapestPrice(self, n, flights, src, dst, K):

        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        visited = [0] * n
        ans = [float('inf')]
        self.dfs(graph, src, dst, K + 1, 0, visited, ans)
        return -1 if ans[0] == float('inf') else ans[0]

    def dfs(self, graph, src, dst, k, cost, visited, ans):
        if src == dst:
            ans[0] = cost
            return
        if k == 0:
            return
        for v, e in graph[src].items():
            if visited[v]: continue
            if cost + e > ans[0]: continue
            visited[v] = 1
            self.dfs(graph, v, dst, k - 1, cost + e, visited, ans)
            visited[v] = 0


"""
方法二：BFS
如果给定步数的情况下，一个更直接的方法就是BFS，这样就可以直接判断在指定的k步以内能不能走到dst，
不会进行更多的搜索了，因此这个方法要快很多。

BFS是个模板，直接使用一个队列很容易就实现了。这个队列存放的是当我们进行第step次搜索时，
搜索到的当前的节点，以及走到当前节点的花费。所以当当前节点走到dst时，更新最小花费。

时间复杂度是O(KN)，空间复杂度是O(N).打败了60%的提交。

"""
class Solution4:
    def findCheapestPrice(self, n, flights, src, dst, K):

        graph = collections.defaultdict(dict)
        for u, v, e in flights:
            graph[u][v] = e
        ans = float('inf')
        que = collections.deque()
        que.append((src, 0))
        step = 0
        while que:
            size = len(que)
            for i in range(size):
                cur, cost = que.popleft()
                if cur == dst:
                    ans = min(ans, cost)
                for v, w in graph[cur].items():
                    if cost + w > ans:
                        continue
                    que.append((v, cost + w))
            if step > K: break
            step += 1
        return -1 if ans == float('inf') else ans


"""
解题思路：
动态规划（Dynamic Programming）

状态转移方程：

ans = min(ans, costs[k] + prices[k][dst])
​其中costs[k]表示到达位置k时的最小花费，prices[k][dst]表示从k到达dst的航班价格。
"""

class SolutionBF:
    def findCheapestPrice(self, n, flights, src, dst, K):

        INF = 0x7FFFFFFF
        prices = collections.defaultdict(lambda: collections.defaultdict(int))
        for s, t, p in flights:
            prices[s][t] = p
        ans = prices[src][dst] or INF
        queue = [src]
        costs = {src : 0}
        for x in range(K + 1):
            nset = set()
            for loc in queue:
                ans = min(ans, costs[loc] + (prices[loc][dst] or INF))
                for next in prices[loc]:
                    costs[next] = min(costs.get(next, INF), costs[loc] + (prices[loc][next] or INF))
                    nset.add(next)
            queue = list(nset)
        return ans if ans < INF else -1


class Solution5:
    def findCheapestPrice(self, n, flights, src, dst, K):
        dist = [[float('inf')] * n for _ in range(2)]
        dist[0][src] = dist[1][src] = 0

        for i in range(K+1):
            for u, v, w in flights:
                dist[i&1][v] = min(dist[i&1][v], dist[~i&1][u] + w)

        return dist[K&1][dst] if dist[K&1][dst] < float('inf') else -1


class Solution6:
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

