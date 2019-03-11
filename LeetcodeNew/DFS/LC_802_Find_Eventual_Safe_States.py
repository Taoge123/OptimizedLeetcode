"""
Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.


"""


import collections


class Solution1:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # color[i], 0 means not visited. 1 means safe. 2 means unsafe.
        color = [0] * len(graph)
        res = []
        for start in range(len(graph)):
            if self.dfs(graph, start, color):
                res.append(start)
        res.sort()
        return res

    def dfs(self, graph, start, color):
        # 返回start节点是否是安全，如果是，返回True
        if color[start] != 0:
            return color[start] == 1
        color[start] = 2
        for e in graph[start]:
            if not self.dfs(graph, e, color):
                return False
        color[start] = 1
        return True


# ---------------------
# 作者：fuxuemingzhu
# 来源：CSDN
# 原文：https: // blog.csdn.net / fuxuemingzhu / article / details / 82749341
# 版权声明：本文为博主原创文章，转载请附上博文链接！
class Solution2:
    def eventualSafeNodes(self, graph):
        N = len(graph)
        safe = [False] * N

        graph = map(set, graph)
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]







"""As in Approach #1, the crux of the problem is whether you reach a cycle or not.

Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually.
This is a classic "white-gray-black" DFS algorithm that would be part of any textbook on DFS.
We mark a node gray on entry, and black on exit.
If we see a gray node during our DFS, it must be part of a cycle.
In a naive view, we'll clear the colors between each search.
"""

class Solution:
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))







