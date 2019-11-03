"""
You are given a perfect binary tree where all leaves are on the same level,
and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

"""

import collections


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return

        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right

                if node.next:
                    node.right.next = node.next.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


    def connect2(self, root: 'Node') -> 'Node':
        if not root:
            return

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left

                stack.append(node.left)
                stack.append(node.right)

        return root







