import collections

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.graph = collections.defaultdict(list)
        return self.dfs(node)

    def dfs(self, node):

        if self.graph[node]:
            return self.graph[node]
        newNode = Node(node.val, [])
        self.graph[node] = newNode
        for nei in node.neighbors:
            newNode.neighbors.append(self.dfs(nei))
        return newNode



