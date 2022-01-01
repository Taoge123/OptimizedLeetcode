
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionTony:
    def isCousins(self, root, x, y):
        self.x, self.y = x, y
        self.x_parent, self.x_level = None, 0
        self.y_parent, self.y_level = None, 0
        self.dfs(root, 0, None, x)
        self.dfs(root, 0, None, y)
        return self.x_level == self.y_level and self.x_parent != self.y_parent


    def dfs(self, node, level, prev, target):
        if not node:
            return 0, None

        if node.val == self.x:
            self.x_parent, self.x_level = prev, level
        if node.val == self.y:
            self.y_parent, self.y_level = prev, level
        self.dfs(node.left, level + 1, node, target)
        self.dfs(node.right, level + 1, node, target)



class SolutionLocal:
    def isCousins(self, root, x, y):

        px, dx = self.dfs(root, None, 0, x)
        py, dy = self.dfs(root, None, 0, y)

        return dx == dy and px != py

    def dfs(self, node, parent, depth, target):
        if not node:
            return
        if node.val == target:
            return parent, depth
        return self.dfs(node.left, node, depth + 1, target) or self.dfs(node.right, node, depth + 1, target)


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

a = SolutionLocal()
x, y = a.dfs(root, None, 0, 3)
print(x.val, y)