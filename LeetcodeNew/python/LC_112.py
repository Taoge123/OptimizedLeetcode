"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) \
               or self.hasPathSum(root.right, sum - root.val)

class Solution2:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()
            print(node.val)
            if not node.left and not node.right:
                if node.val == sum:
                    return True

            if node.left:
                node.left.val += node.val
                stack.append(node.left)

            if node.right:
                node.right.val += node.val
                stack.append(node.right)

        return False


class Solution3:
    def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


class Solution4:
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum)

    def dfs(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and sum - root.val == 0:
            return True
        left = self.dfs(root.left, sum - root.val)
        right = self.dfs(root.right, sum - root.val)
        return left or right



