"""

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

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


I use a additional function addLevel to record the level number of nodes,
then according to the level number, I can easily deal with the level order,
see the code for details
"""
# Definition for a  binary tree node
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



#Caikehe version solution
class Solution1:
    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        self.dfs(root, 0, res)
        return res


    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)



class Solution3:
    def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res

"""
We don't really need 2 stacks, all we need is

one array that keeps track of current level/depth we are at and
direction, either zig (from left-to-right) or zag (from right-to-left)
the only difference between zig and zag is that 
we reverse the collection/array of nodes at the level 
we wanna process if the direction is zag
"""



class SolutionTony:
    def zigzagLevelOrder(self, root: TreeNode):

        if not root:
            return []

        res = []
        queue = deque([root])
        reverse = False

        while queue:
            size, cur_level = len(queue), []

            for i in range(size):
                node = queue.popleft()
                # print(queue)
                if reverse:
                    # becuz we append from left to right, when reverse is True, we will need to insert 9, then insert 20 the the 0 position so 20 is at the left of 9
                    cur_level.insert(0, node.val)
                else:
                    cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)
            reverse = not reverse
        return res




