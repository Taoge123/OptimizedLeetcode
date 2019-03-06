

"""
Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    /
   2
  /
 1

Output: 2

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, path, parentval):
            if node is None:
                return path
            path = path + 1 if node.val == parentval + 1 else 1
            left = dfs(node.left, path, node.val)
            right = dfs(node.right, path, node.val)
            return max(left, right, path)

        return dfs(root, 0, 0)


class SolutionBFS:
    def longestConsecutive(root):
        if not root:
            return 0

        ret = 0
        stack = [(root, 1)]
        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append((node.left, cnt + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append((node.right, cnt + 1 if node.right.val == node.val + 1 else 1))
            ret = max(ret, cnt)

        return ret


class Solution2:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if not root:
            return self.res
        self.dfs(root, 1)
        return self.res

    def dfs(self, root, curLen):
        self.res = curLen if curLen > self.res else self.res
        if not root:
            return 0
        if root.left:
            if root.left.val == root.val + 1:
                self.dfs(root.left, curLen + 1)
            else:
                self.dfs(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.dfs(root.right, curLen + 1)
            else:
                self.dfs(root.right, 1)


class Solution3:
    def longestConsecutive(self, root):

        def dfs(root):
            l = dfs(root.left) + 1 if root.left else 1  # must calculate if root.left exists
            if root.left and root.left.val != root.val + 1:
                l = 1  # reset to 1 if numbers are not consecutive
            r = dfs(root.right) + 1 if root.right else 1  # must calculate if root.right exists
            if root.right and root.right.val != root.val + 1:
                r = 1  # reset to 1 if numbers are not consecutive
            self.depth = max(l, r, self.depth)
            return max(l, r)

        self.depth = 0
        if root:
            dfs(root)
        return self.depth


class SolutionEasy:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If it's empty then return 0
        if root == None:
            return 0
        max_consecutive = self.traverse(root, None, 1)
        return max_consecutive

    """
    root is the current node
    prev_val is the previous value
    consecuive_num is the number of consecutive times  
    """

    def traverse(self, root, prev_val, consecutive_num):
        # Return the last consecutive number if the root is null
        if root == None:
            return consecutive_num

        new_consecutive = 1
        # The check is there because we initiall set pre_val to None
        if prev_val != None:
            if root.val == prev_val + 1:
                # Overrrid the new_consecutive if the node is a consecutive node
                new_consecutive = (consecutive_num + 1)

        # Return max of either current consecutive, or the max of the left tree, or the right tree
        return max(consecutive_num, self.traverse(root.left, root.val, new_consecutive),
                   self.traverse(root.right, root.val, new_consecutive))

class Solution4:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root, -1.2345, 1)


    def helper(self, root, val, count):
        if not root:
            return count
        if root.val == val + 1:
            return max(self.helper(root.left, root.val, count + 1), self.helper(root.right, root.val, count + 1))
        else:
            return max(count, self.helper(root.left, root.val, 1), self.helper(root.right, root.val, 1))





