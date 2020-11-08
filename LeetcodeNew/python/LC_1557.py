"""
Intuition
Just return the nodes with no in-degres.


Explanation
Quick prove:

Necesssary condition: All nodes with no in-degree must in the final result,
because they can not be reached from
All other nodes can be reached from any other nodes.

Sufficient condition: All other nodes can be reached from some other nodes.


Complexity
Time O(E)
Space O(N)
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        res = []
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1

        for i in range(n):
            if indegree[i] == 0:
                res.append(i)

        return res




class Solution2:
    def findSmallestSetOfVertices(self, n: int, edges):
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        return [i for i in range(n) if indegree[i] == 0]






