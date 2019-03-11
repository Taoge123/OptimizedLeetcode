
"""
https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand
https://leetcode.com/problems/longest-univalue-path/discuss/186594/Python-Use-more-info-during-DFS


Given a binary tree, find the length of the longest path where each node in the path has the same value.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2

"""

"""
Let arrow_length(node) be the length of the longest arrow that extends from the node. 
That will be 1 + arrow_length(node.left) if node.left exists and has the same value as node. 
Similarly for the node.right case.

While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node. 
We record these candidate answers and return the best one.

"""


class Solution1:
    def longestUnivaluePath(self, root):
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans



"""
The approach is similar to the Diameter of Binary Tree question except 
that we reset the left/right to 0 whenever the current node does not match the children node value.

In the Diameter of Binary Tree question, the path can either go through the root or it doesn't.

Hence at the end of each recursive loop, return the longest length using that node 
as the root so that the node's parent can potentially use it in its longest path computation.

We also use an external variable longest that keeps track of the longest path seen so far.

"""


class Solution2:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len = traverse(node.left)
            right_len = traverse(node.left)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]







