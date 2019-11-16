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







