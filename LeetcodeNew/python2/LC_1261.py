
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root):
        self.visited = set()
        self.dfs(root, 0)

    def dfs(self, node, val):
        if not node:
            return

        node.val = val
        self.visited.add(val)
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.visited

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

a = FindElements(root)
node = TreeNode(4)