
"""
Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1


If we had each node's subtree sum, our answer would look like this psuedocode:
for each node: ans += abs(node.left.subtreesum - node.right.subtreesum).
Let _sum(node) be the node's subtree sum.
We can find it by adding the subtree sum of the left child, plus the subtree sum of the right child,
plus the node's value. While we are visiting the node (each node is visited exactly once),
we might as well do the ans += abs(left_sum - right_sum) part.


Think about a recursive function. Beside the tilt of subtrees,
we also need to get the sum of subtrees.
So I came up with the idea of sub function tilt(root),
which returns the tuple (sum, tilt) of tree

"""

class Solution:
    def findTilt(self, root):
        self.ans = 0

        def _sum(node):
            if not node: return 0
            left, right = _sum(node.left), _sum(node.right)
            self.ans += abs(left - right)
            return node.val + left + right

        _sum(root)
        return self.ans




