
"""

Given a binary search tree and a node in it,
find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.



Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


https://www.geeksforgeeks.org/?p=9999
https://stackoverflow.com/questions/5471731/in-order-successor-in-binary-search-tree
https://leetcode.com/problems/inorder-successor-in-bst/discuss/72652/For-those-who-is-not-so-clear-about-inorder-successors.


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

暴力解法
将整个树用中序遍历走一遍，并且将值储存在一个array里面。
之后如果要找的p.val是数组最后一个数，证明p没有继承者
不是最后一个数，则返回p.val在数组里的下一位

这里空间多用了N
只要比p.val大，该root就可能成为p的继承者，不断的递归缩小root的值，最后就会返回比p.val大的最小值。
如果没有比p.val大的值，直接返回None即可

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                res = root
                root = root.left
        return res


    def inorderSuccessor2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.dfs(root, p)
        return self.res

    def dfs(self, root, p):
        if not root:
            return
        if p.val < root.val:
            self.res = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)





