"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reverseOddLevels(self, root):

        if not root:
            return []

        res = []
        queue = collections.deque([root])
        reverse = False

        while queue:
            size, cur_level = len(queue), collections.deque()

            for i in range(size):
                node = queue.popleft()
                # print(queue)
                if reverse:
                    # becuz we append from left to right, when reverse is True, we will need to insert 9, then insert 20 the the 0 position so 20 is at the left of 9
                    cur_level.appendleft(node.val)
                else:
                    cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.extend(cur_level)
            reverse = not reverse
        # print(res)

        def insertLevelOrder(arr, i, n):
            root = None
            # Base case for recursion
            if i < n:
                root = TreeNode(arr[i])

                # insert left child
                root.left = insertLevelOrder(arr, 2 * i + 1, n)

                # insert right child
                root.right = insertLevelOrder(arr, 2 * i + 2, n)

            return root

        def inOrder(root):
            if root != None:
                inOrder(root.left)
                print(root.val, end=" ")
                inOrder(root.right)

        n = len(res)
        root = None
        root = insertLevelOrder(res, 0, n)
        inOrder(root)
        return root


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(1)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(1)


a = Solution()
print(a.reverseOddLevels(root))







