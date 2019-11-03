

"""
Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


https://leetcode.com/problems/house-robber-iii/discuss/79330/step-by-step-tackling-of-the-problem


Let

f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).

f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.

Then we have

f2(node) = f1(node.left) + f1(node.right) and

f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).



Termination condition: when do we know the answer to rob(root) without any calculation?
Of course when the tree is empty ---- we've got nothing to rob so the amount of money is zero.

Recurrence relation: i.e., how to get rob(root) from rob(root.left), rob(root.right), ... etc.
From the point of view of the tree root, there are only two scenarios at the end:
root is robbed or is not. If it is, due to the constraint that "we cannot rob any two directly-linked houses",
the next level of subtrees that are available would be the four "grandchild-subtrees"
(root.left.left, root.left.right, root.right.left, root.right.right).
However if root is not robbed, the next level of available subtrees would just be the two
"child-subtrees" (root.left, root.right).
We only need to choose the scenario which yields the larger amount of money.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.helper(root))

    def helper(self, root):
        if not root:
            return (0, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)

        now = root.val + left[1] + right[1]
        later = max(left) + max(right)

        return (now, later)







