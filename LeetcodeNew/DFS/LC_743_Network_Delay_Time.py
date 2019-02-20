
"""
这道题给了我们一些有向边，又给了一个结点K，问至少需要多少时间才能从K到达任何一个结点。
这实际上是一个有向图求最短路径的问题，我们求出K点到每一个点到最短路径，
然后取其中最大的一个就是需要的时间了。可以想成从结点K开始有水流向周围扩散，
当水流到达最远的一个结点时，那么其他所有的结点一定已经流过水了。
最短路径的常用解法有迪杰克斯特拉算法Dijkstra Algorithm,
弗洛伊德算法Floyd-Warshall Algorithm, 和贝尔曼福特算法Bellman-Ford Algorithm，
其中，Floyd算法是多源最短路径，即求任意点到任意点到最短路径，
而Dijkstra算法和Bellman-Ford算法是单源最短路径，即单个点到任意点到最短路径。
这里因为起点只有一个K，所以使用单源最短路径就行了。这三种算法还有一点不同，
就是Dijkstra算法处理有向权重图时，权重必须为正，而另外两种可以处理负权重有向图，
但是不能出现负环，所谓负环，就是权重均为负的环。为啥呢，这里要先引入松弛操作Relaxtion，
这是这三个算法的核心思想，当有对边 (u, v) 是结点u到结点v，
如果 dist(v) > dist(u) + w(u, v)，那么 dist(v) 就可以被更新，这是所有这些的算法的核心操作。
Dijkstra算法是以起点为中心，向外层层扩展，直到扩展到终点为止。根据这特性，
用BFS来实现时再好不过了，注意while循环里的第一层for循环，这保证了每一层的结点先被处理完，
才会进入进入下一层，这种特性在用BFS遍历迷宫统计步数的时候很重要。对于每一个结点，
我们都跟其周围的结点进行Relaxtion操作，从而更新周围结点的距离值。为了防止重复比较，
我们需要使用visited数组来记录已访问过的结点，最后我们在所有的最小路径中选最大的返回，
注意，如果结果res为INT_MAX，说明有些结点是无法到达的，返回-1。
普通的实现方法的时间复杂度为O(V2)，基于优先队列的实现方法的时间复杂度为O(E + VlogV)，
其中V和E分别为结点和边的个数，这里多说一句，Dijkstra算法这种类贪心算法的机制，
使得其无法处理有负权重的最短距离，还好这道题的权重都是正数
"""


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        result = [-1] * (N + 1)
        visited = [False] * (N + 1)
        dist = [[-1] * (N + 1) for _ in range(N + 1)]
        for (s, e, t) in times:
            dist[s][e] = t

        result[K] = 0
        for _ in range(N):
            idx = None
            for i in range(1, N + 1):
                if not visited[i] and result[i] != -1 and (idx == None or result[i] < result[idx]):
                    idx = i
            if idx == None:
                return -1
            else:
                visited[idx] = True

            for j in range(1, N + 1):
                if not visited[j] and dist[idx][j] != -1 and (
                        result[j] == -1 or result[j] > result[idx] + dist[idx][j]):
                    result[j] = result[idx] + dist[idx][j]
        return max(result)



class Solution2:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        K -= 1
        nodes = collections.defaultdict(list)
        for u, v, w in times:
            nodes[u - 1].append((v - 1, w))
        dist = [float('inf')] * N
        dist[K] = 0
        done = set()
        for _ in range(N):
            smallest = min((d, i) for (i, d) in enumerate(dist) if i not in done)[1]
            for v, w in nodes[smallest]:
                if v not in done and dist[smallest] + w < dist[v]:
                    dist[v] = dist[smallest] + w
            done.add(smallest)
        return -1 if float('inf') in dist else max(dist)



# Floyd-Warshall算法。这个算法TLE


class Solution3:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [[float('inf')] * N for _ in range(N)]
        for time in times:
            u, v, w = time[0] - 1, time[1] - 1, time[2]
            d[u][v] = w
        for i in range(N):
            d[i][i] = 0
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return -1 if float('inf') in d[K - 1] else max(d[K - 1])



# Bellman-Ford算法，这个算法TLE
class Solution4:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf')] * N
        dist[K - 1] = 0
        for i in range(N):
            for time in times:
                u = time[0] - 1
                v = time[1] - 1
                w = time[2]
                dist[v] = min(dist[v], dist[u] + w)
        return -1 if float('inf') in dist else max(dist)



