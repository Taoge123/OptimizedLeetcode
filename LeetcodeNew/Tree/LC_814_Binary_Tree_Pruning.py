

"""
We are given the head node root of a binary tree,
where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]



Note:

The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

"""
"""
Algorithm

We'll use a function containsOne(node) that does two things: 
it tells us whether the subtree at this node contains a 1, 
and it also prunes all subtrees not containing 1.

If for example, node.left does not contain a one, 
then we should prune it via node.left = null.

Also, the parent needs to be checked. If for example the tree is a single node 0, 
the answer is an empty tree.
"""

class Solution:
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and not root.val: return None
        return root


"""
Of course. We should take care about free memory.
But in my opinion, we can delete a node only if we know it was allocated with new, right?
So in my cpp, I didn't do this part.
My rule is that, If you don't new it, don't delete it.
"""
class SolutionLee:
    def pruneTree(self, root):
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None


class Solution2:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return None if not root.val and not root.left and not root.right else root



class Solution3:
    def pruneTree(self, root):
        if not root: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val:
            return root
        else:
            return root if root.left or root.right else None


