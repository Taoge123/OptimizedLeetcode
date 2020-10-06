"""
863
"""



import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        self.dfs(graph, root, None)
        queue = collections.deque(node for node in graph if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

    def dfs(self, graph, node, parent):
        if node:
            graph[node].append(parent)
            graph[parent].append(node)
            self.dfs(graph, node.left, node)
            self.dfs(graph, node.right, node)





class Solution2:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:

        table = {}
        target = self.helper(root, k, table)
        queue = collections.deque()
        visited = set()
        queue.append(target)
        visited.add(target)

        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                return node.val

            if node.left and node.left not in visited:
                queue.append(node.left)
                visited.add(node.left)

            if node.right and node.right not in visited:
                queue.append(node.right)
                visited.add(node.right)

            if node in table and table[node] not in visited:
                queue.append(table[node])
                visited.add(table[node])

    def helper(self, root, k, table):
        if root.val == k:
            return root
        if root.left:
            table[root.left] = root
            left = self.helper(root.left, k, table)
            if left:
                return left

        if root.right:
            table[root.right] = root
            right = self.helper(root.right, k, table)
            if right:
                return right

        return None



