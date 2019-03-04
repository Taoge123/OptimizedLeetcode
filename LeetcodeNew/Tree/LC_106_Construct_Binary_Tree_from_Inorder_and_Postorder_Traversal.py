
"""
That's because inorder traversal goes 'Left-Parent-Right'
and postorder traversal goes 'Left-Right-Parent'.
And, postorder.pop() keeps picking the right-most element of the list,
that means it should go 'Parent-(one of parents of) Right (subtree) - Left'.
So, switching the order doesn't work.

Optimized Solution
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/221681/Don't-use-top-voted-Python-solution-for-interview-here-is-why.


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if inorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.right = self.buildTree(inorder[ind + 1:], postorder)
            root.left = self.buildTree(inorder[:ind], postorder)
            return root



class Solution2:
    def buildTree(self, inorder, postorder):
        map_inorder = {}
        for i, val in enumerate(inorder): map_inorder[val] = i
        def recur(low, high):
            if low > high: return None
            x = TreeNode(postorder.pop())
            mid = map_inorder[x.val]
            x.right = recur(mid+1, high)
            x.left = recur(low, mid-1)
            return x
        return recur(0, len(inorder)-1)

"""
Same ideas as in Construct Binary Tree from Preorder and Inorder Traversal: 

use inddict, a dictionary of val:index in inorder, to reduce the runtime. 

Geting an item in a dictionary is O(1), but list.index() is O(n) 
use index pointers Lin, Rin for inorder instead of slicing
"""

class Solution3:
    def buildTree(self, inorder, postorder):
        def helper(Lin, Rin):
            if Lin < Rin:
                root = TreeNode(postorder.pop(-1))
                rootind = inddict[root.val]
                root.right = helper(rootind + 1, Rin)
                root.left = helper(Lin, rootind)
                return root

        inddict = {val: i for i, val in enumerate(inorder)}
        return helper(0, len(inorder))


