
"""
We are given the root node of a maximum tree:
a tree where every node has a value greater than any other value in its subtree.

Just as in the previous problem, the given tree was constructed from an list A
(root = Construct(A)) recursively with the following Construct(A) routine:

If A is empty, return null.
Otherwise, let A[i] be the largest element of A.  Create a root node with value A[i].
The left child of root will be Construct([A[0], A[1], ..., A[i-1]])
The right child of root will be Construct([A[i+1], A[i+2], ..., A[A.length - 1]])
Return root.
Note that we were not given A directly, only a root node root = Construct(A).

Suppose B is a copy of A with the value val appended to it.  It is guaranteed that B has unique values.

Return Construct(B).

Example 1:

Input: root = [4,1,3,null,null,2], val = 5
Output: [5,4,null,1,3,null,null,2]
Explanation: A = [1,4,2,3], B = [1,4,2,3,5]
Example 2:

Input: root = [5,2,4,null,1], val = 3
Output: [5,2,4,null,1,null,3]
Explanation: A = [2,1,5,4], B = [2,1,5,4,3]
Example 3:

Input: root = [5,2,3,null,1], val = 4
Output: [5,2,4,null,1,3]
Explanation: A = [2,1,5,3], B = [2,1,5,3,4]


"""

"""
Solution 1: Recursion
If root.val > val, recusion on the right.
Else, put right subtree on the left of new node TreeNode(val)

Time Complexity:
O(N) time,
O(N) recursion space.

"""

"""
If the value is greater than current node, then the entire current node becomes the left child.
If the value is lesser than the current node, then we recurse on the right child.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root

class SolutionRecursionLee:
    def insertIntoMaxTree(self, root, val):
        if root and root.val > val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node

class Solution2:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        nd = TreeNode(val)
        if val > root.val:
            nd.left = root
            return nd
        p = root
        while p.right and p.right.val > val:
            p = p.right
        nd.left = p.right
        p.right = nd
        return root




