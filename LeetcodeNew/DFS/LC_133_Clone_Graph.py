

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


