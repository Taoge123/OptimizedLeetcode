import collections

"""

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.



https://leetcode.com/problems/is-graph-bipartite/discuss/115493/Python-7-lines-DFS-graph-coloring-w-graph-and-Explanation
We'll keep an array (or hashmap) to lookup the color of each node: color[node].
The colors could be 0, 1, or uncolored (-1 or null).

We should be careful to consider disconnected components of the graph,
by searching each node. For each uncolored node,
we'll start the coloring process by doing a depth-first-search on that node.
Every neighbor gets colored the opposite color from the current node.
If we find a neighbor colored the same color as the current node,
then our coloring was impossible.

To perform the depth-first search, we use a stack.
For each uncolored neighbor in graph[node], we'll color it and add it to our stack,
which acts as a sort of todo list of nodes to visit next.
Our larger loop for start... ensures that we color every node.
"""

class Solution0:
    def isBipartite(self, graph):
        color = collections.defaultdict(lambda: -1)
        return all(self.dfs(graph, v, edges, 0, color) for v, edges in enumerate(graph) if color[v] == -1)

    def dfs(self, graph, v, edges, cur_color, color):
        if color[v] != -1: return color[v] == cur_color
        color[v] = cur_color
        return all(self.dfs(graph, e, graph[e], int(not cur_color), color) for e in edges)

class Solution1:
    def isBipartite(self, graph):
        color = {}
        def dfs(pos):
            for i in graph[pos]:
                if i in color:
                    if color[i] == color[pos]: return False
                else:
                    color[i] = 1 - color[pos]
                    if not dfs(i): return False
            return True
        for i in range(len(graph)):
            if i not in color: color[i] = 0
            if not dfs(i): return False
        return True



class Solution:
    def isBipartite(self, graph):
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True

















