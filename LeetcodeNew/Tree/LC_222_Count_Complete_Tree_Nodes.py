

"""

https://www.cnblogs.com/yrbbest/p/4993469.html



Input:
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

compare the depth between left sub tree and right sub tree.
A, If it is equal, it means the left sub tree is a full binary tree
B, It it is not , it means the right sub tree is a full binary tree
Nice solution, add a word, comparing the depth between left sub tree and right sub tree,
If it is equal, it means the left sub tree is a perfect binary tree, not only a full binary tree.
If it is not , it means the right sub tree is a perfect binary tree.


class Solution:
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
O(log(n) ^ 2):
The idea is compare the left subtree depth with the right subtree depth.
If they are equal, we have a full tree, thus we return 2^height - 1.
If they aren't equal, we do recursive call for the root.left subtree and the root.right subtree.
Note that everytime we do recursive call for the root.left subtree or the root.right subtree,
one of them must be a full tree due to the condition of the problem.

求完全二叉树的节点数目。注意完全二叉树和满二叉树Full Binary Tree的唯一区别是，完全二叉树最后一层的节点不满，而且假设最后一层有节点，都是从左边开始。 这样我们可以利用这个性质得到下面的结论：

假如左子树高度等于右子树高度，则右子树为完全二叉树，左子树为满二叉树。
假如高度不等，则左字数为完全二叉树，右子树为满二叉树。
求高度的时候只往左子树来找。
可以使用上面的结论得出本题的解法：

先构造一个getHeight方法， 用来求出二叉树的高度。这里我们只用求从根节点到最左端节点的长度。

求出根节点左子树高度leftHeight和根节点右子树高度rightHeight

假如两者相等，那么说明左子树是满二叉树，而右子树可能是完全二叉树。
– 我们可以返回 2 ^ leftHeight - 1 + 1 + countNodes(root.right)
– 这里+1是因为把根节点也算进去，化简一下就是 1 << leftHeight + countNodes(root.right)，返回结果
否则两者不等，说明左子树是完全二叉树，右子树是满二叉树
– 我们可以返回 2^ rightHeight - 1 + 1 + countNodeS(root.left)
– 化简以后得到 1 << rightHeight + countNodes(root.left)，返回结果
---------------------
作者：负雪明烛
来源：CSDN
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80781666
版权声明：本文为博主原创文章，转载请附上博文链接！


这道题有好些方法可以做。Stefan Pochmann的帖子里就写了很多。

下面我们介绍最基本最Naive的一种。

完全二叉树Complete Binary Tree是指除了最后一行以外，每一行都是满的。如果最后一行存在节点，那么这些节点满足从左到右排列。

满二叉树Full Binary Tree是指所有的节点的子节点要么为空要么有两个子节点。而满二叉树的节点总数是 2 ^ h - 1，这里h是满二叉树的高度。

知道了以上性质，我们就可以进行解题
    先构造一个getHeight方法， 用来求出二叉树的高度。这里我们只用求从根节点到最左端节点的长度。
    求出根节点左子树高度leftHeight和根节点右子树高度rightHeight
        假如两者相等，那么说明左子树是满二叉树，而右子树可能是完全二叉树。
            我们可以返回  2 ^ leftHeight - 1 + 1  + countNodes(root.right)
            这里+1是因为把根节点也算进去，化简一下就是 1 << leftHeight + countNodes(root.right)，返回结果

            否则两者不等，说明左子树是完全二叉树，右子树是满二叉树
                我们可以返回 2^ rightHeight - 1 + 1 + countNodeS(root.left)
                化简以后得到 1 << rightHeight + countNodes(root.left)，返回结果
    这里getHeight()方法的时间复杂度是O(logn)， countNodes()方法的时间复杂度也是O(logn)，所以总的时间复杂度是O(logn * logn)

    空间复杂度是递归栈的深度，是O(logn)
"""

class Solution0:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        nodes = 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        if left_height == right_height:
            nodes = 2 ** left_height + self.countNodes(root.right)
        else:
            nodes = 2 ** right_height + self.countNodes(root.left)
        return nodes


    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

class Solution2:
    def countNodes(self, root):
        leftdepth = self.getdepth(root, True)
        rightdepth = self.getdepth(root, False)

        if leftdepth == rightdepth:
            return 2 ** leftdepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getdepth(self, root, isLeft):
        if root is None:
            return 0
        if isLeft:
            return 1 + self.getdepth(root.left, isLeft)
        else:
            return 1 + self.getdepth(root.right, isLeft)


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

class SolutionCaikehe:
    def countNodes(self, root):
        if not root:
            return 0
        h1 = self.height(root.left)
        h2 = self.height(root.right)
        if h1 > h2:  # right child is full
            return self.countNodes(root.left) + 2 ** h2
        else:  # left child is full
            return self.countNodes(root.right) + 2 ** h1

    # the height of the left-most leaf node
    def height1(self, root):
        h = 0
        while root:
            h += 1
            root = root.left
        return h

    def height(self, root):
        if not root:
            return 0
        return self.height(root.left) + 1









