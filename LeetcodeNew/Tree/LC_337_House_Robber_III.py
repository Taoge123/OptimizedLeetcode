

"""

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


class Solution:
    class Solution(object):
        def rob(self, root):
            return self.robDFS(root)[1];

        def robDFS(self, node):
            if node is None:
                return (0, 0)
            l = self.robDFS(node.left)
            r = self.robDFS(node.right)
            return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))


class Solution1:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def superrob(node):
            # returns tuple of size two (now, later)
            # now: max money earned if input node is robbed
            # later: max money earned if input node is not robbed

            # base case
            if not node: return (0, 0)

            # get values
            left, right = superrob(node.left), superrob(node.right)

            # rob now
            now = node.val + left[1] + right[1]

            # rob later
            later = max(left) + max(right)

            return (now, later)

        return max(superrob(root))







