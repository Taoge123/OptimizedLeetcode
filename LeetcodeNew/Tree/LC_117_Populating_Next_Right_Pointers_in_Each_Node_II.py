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
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/79560379
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

import collections

def connect(self, root):
    if not root:
        return
    # connect nodes level by level,
    # similar to level order traversal
    queue = collections.deque([root])
    nextLevel = collections.deque([])
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



class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)






