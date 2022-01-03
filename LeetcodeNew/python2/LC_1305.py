import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        res = []
        q1, q2 = collections.deque(), collections.deque()
        self.inorder(root1, q1)
        self.inorder(root2, q2)
        print(q1, q2)
        while q1 or q2:
            if not q2:
                res.append(q1.popleft())
            elif not q1:
                res.append(q2.popleft())
            else:
                if q1[0] < q2[0]:
                    res.append(q1.popleft())
                else:
                    res.append(q2.popleft())
        return res

    def inorder(self, node, res):
        if not node:
            return
        self.inorder(node.left, res)
        res.append(node.val)
        self.inorder(node.right, res)



class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        res = []
        self.dfs(root1, res)
        self.dfs(root2, res)
        return sorted(res)

    def dfs(self, node, res):
        if not node:
            return
        self.dfs(node.left, res)
        res.append(node.val)
        self.dfs(node.right, res)


class SolutionTony:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        path1, path2 = [], []
        self.dfs(root1, path1)
        self.dfs(root2, path2)
        res = path1 + path2
        path1.extend(path2)
        return list(sorted(path1))

    def dfs(self, node, path):
        if not node:
            return

        path.append(node.val)
        self.dfs(node.left, path)
        self.dfs(node.right, path)

