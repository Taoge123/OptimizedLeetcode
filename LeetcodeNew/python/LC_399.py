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

class Solution:
    def calcEquation(self, equations, values, queries):

        table = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            table[x][y] = val
            table[y][x] = 1.0 / val

        res = []
        for i, j in queries:
            if i in table and j in table:
                res.append(self.dfs(i, j, table, set()))
            else:
                res.append(-1.0)
        return res

    def dfs(self, i, j, table, visited):
        if i == j:
            return 1.0
        visited.add(i)

        for n in table[i]:
            if n in visited:
                continue
            visited.add(n)
            div = self.dfs(n, j, table, visited)
            if div > 0:
                return div * table[i][n]
        return -1.0





equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

a = Solution()
print(a.calcEquation(equations, values, queries))





