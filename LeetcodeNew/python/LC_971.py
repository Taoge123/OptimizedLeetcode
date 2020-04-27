"""
首先在递归函数中，我们对root节点进行判断，如果root不存在，这种情况不应该认为是题目输入错误，
而是应该认为已经遍历到最底部了，这个时候相当于root = [], voyage = []，所以返回true;
在先序遍历的时候，root节点是第一个要被遍历到的节点，如果不和voyage[0]相等，直接返回false;

这个题目的难点在于是否需要翻转一个节点的左右孩子。判断的方法其实是简单的：
如果voyage第二个元素等于root的左孩子，那么说明不用翻转，直接递归调用左右孩子；
否则如果voyage的第二个元素等于root的右孩子，那么还要注意一下，在左孩子存在的情况下，
我们需要翻转当前的节点左右孩子。

翻转是什么概念呢？这里并没有直接交换，而是把当前遍历到的位置使用遍历i保存起来，这样voyage[i]就表示当前遍历到哪个位置了;
所以dfs调用两个孩子的顺序很讲究，它体现了先序遍历先解决哪个树的问题，也就是完成了逻辑上的交换左右孩子。

"""
"""
思路分析：
假设当前结点为root，那么只要判断给定的数组是否满足以下两种形式即可

[root.val, root.left.val,….., root.right.val,…..]
[root.val, root.right.val,….., roo.left.val,……]
当然需要考虑到可能没有左孩子或右孩子的情况
虽然思路很简单，但单纯的用if else逻辑来写会让这道题的代码显得很杂乱，我们注意到树里面给定的所有值和voyage里面的所有值都是各不相同并且是属于1，N的。这一点能让我们使用一点技巧将代码变短。

在讲具体方法的时候，这里先思考一个问题，我们平常是如何判断一个数组是一棵树的先序遍历情况呢？
显然，如果我们新开一个数组来保存先序遍历的值，然后和给定数组进行比较是完全ok的，但这新建了O(n)的空间，我们是可以不用开新空间的（书本知识）

# 当然有迭代写法，这里写一个递归的方法
index = 0
def check(root, nums):
    if not root: return True
    if root.val != nums[index]:
        return False
    index += 1
    return check(root.left, nums) and check(root.right, nums)
    
    
这里我们也可以采用同样的思路，依次遍历结点，只有出现有左子树且左孩子的节点值不等于当前index指向的值，
才交换左右孩子，其余情况正常遍历即可。

"""

class Solution:
    def flipMatchVoyage(self, root, voyage):
        self.index = 0
        res = []
        if self.dfs(root, voyage, res):
            return res
        return [-1]

    def dfs(self, root, voyage, res):
        if not root:
            return True
        if root.val != voyage[self.index]:
            return False
        self.index += 1
        # 有左子树，且左子树的节点值不等于当前index指向的值
        if root.left and root.left.val != voyage[self.index]:
            if not root.right:
                return False
            res.append(root.val)
            # 此时先右再左
            return self.dfs(root.right, voyage, res) and self.dfs(root.left, voyage, res)
        return self.dfs(root.left, voyage, res) and self.dfs(root.right, voyage, res)


class Solution2:
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0
        self.dfs(root, voyage)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

    def dfs(self, node, voyage):
        if node:
            if node.val != voyage[self.i]:
                self.flipped = [-1]
                return
            self.i += 1

            if (self.i < len(voyage) and node.left and node.left.val != voyage[self.i]):
                self.flipped.append(node.val)
                self.dfs(node.right, voyage)
                self.dfs(node.left, voyage)
            else:
                self.dfs(node.left, voyage)
                self.dfs(node.right, voyage)






