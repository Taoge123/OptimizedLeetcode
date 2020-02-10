"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
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

            res.append(cur_level)
            reverse = not reverse
        return res







