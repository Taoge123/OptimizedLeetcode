
"""
https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion




Equations are given in the format A / B = k,
where A and B are variables represented as strings,
and k is a real number (floating point number).
Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

"""

"""
For example:
Given:
a/b = 2.0, b/c = 3.0
We can build a directed graph:
a -- 2.0 --> b -- 3.0 --> c
If we were asked to find a/c, we have:
a/c = a/b * b/c = 2.0 * 3.0
In the graph, it is the product of costs of edges.

Do notice that, 2 edges need to added into the graph with one given equation,
because with a/b we also get result of b/a, which is the reciprocal of a/b.

so the previous example also gives edges:
c -- 0.333 --> b -- 0.5 --> a

Now we know how to model this problem, what we need to do is simply build the
graph with given equations, and traverse the graph, either DFS or BFS, to find a path
for a given query, and the result is the product of costs of edges on the path.

One optimization, which is not implemented in the code, is to "compress" paths for
past queries, which will make future searches faster. This is the same idea used in
compressing paths in union find set. So after a query is conducted and a result is found,
we add two edges for this query if these edges are not already in the graph.

Given the number of variables N, and number of equations E,
building the graph takes O(E), each query takes O(N), space for graph takes O(E)

I think if we start to compress paths, the graph will grow to O(N^2), and we
can optimize the query to O(1), please correct me if I'm wrong.

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




