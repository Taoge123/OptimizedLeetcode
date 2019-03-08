

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

class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root


class Solution2:
    def convertBST(self, root):
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root


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

class Solution3:
    def convertBST(self, root):
        # Get the node with the smallest value greater than this one.
        def get_successor(node):
            succ = node.right
            while succ.left is not None and succ.left is not node:
                succ = succ.left
            return succ

        total = 0
        node = root
        while node is not None:
            # If there is no right subtree, then we can visit this node and
            # continue traversing left.
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            # If there is a right subtree, then there is a node that has a
            # greater value than the current one. therefore, we must traverse
            # that node first.
            else:
                succ = get_successor(node)
                # If there is no left subtree (or right subtree, because we are
                # in this branch of control flow), make a temporary connection
                # back to the current node.
                if succ.left is None:
                    succ.left = node
                    node = node.right
                # If there is a left subtree, it is a link that we created on
                # a previous pass, so we should unlink it and visit this node.
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root



