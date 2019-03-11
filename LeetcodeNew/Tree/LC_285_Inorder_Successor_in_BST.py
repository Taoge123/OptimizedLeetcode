
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


class Solution:
    def inorderSuccessor(self, root, p):
        self.res = None
        self.dfs(root, p)
        return self.res

    def dfs(self, root, p):
        if not root: return
        if p.val < root.val:
            self.res = root
            self.dfs(root.left, p)
        else:
            self.dfs(root.right, p)


class Solution2:
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

class Solution22:
    def inorderSuccessor(self, root, p):

        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right,p)
        return self.inorderSuccessor(root.left,p) or root

class Solution3:
    def inorderSuccessor(self, root, p):
        self.arr = []
        self.dfs(root)
        print(self.arr)
        if self.arr[-1] == p.val:
            return None
        else:
            for i, num in enumerate(self.arr):
                if num == p.val:
                    return self.arr[i+1]

    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)





