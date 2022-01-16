class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
    def tree2str(self, root):
        if not root:
            return ""
        elif not root.left and not root.right:
            return str(root.val)
        elif not root.right:
            s = self.tree2str(root.left)
            return str(root.val) + "(" + s + ")"
        elif not root.left:
            s = self.tree2str(root.right)
            return str(root.val) + "()" + "(" + s + ")"
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        return str(root.val) + "(" + left + ")" + "(" + right + ")"




class SolutionRika:
    def tree2str(self, root):
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return ''
        val = str(root.val)
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if not root.left and not root.right:
            return val + ""

        elif not root.left:
            return val + '(' + ')' + '(' + right + ')'

        elif not root.right:
            return val + '(' + left + ')'

        else:
            return val + '(' + left + ')' + '(' + right + ')'



class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        if not t.left and not t.right:
            return str(t.val) + ""

        if not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"

        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")"


