
"""

https://leetcode.com/problems/complete-binary-tree-inserter/solution/


A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree
with value node.val = v so that the tree remains complete,
and returns the value of the parent of the inserted TreeNode;

CBTInserter.get_root() will return the head node of the tree.


Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]


"""


"""
Store tree nodes to a list self.tree in bfs order.
Node tree[i] has left child tree[2 * i + 1] and tree[2 * i + 2]

So when insert the Nth node (0-indexed), we push it into the list.
we can find its parent tree[(N - 1) / 2] directly.
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionLee:
    def __init__(self, root):
        self.tree = [root]
        for i in self.tree:
            if i.left:
                self.tree.append(i.left)
            if i.right:
                self.tree.append(i.right)

    def insert(self, v):
        N = len(self.tree)
        self.tree.append(TreeNode(v))
        if N % 2:
            self.tree[(N - 1) / 2].left = self.tree[-1]
        else:
            self.tree[(N - 1) / 2].right = self.tree[-1]

        return self.tree[(N - 1) / 2].val

    def get_root(self):
        return self.tree[0]

"""
Approach 1: Deque
Intuition

Consider all the nodes numbered first by level and then left to right. 
Call this the "number order" of the nodes.

At each insertion step, we want to insert into the node with the lowest number (that still has 0 or 1 children).

By maintaining a deque (double ended queue) of these nodes in number order, we can solve the problem. 
After inserting a node, that node now has the highest number and no children, 
so it goes at the end of the deque. To get the node with the lowest number, 
we pop from the beginning of the deque.

Algorithm

First, perform a breadth-first search to populate the deque with nodes that have 0 or 1 children, in number order.

Now when inserting a node, the parent is the first element of deque, and we add this new node to our deque.


"""


class CBTInserter:
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root



"""
题目大意
编写一个完全二叉树的数据结构，需要完成构建、插入、获取root三个函数。函数的参数和返回值如题。

解题方法
完全二叉树是每一层都满的，因此找出要插入节点的父亲节点是很简单的。
如果用数组tree保存着所有节点的层次遍历，那么新节点的父亲节点就是tree[(N-1)/2]，N是未插入该节点前的树的元素个数。

构建树的时候使用层次遍历，也就是BFS把所有的节点放入到tree里。
插入的时候直接计算出新节点的父亲节点。获取root就是数组中的第0个节点。

时间复杂度是O(N)，空间复杂度是O(N)。
--------------------- 
作者：负雪明烛 
来源：CSDN 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/82958284 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""


class CBTInserter2:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.tree = list()
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            self.tree.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        _len = len(self.tree)
        father = self.tree[(_len - 1) / 2]
        node = TreeNode(v)
        if not father.left:
            father.left = node
        else:
            father.right = node
        self.tree.append(node)
        return father.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.tree[0]




