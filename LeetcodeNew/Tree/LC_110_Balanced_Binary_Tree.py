"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.


104. Maximum Depth of Binary Tree
最基础的递归，先递归到底，当Leaf Node的左右两个Children Node都分别触及Base Case，
也就是None的时候，向上返回。然后之后对应当前node，左右两边的递归都操作结束以后，
返回的过程中对左右高度进行对比，取两个中间最大值，然后这里记住要加1，也就是当前的层数。
"""

"""
110. Balanced Binary Tree
有了104的基础，我们在延伸下看看110这道题，其实就是基于高度计算，然后判断一下。

但由于嵌套的Recursion调用，整体的时间复杂度是：O(nlogn) , 在每一层调用get_height的平均时间复杂度是O(N)，
然后基于二叉树的性质，调用了的高度是logn，所以n * logn 的时间复杂。

时间复杂度为什么是nlogn搞不清楚的看 时间复杂度图解


上面这种Brute Froce的方法，整棵树有很多冗余无意义的遍历，其实我们在处理完get_height这个高度的时候，
我们完全可以在检查每个节点高度并且返回的同时，记录左右差是否已经超过1，
只要有一个节点超过1，那么直接返回False即可，因此我们只需要在外围设立一个全球变量记录True和False，
在调用get_height的时候，内置代码里加入对左右高度的判定即可，代码如下

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        self.flag = True
        self.post(root)
        return self.flag

    def post(self, root):

        if not root:
            return True

        left = self.post(root.left)
        right = self.post(root.right)

        if abs(left - right) > 1:
            self.flag = False
            return -1

        return max(left, right) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root) != -1

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left == -1 or right == -1 or abs(right - left) > 1:
            return -1

        return max(left, right) + 1

