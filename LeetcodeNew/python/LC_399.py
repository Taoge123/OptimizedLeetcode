"""Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].


The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction."""
"""
这个题其实是一个带权有向图。

题目中给了顶点和顶点之间的关系，其实就是绘制了这个图。然后要求的新的比值其实就是从一个顶点到达另外一个顶点的路径，并且把这条路径上所有的权重相乘。

注意，如果a/b=3，那么从a到b是3，那么从b到a是1/3.

既然是从一个顶点出发到达另外一个顶点，所以应该是dfs解决的问题。

为了防止在DFS中走已经走过了的路，所以需要使用visited保存每次已经访问过的节点
"""

import collections


class SolutionTonnie:
    def calcEquation(self, equations, values, queries):
            graph = collections.defaultdict(dict)
            for (x, y), val in zip(equations, values):
                graph[x][y] = val
                graph[y][x] = 1 / val

            res = []
            for i, j in queries:
                visited = set()
                res.append(self.dfs(graph, i, j, 1.0, visited))
            return res

    def dfs(self, graph, node, target, path, visited):
            # node in graph -> counter example -> query = (x, x)
            if node == target and node in graph:
                return path
            if node in visited:
                return -1.0

            visited.add(node)
            for nei in graph[node]:
                res = self.dfs(graph, nei, target, path * graph[node][nei], visited)
                if res != -1:
                    return res
            return -1.0



class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        res = []
        for u, v in queries:
            if u in graph and v in graph:
                res.append(self.dfs(graph, u, v, set()))
            else:
                res.append(-1)

        return res

    def dfs(self, graph, i, j, visited):
        if i == j:
            return 1

        for nei in graph[i]:
            if nei in visited:
                continue
            visited.add(nei)
            div = self.dfs(graph, nei, j, visited)
            if div > 0:
                return graph[i][nei] * div

        return -1




class SolutionBFS:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1 / v
        res = []
        for i, j in queries:
            res.append(self.bfs(graph, i, j))
        return res

    def bfs(self, graph, i, j):
        if not (i in graph and j in graph):
            return -1.0
        queue = [(i, 1.0)]
        visited = set()
        for x, val in queue:
            if x == j:
                return val
            visited.add(x)
            for y in graph[x]:
                if y not in visited:
                    queue.append((y, val * graph[x][y]))
        return -1.0


class DJS:
    def __init__(self, alphabet):
        self.parent = {char: char for char in alphabet}
        self.vals = {char: 1.0 for char in alphabet}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]

    def union(self, y, x, val):
        x, valx = self.find(x)
        y, valy = self.find(y)
        if x == y: return
        self.parent[y] = self.parent[x]
        self.vals[y] = val * valx / valy


class SolutionUF2:
    def calcEquation(self, equations, values, queries):
        chars = set(sum(equations, []))
        uf = DJS(chars)
        for (y, x), val in zip(equations, values):
            uf.union(y, x, val)

        res = []
        for y, x in queries:
            if x not in chars or y not in chars:
                res.append(-1.0)
                continue
            y, valy = uf.find(y)
            x, valx = uf.find(x)
            if x == y:
                res.append(valy / valx)
            else:
                res.append(-1.0)
        return res


"""
node1 has two paths to root parent2 and they should be equal: 
weight[node1] * weight[parent1] = value * weight[node2]
so that weight[parent1] = value * weight[node2] / weight[node1].
"""
class SolutionUF1:
    def union(self, i, j, parents, weights, value):
        x = self.find(i, parents, weights)
        y = self.find(j, parents, weights)
        if x != y:
            # IMPORTANT: Node1 may already be compressed: its weight could be the product of all weights up to x

            parents[x] = y
            weights[x] = value * (weights[j] / weights[i])

    def find(self, i, parents, weights):
        # Find parent i of a given i, doing path compression while doing so
        # (set the i's parent to its root and multiply all weights along the way.)
        if parents[i] != i:
            p = parents[i]
            parents[i] = self.find(parents[i], parents, weights)
            weights[i] = weights[i] * weights[p]
        return parents[i]

    def calcEquation(self, equations, values, queries):
        parents = {}  # {Child:Parent}, eg {'a':'b'}
        weights = {}  # {Node: float}, eg{'a': 1.0}
        res = []

        for (x, y), value in zip(equations, values):
            if x not in parents:
                parents[x] = x
                weights[x] = 1.0
            if y not in parents:
                parents[y] = y
                weights[y] = 1.0
            self.union(x, y, parents, weights, value)

        for i, j in queries:
            if i not in parents or j not in parents:
                res.append(-1.0)
            else:
                parent1 = self.find(i, parents, weights)
                parent2 = self.find(j, parents, weights)
                if parent1 != parent2:
                    res.append(-1.0)
                else:
                    res.append(weights[i] / weights[j])

        return res


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

a = Solution()
print(a.calcEquation(equations, values, queries))





