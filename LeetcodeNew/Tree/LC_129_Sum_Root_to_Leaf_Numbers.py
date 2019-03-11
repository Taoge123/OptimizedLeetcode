"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


"""
import collections


class Solution1:
    def sumNumbers(self, root):
        return self.sum_numbers_help(root, 0)

    def sum_numbers_help(self, root, curr):
        if not root:
            return 0

        curr = 10 * curr + root.val
        if not root.left and not root.right:
            return curr
        return self.sum_numbers_help(root.left, curr) + self.sum_numbers_help(root.right, curr)

class Solution:
    # dfs + stack
    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res

    # bfs + queue
    def sumNumbers2(self, root):
        if not root:
            return 0
        queue, res = collections.deque([(root, root.val)]), 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    queue.append((node.left, value * 10 + node.left.val))
                if node.right:
                    queue.append((node.right, value * 10 + node.right.val))
        return res

    # recursively
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, value):
        if root:
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.left, value * 10 + root.val)
            # if not root.left and not root.right:
            #    self.res += value*10 + root.val
            self.dfs(root.right, value * 10 + root.val)
            if not root.left and not root.right:
                self.res += value * 10 + root.val



