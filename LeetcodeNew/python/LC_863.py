
"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""




"""
A recursive dfs funciton connect help to build up a map conn.
The key of map is node's val and the value of map is node's connected nodes' vals.
Then we do N times bfs search loop to find all nodes of distance K

"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def distanceK(self, root, target, K):
        graph = collections.defaultdict(list)
        self.connect(graph, None, root)
        queue = [target.val]
        visited = set(queue)
        for i in range(K):
            # queue = [y for x in queue for y in graph[x] if y not in visited]
            temp = []
            while queue:
                x = queue.pop(0)
                for y in graph[x]:
                    if y not in visited:
                        temp.append(y)

            queue = temp
            visited |= set(queue)
        return queue

    def connect(self, graph, parent, child):
        if parent and child:
            graph[parent.val].append(child.val)
            graph[child.val].append(parent.val)
        if child.left:
            self.connect(graph, child, child.left)
        if child.right:
            self.connect(graph, child, child.right)


class Solution2:
    def distanceK(self, root, target, K):

        self.dfs(root, None)
        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, dist in queue]
            node, dist = queue.popleft()
            for nei in (node.left, node.right, node.parent):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist + 1))

        return []

    def dfs(self, node, parent):
        if node:
            node.parent = parent
            self.dfs(node.left, node)
            self.dfs(node.right, node)






