"""

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



跟【LeetCode】116. Populating Next Right Pointers in Each Node 解题报告（Python）很像，
只不过这个题没有完全二叉树的条件，因此我们需要额外的条件。

下面这个做法没满足题目中的常数空间的要求，不过是个非递归的好做法，对完全二叉树也完全试用。
做法就是把每层的节点放到一个队列里，把队列的每个元素进行弹出的时候，如果它不是该层的最后一个元素，
那么把它指向队列中的后面的元素（不把后面的这个弹出）

Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

---------------------
"""

class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue, nextLevel = collections.deque([root]), collections.deque()

        while queue:
            node = queue.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if queue:
                node.next = queue[0]
            if not queue:
                queue, nextLevel = nextLevel, queue

        return root


    def connect2(self, root: 'Node') -> 'Node':
        queue, level, curr = root, None, None

        while queue:
            if queue.left:
                if not level:
                    level = curr = queue.left
                else:
                    curr.next = queue.left
                    curr = curr.next
            if queue.right:
                if not level:
                    level = curr = queue.right
                else:
                    curr.next = queue.right
                    curr = curr.next
            queue = queue.next
            if not queue and level:
                queue, level, curr = level, None, None
        return root






