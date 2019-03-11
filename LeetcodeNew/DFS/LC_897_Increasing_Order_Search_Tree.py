"""

Given a tree, rearrange the tree in in-order
so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9


Similar in geeksforgeek
https://www.geeksforgeeks.org/modify-binary-tree-get-preorder-traversal-using-right-pointers/

I didn't use this condition of BST, and just inorder output the whole tree.

Straigh forward idea:
res = inorder(root.left) + root + inorder(root.right)

Several tips here:

I pass a tail part to the function, so it can link it to the last node.
This operation takes O(1), instead of O(N).
Otherwise the whole time complexity will be O(N^2).

Also, remember to set root.left = null.
Otherwise it will be TLE for Leetcode to traverse your tree.

Should arrange the old tree, not create a new tree.
The judgement won't take it as wrong answer, but it is.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SoilutionBest:
    def increasingBST(self, root, tail = None):
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res


class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right



class Solution2:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                #relink during traversal
                node.left = None
                self.cur.right = node
                self.cur = node

                inorder(node.right)

        ans = self.cur = TreeNode(None)

        inorder(root)
        return ans.right

class Solution3:
    def increasingBST(self, root, tail=None):
        if root is None:
            return tail
        x = TreeNode(root.val)
        x.right = self.increasingBST(root.right, tail)
        return self.increasingBST(root.left, x)

