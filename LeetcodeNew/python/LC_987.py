
import collections

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





