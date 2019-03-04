"""
104. Maximum Depth of Binary Tree
最基础的递归，先递归到底，当Leaf Node的左右两个Children Node都分别触及Base Case，
也就是None的时候，向上返回。然后之后对应当前node，左右两边的递归都操作结束以后，
返回的过程中对左右高度进行对比，取两个中间最大值，然后这里记住要加1，也就是当前的层数。
"""

class Solution:
    def maxDepth_gd(self, root):
        '''bugfree'''
        if not root: return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1



"""
110. Balanced Binary Tree
有了104的基础，我们在延伸下看看110这道题，其实就是基于高度计算，然后判断一下。

但由于嵌套的Recursion调用，整体的时间复杂度是：O(nlogn) , 在每一层调用get_height的平均时间复杂度是O(N)，
然后基于二叉树的性质，调用了的高度是logn，所以n * logn 的时间复杂。

时间复杂度为什么是nlogn搞不清楚的看 时间复杂度图解"""


class Solution2:
    def isBalanced(self, root):
        if not root: return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1


"""
上面这种Brute Froce的方法，整棵树有很多冗余无意义的遍历，其实我们在处理完get_height这个高度的时候，
我们完全可以在检查每个节点高度并且返回的同时，记录左右差是否已经超过1，
只要有一个节点超过1，那么直接返回False即可，因此我们只需要在外围设立一个全球变量记录True和False，
在调用get_height的时候，内置代码里加入对左右高度的判定即可，代码如下

"""

class SolutionBetter:
    def isBalanced(self, root):
        if not root: return True
        self.flag = False
        self.getHeight(root)
        return not self.flag

    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)

        if abs(left - right) > 1 or self.flag:
            self.flag = True
        return max(left, right) + 1


class SolutionVeryGood:
    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1

    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1: return -1
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1


