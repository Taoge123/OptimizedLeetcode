
import collections, heapq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode):
        graph = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            nextLevel = []
            table = collections.defaultdict(list)
            for node, step in queue:
                table[step].append(node.val)
                if node.left:
                    nextLevel.append((node.left, step - 1))
                if node.right:
                    nextLevel.append((node.right, step + 1))

            for i in table:
                graph[i].extend(sorted(table[i]))
            queue = nextLevel
        return [graph[i] for i in sorted(graph)]


class Solution:
    def verticalTraversal(self, root: TreeNode):
        graph = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            nextLevel = []
            table = collections.defaultdict(list)
            for node, step in queue:
                heapq.heappush(table[step], node.val)
                if node.left:
                    nextLevel.append((node.left, step - 1))
                if node.right:
                    nextLevel.append((node.right, step + 1))

            for i in table:
                graph[i].extend(heapq.nsmallest(len(table[i]), table[i]))
            queue = nextLevel

        return [graph[i] for i in sorted(graph)]


"""
defaultdict(<class 'list'>, {0: [1, 5, 6], -1: [2], 1: [3], -2: [4], 2: [7]})
"""
"""
           1
       2       3
     4    5 6   7
    
"""

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


a = Solution()
print(a.verticalTraversal(root))

