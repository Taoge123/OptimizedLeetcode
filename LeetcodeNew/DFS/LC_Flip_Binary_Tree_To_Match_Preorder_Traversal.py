"""
Explanation:
Global integer i indicates next index in voyage v.
If current node == null, it's fine, we return true
If current node.val != v[i], doesn't match wanted value, return false
If left child exist but don't have wanted value, flip it with right child.

https://buptwc.com/2019/01/09/Leetcode-971-Flip-Binary-Tree-to-Match-Preorder-Traversal/

思路分析：
假设当前结点为root，那么只要判断给定的数组是否满足以下两种形式即可

[root.val, root.left.val,….., root.right.val,…..]
[root.val, root.right.val,….., roo.left.val,……]
当然需要考虑到可能没有左孩子或右孩子的情况
虽然思路很简单，但单纯的用if else逻辑来写会让这道题的代码显得很杂乱，
我们注意到树里面给定的所有值和voyage里面的所有值都是各不相同并且是属于1，N的。这一点能让我们使用一点技巧将代码变短。

在讲具体方法的时候，这里先思考一个问题，我们平常是如何判断一个数组是一棵树的先序遍历情况呢？
显然，如果我们新开一个数组来保存先序遍历的值，然后和给定数组进行比较是完全ok的，但这新建了O(n)的空间，
我们是可以不用开新空间的（书本知识）


"""

'''

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

'''

class SolutionGiven:
    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node:
                if node.val != voyage[self.i]:
                    self.flipped = [-1]
                    return
                self.i += 1

                if (self.i < len(voyage) and
                        node.left and node.left.val != voyage[self.i]):
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)

        dfs(root)
        if self.flipped and self.flipped[0] == -1:
            self.flipped = [-1]
        return self.flipped

class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0
        def dfs(root):
            if not root: return True
            if root.val != voyage[self.i]: return False
            self.i += 1
            if root.left and root.left.val != voyage[self.i]:
                res.append(root.val)
                root.left ,root.right = root.right, root.left
            return dfs(root.left) and dfs(root.right)
        return res if dfs(root) else [-1]


class Solution2:
    def flipMatchVoyage(self, root, voyage):
        def dfs(root):
            if not root:
                return True
            if root.val != voyage[self.next]:
                return False

            self.next += 1
            if root.left and root.right and root.left.val != voyage[self.next] and root.right.val == voyage[self.next]:
                res.append(root.val)
                root.left, root.right = root.right, root.left

            return dfs(root.left) and dfs(root.right)

        res = []
        self.next = 0
        if dfs(root):
            return res
        else:
            return [-1]


class Solution2:
    def flipMatchVoyage(self, root, voyage):
        flip = []

        def traverse(node, route):
            if not node:
                return
            if node.val == route[0]:
                route.pop(0)
            if node.left and node.right and node.right.val == route[0]:
                flip.append(node.val)
                node.left, node.right = node.right, node.left
            traverse(node.left, route)
            traverse(node.right, route)

        traverse(root, voyage)
        return flip if not voyage else [-1]



class Solution3:
    def flipMatchVoyage(self, root, voyage):
        self.index = 0
        res = []
        def dfs(root):
            if not root: return True
            if root.val != voyage[self.index]: return False
            self.index += 1
            # 有左子树，且左子树的节点值不等于当前index指向的值
            if root.left and root.left.val != voyage[self.index]:
                if not root.right: return False
                res.append(root.val)
                # 此时先右再左
                return dfs(root.right) and dfs(root.left)
            return dfs(root.left) and dfs(root.right)

        if dfs(root):
            return res
        return [-1]

