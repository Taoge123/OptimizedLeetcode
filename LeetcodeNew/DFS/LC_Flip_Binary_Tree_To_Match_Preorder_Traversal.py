"""
Explanation:
Global integer i indicates next index in voyage v.
If current node == null, it's fine, we return true
If current node.val != v[i], doesn't match wanted value, return false
If left child exist but don't have wanted value, flip it with right child.


"""

class SolutionGiven:
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0
        def dfs(root):
            if not root: return True
            if root.val != voyage[self.i]: return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left ,root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]


class Solution2:
    def flipMatchVoyage(self, root, voyage):
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.next]:
                return False

            self.next += 1
            if root.left and root.right and root.left.val != voyage[self.next] and root.right.val == voyage[self.next]:
                res.append(root.val)
                root.left, root.right = root.right, root.left

            return dfs(root.left) and dfs(root.right)

        res = []
        self.next = 0
        if dfs(root):
            return res
        else:
            return [-1]

