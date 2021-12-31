
import collections, heapq

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionBFS:
    def verticalTraversal(self, root):
        # similar to #314 Binary tree vertical order travel
        if not root:
            return []
        table = []

        queue = collections.deque()
        queue.append((root, 0, 0))

        while queue:
            cur, row, col = queue.popleft()
            table.append((col, row, cur.val))

            if cur.left:
                queue.append((cur.left, row + 1, col - 1))
            if cur.right:
                queue.append((cur.right, row + 1, col + 1))

        res = collections.defaultdict(list)

        for col, row, value in sorted(table):
            res[col].append(value)
        return res.values()



class SolutionDFS:
    def verticalTraversal(self, root):
        self.res = []
        self.dfs(root, 0, 0)
        res = collections.defaultdict(list)

        for col, depth, value in sorted(self.res):
            res[col].append(value)
        return res.values()

    def dfs(self, root, depth, col):
        if not root:
            return 0
        self.res.append((col, depth, root.val))
        left = self.dfs(root.left, depth + 1, col - 1)
        right = self.dfs(root.right, depth + 1, col + 1)


class Solution:
    def verticalTraversal(self, root: TreeNode):
        graph = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            nextLevel = []
            table = collections.defaultdict(list)
            for node, col in queue:
                table[col].append(node.val)
                if node.left:
                    nextLevel.append((node.left, col - 1))
                if node.right:
                    nextLevel.append((node.right, col+ 1))

            for i in table:
                graph[i].extend(sorted(table[i]))
            queue = nextLevel
        return [graph[i] for i in sorted(graph)]


class Solution2:
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

