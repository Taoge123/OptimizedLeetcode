

"""

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?


http://www.cnblogs.com/grandyang/p/5188938.html
https://www.geeksforgeeks.org/largest-bst-binary-tree-set-2/
https://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
http://www.cnblogs.com/grandyang/p/5188938.html
https://blog.csdn.net/qq508618087/article/details/51731417


My dfs returns four values:

    - N is the size of the largest BST in the tree.
    - If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
    - If the tree is a BST, then min and max are the minimum/maximum value in the tree.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SubTree:
    def __init__(self, largest, size, min, max):
        self.largest = largest
        self.size = size
        self.min = min
        self.max = max


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res.largest

    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if root.val > left.max and root.val < right.min:
            size = left.size + right.size + 1
        else:
            size = float('-inf')

        largest = max(left.largest, right.largest, size)

        return SubTree(largest, size, min(root.val, left.min), max(root.val, right.max))


