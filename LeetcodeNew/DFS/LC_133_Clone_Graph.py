"""
Given a reference of a node in a connected undirected graph,
return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.



Example:



Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.

"""

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return None
        if node.label in self.visited:
            return self.visited[node.label]

        cloneNode = UndirectedGraphNode(node.label)
        self.visited[node.label] = cloneNode

        for n in node.neighbors:
            cloneNode.neighbors.append(self.cloneGraph(n))
        return cloneNode


#Normal thought
class Solution2:
    def cloneGraph(self, node):
        if not node:
            return None
        self.newNodeDict = {}
        return self.createNode(node)

    def createNode(self, oldNode):
        newNode = UndirectedGraphNode(oldNode.label)
        self.newNodeDict[newNode.label] = newNode

        for i in oldNode.neighbors:
            if i.label not in self.newNodeDict:
                self.createNode(i)  # recursively create nodes
            newNode.neighbors.append(self.newNodeDict[i.label])
        return newNode


class Solution3:
    def cloneGraph(self, node):
        return self.dfs(node, {})

    def dfs(self, node, dic):
        if not node: return None
        if node not in dic:
            dic[node] = UndirectedGraphNode(node.label)
            dic[node].neighbors += [self.dfs(n, dic) for n in node.neighbors]
        return dic[node]


