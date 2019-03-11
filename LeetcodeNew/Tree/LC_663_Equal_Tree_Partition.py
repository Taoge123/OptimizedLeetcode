
"""

https://leetcode.com/problems/equal-tree-partition/discuss/106738/Clean-Java-and-CSolution-with-Explanation-and-Visualization-No-Extra-Data-Structure



Given a binary tree with n nodes,
your task is to check if it's possible to partition the tree to two trees
which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation:
    5
   /
  10

Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:
Input:
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.

"""


class Solution1:
    def checkEqualTree(self, root):
        seen = []

        def summation(node):
            if not node: return 0
            seen.append(summation(node.left) + summation(node.right) + node.val)
            return seen[-1]

        total = summation(root)
        seen.pop()
        return total / 2.0 in seen


"""
Now, if any edge is removed, the separated subtree will have the sum=total_sum - its_value.

- For example if we remove 28's left subtree, we will have two trees which have sums of: 28-7=21 and 7.

- We keep the total sum which is the given root's value. (Root of the updated tree).

- Then we perform a DFS and check node by node, if by removing an edge, 
  sum of the remaining nodes (rootSum - root.right.val) 
  equals to sum of separated subtree (root.right.val), we return true.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def update(node):
            if not node:
                return 0
            node.val += update(node.left) + update(node.right)
            return node.val

        target = update(root) / 2.0

        def check(node):
            if node:
                if node.val == target:
                    return True
                return check(node.left) or check(node.right)
            return False

        return check(root.left) or check(root.right)


"""
Idea: Denote by T the given binary tree. 
Denote by f(v) the sum of all node values of some subtree of T with root v. 
Then T admits an equal tree partition if and only if there exists some tree node v != root, 
such that f(v) == f(root) / 2.0. To implement the above algorithm, 
we first do a DFS and record f(v) for all tree nodes v in a list. 
Then we pop f(root) from the list and check if f(root) / 2.0 is in the list. 
If yes, we return True. Otherwise, we return False.

Time complexity: O(N), space complexity: O(N), where N is the total number of nodes in the tree.
"""


class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            res = l + r + root.val
            rec.append(res)
            return res

        rec = []
        val = dfs(root) / 2.0
        rec.pop()
        return val in rec




class Solution3:
    def checkEqualTree(self, root):  # dfs to find if exist one node such that node's tree sum==n/2
        value = set()  # store all value sum of each node,root cannot be full splited.

        def dfs(node):
            if not node:
                return 0
            val = node.val + dfs(node.left) + dfs(node.right)
            if node != root:  # don't add root value sum in set,so that this case will
                value.add(val)
            return val

        return dfs(root) * 0.5 in value




