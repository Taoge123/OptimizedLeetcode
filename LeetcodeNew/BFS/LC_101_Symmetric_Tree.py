
"""
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

这道题具体的Recursion Rule不是传递Root本身，而是对两个子孩子的比较，
所以Helper的参数定义为root.left 和 root.right. 然后根据题目的特性，
在每一层往下传递之前要做比较，所以是preorder的写法，先写比较的几种格式，然后在做递归。
递归向上返回的参数是一个Boolean。

时间复杂度 : O(N)
空间复杂度 : O(N) or O(Height)

"""
import collections

class SolutionBFS:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True

        dq = collections.deque([(root.left,root.right)])
        while dq:
            node1, node2 = dq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            # node1.left and node2.right are symmetric nodes in structure
            # node1.right and node2.left are symmetric nodes in structure
            dq.append((node1.left,node2.right))
            dq.append((node1.right,node2.left))
        return True


class SolutionDFS:
    def isSymmetric(self, root):
        if not root: return True
        return self.dfs_helper(root.left, root.right)

    def dfs_helper(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        if n1.val != n2.val: return False
        left = self.dfs_helper(n1.left, n2.right)
        right = self.dfs_helper(n1.right, n2.left)
        return left and right

class SolutionGoogle:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if not root:
            return True

        return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, node1, node2):
        if node1 and node2:
            return node1.val == node2.val and self.isSymmetricTree(node1.left, node2.right) and self.isSymmetricTree(node1.right, node2.left)
        else:
            return node1 == node2


