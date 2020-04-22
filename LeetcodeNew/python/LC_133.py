"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.


Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.


"""


import collections

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
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



class Solution2:
    def cloneGraph1(self, node):
        if not node:
            return
        nodeCopy = Node(node.label)
        table = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in table:  # neighbor is not visited
                    neighborCopy = Node(neighbor.label)
                    table[neighbor] = neighborCopy
                    table[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    table[node].neighbors.append(table[neighbor])
        return nodeCopy

