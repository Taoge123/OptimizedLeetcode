"""
解法1：常规BFS
常规的BFS解法就是从start出发往周围的点遍历。但是，并不是某个点被遍历过之后就不要再遍历了。这是因为通过不同路径到达某个点时的概率是不同的。某些路径虽然在BFS的算法中晚遍历到点A，但路径概率更大，这就意味着从A往后延伸的路径必须再次重新遍历。这个算法的时间复杂度可以很高。

解法2：Dijkstra 贪心
回顾一下Dijkstra算法。它适合单源非负权重图。所谓“单源”，就是它只能求某个特定节点作为起点的最短路径。思想是基于BFS的贪心策略。在队列中的所有节点都按照“（从起点）到达路径长度”排序，任何轮次中，最先弹出的节点A如果之前从没有访问过，那么它所对应的路径就一定是从起点到A的最短路径。

本题需要改造一番才能使用Dijkstra算法。原本的题意是求最大乘积路径问题：

maxmize prob(E1)*prob(E2)*...*prob(Ek)
= maxmize log[prob(E1)]+log[prob(E2)] + ... + log[prob(Ek)]
= minimize -log[prob(E1)] -log[prob(E2)] - ... -log[prob(Ek)]
我们发现每条边的-log[prob(Ek)]都是正数，并且目标是最小化路径之和。所以考虑-log[prob(Ek)]为权重的图，原题就可以转化成标准的最短路径问题。

"""

import collections
import heapq

class Solution:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        graph = collections.defaultdict(dict)
        for i, (u, v) in enumerate(edges):
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
        queue = collections.deque([(start, 1)])
        prob = [0] * n
        prob[start] = 1
        while queue:
            node, p = queue.popleft()
            if node == end:
                continue
            for nei, neiP in graph[node].items():
                if neiP * p > prob[nei]:
                    queue.append((nei, neiP * p))
                    prob[nei] = neiP * p
        return prob[end]




"""
Dijkstra : single source, non-ngeative weight, min weight sum

heap, {node, distance from start to node}
for the popped node, if never been visited, distance from start to node is the optimal distance for this node

"""



class Solution2:
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        prob = [0.0] * n
        graph = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, i))
            graph[v].append((u, i))
        prob[start] = 1.0
        heap = [(-prob[start], start)]
        while heap:
            p, node = heapq.heappop(heap)
            if node == end:
                return -p
            for newP, nei in graph[node]:
                if -p * succProb[nei] > prob[newP]:
                    prob[newP] = -p * succProb[nei]
                    heapq.heappush(heap, (-prob[newP], newP))
        return 0.0



