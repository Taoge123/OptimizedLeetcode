"""

https://leetcode.com/problems/tree-diameter/discuss/418982/Java-Depth-of-the-Tree-solution-Time-O(N)-Easy-to-understand

250. Count Univalue Subtrees
508. Most Frequent Subtree Sum
543. Diameter of Binary Tree
1245. Tree Diameter
687. Longest Univalue Path
124. Binary Tree Maximum Path Sum
Max Path Sum in a Grid
298. Binary Tree Longest Consecutive Sequence
549. Binary Tree Longest Consecutive Sequence II

- Similar problem: https://leetcode.com/problems/diameter-of-binary-tree/
- Travese all the nodes of the tree. The diameter of the tree is maximum of the longest path through each node.
- Longest path through a node is sum of top 2 depths of children's tree.

"""

import collections


class SolutionRika:
    def treeDiameter(self, edges):
        # max height and maxx height of two nodes --> each node return max height of child node
        if not edges:
            return 0

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = float('-inf')
        self.dfs(graph, -1, 0)
        return self.res

    def dfs(self, graph, p, node):

        maxval1 = 0
        maxval2 = 0
        for child in graph[node]:
            if child != p:
                val = self.dfs(graph, node, child)
                if val > maxval1:
                    maxval2 = maxval1
                    maxval1 = val
                elif val > maxval2:
                    maxval2 = val

        self.res = max(self.res, maxval1 + maxval2)
        return maxval1 + 1



class Solution:
    def treeDiameter(self, edges) -> int:
        n = len(edges) + 1
        self.res = 0
        graph = [[] for i in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.dfs(0, -1, graph)
        return self.res

    def dfs(self, root, parent, graph):
        first = 0
        second = 0

        for child in graph[root]:
            if child == parent:
                continue

            childDepth = self.dfs(child, root, graph)
            if childDepth > first:
                second = first
                first = childDepth
            elif childDepth > second:
                second = childDepth

        longest = first + second + 1
        self.res = max(self.res, longest - 1)
        return first + 1




class Solution2:
    def treeDiameter(self, edges) -> int:
        if not edges:
            return 0
        n = len(edges)
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        diameter = [0]
        visited = (n + 1) * [False]
        for i in range(n + 1):
            if not visited[i]:
                self.dfs(i, graph, visited, diameter)
        return diameter[0]

    def dfs(self, i, graph, visited, diameter):
        visited[i] = True
        neigh_depths = []
        for j in graph[i]:
            if not visited[j]:
                neigh_depths.append(self.dfs(j, graph, visited, diameter))
        neigh_depths.sort(reverse=True)
        if not neigh_depths:
            return 1
        else:
            diameter[0] = max(diameter[0], sum(neigh_depths[:2]))
            return 1 + neigh_depths[0]










