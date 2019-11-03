

"""
https://leetcode.com/problems/convert-bst-to-greater-tree/solution/

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13


"""

"""
ntuition

There is a clever way to perform an in-order traversal using only linear time 
and constant space, first described by J. H. Morris in his 1979 paper 
"Traversing Binary Trees Simply and Cheaply". 
In general, the recursive and iterative stack methods sacrifice linear space 
for the ability to return to a node after visiting its left subtree. 
The Morris traversal instead exploits the unused null pointer(s) 
of the tree's leaves to create a temporary link out of the left subtree, 
allowing the traversal to be performed using only constant additional memory. 
To apply it to this problem, we can simply swap all "left" and "right" references, 
which will reverse the traversal.

Algorithm

First, we initialize node, which points to the root. 
Then, until node points to null (specifically, 
the left null of the tree's minimum-value node), we repeat the following. 
First, consider whether the current node has a right subtree. 
If it does not have a right subtree, then there is no unvisited node with a greater value, 
so we can visit this node and move into the left subtree. 
If it does have a right subtree, 
then there is at least one unvisited node with a greater value, 
and thus we must visit first go to the right subtree. 
To do so, we obtain a reference to the in-order successor 
(the smallest-value node larger than the current) via our helper function getSuccessor.
This successor node is the node that must be visited immediately before the current node, 
so it by definition has a null left pointer (otherwise it would not be the successor). 
Therefore, when we first find a node's successor, 
we temporarily link it (via its left pointer) to the node and proceed to the node's right subtree. 
Then, when we finish visiting the right subtree, the leftmost left pointer 
in it will be our temporary link that we can use to escape the subtree. 
After following this link, we have returned to the original node that we previously passed through, 
but did not visit. This time, 
when we find that the successor's left pointer loops back to the current node, 
we know that we have visited the entire right subtree, 
so we can now erase the temporary link and move into the left subtree.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return

        self.helper(root.right)
        root.val += self.sum
        self.sum = root.val
        self.helper(root.left)



