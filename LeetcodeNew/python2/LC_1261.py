
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.visited = set()
        self.dfs(root, 0)

    def dfs(self, node, v):
        if not node:
            return
        node.val = v
        self.visited.add(v)
        self.dfs(node.left, 2 * v + 1)
        self.dfs(node.right, 2 * v + 2)


    def find(self, target: int) -> bool:
        return target in self.visited



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
