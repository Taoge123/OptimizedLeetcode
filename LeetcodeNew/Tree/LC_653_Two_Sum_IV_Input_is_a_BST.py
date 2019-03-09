

"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""



class Solution:
    def findTarget(self, root, k):
        if not root: return False
        bfs, s = [root], set()
        for i in bfs:
            if k - i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False

"""
As you traverse the tree, put each node's value into a set. 
In order for some value x to sum up to k, the value k - x must have been in the set already. 
Therefore, assuming we have a set of node values, if we find a complement of a node in that set, 
we have found two values that sum up to k.
"""


class Solution2:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        return self.findTargetHelper(root, set(), k)

    def findTargetHelper(self, node, nodes, k):
        if not node:
            return False

        complement = k - node.val
        if complement in nodes:
            return True

        nodes.add(node.val)

        return self.findTargetHelper(node.left, nodes, k) or self.findTargetHelper(node.right, nodes, k)


class SolutionComprehensive:

    def findTarget(self, root, k):
        # Array to store elements tested during traversal
        nums = []
        # DFS pre-order using array of found elements
        return self._preOrderSearch(root, k, nums)
        # DFS in-order using array of found elements
        # return self._inOrderSearch(root, k, nums)
        # # DFS post-order using array of found elements
        # return self._postOrderSearch(root, k, nums)
        # # BFS Recruisive using array of found elements
        # return self._bfsSearchRecursive([root], k, nums)
        # # BFS Iterative using array of found elements
        # return self._bfsSearchIterative(root, k, nums)
        # # DFS in-order to sort and then use two pointer to find target
        # return self._bfsSortFirst(root, k)

    def _preOrderSearch(self, root, k, nums):
        if not root:
            return False
        needle = k - root.val
        if needle in nums:
            return True
        else:
            nums.append(root.val)
        return self._preOrderSearch(root.left, k, nums) or self._preOrderSearch(root.right, k, nums)

    def _inOrderSearch(self, root, k, nums):
        if not root:
            return False
        if self._inOrderSearch(root.left, k, nums):
            return True
        if (k - root.val) in nums:
            return True
        else:
            nums.append(root.val)
        if self._inOrderSearch(root.right, k, nums):
            return True
        return False

    def _postOrderSearch(self, root, k, nums):
        if not root:
            return False
        if self._postOrderSearch(root.left, k, nums) or self._postOrderSearch(root.right, k, nums):
            return True
        if (k - root.val) in nums:
            return True
        nums.append(root.val)
        return False

    def _bfsSearchRecursive(self, parentNodes, k, nums):
        if len(parentNodes) == 0:
            return False
        nodes = []
        for key, node in enumerate(parentNodes):
            if (k - node.val) in nums:
                return True
            nums.append(node.val)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
        return self._bfsSearch(nodes, k, nums)

    def _bfsSearchIterative(self, root, k, nums):
        q = [root]

        while len(q):
            node = q.pop(0)
            if (k - node.val) in nums:
                return True
            nums.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return False

    def _bfsSortFirst(self, root, k):
        nums = []
        self.inOrder(root, nums)
        l, r = 0, len(nums) - 1
        while l < r:
            if (nums[l] + nums[r]) == k:
                return True
            elif (nums[l] + nums[r]) < k:
                l += 1
            else:
                r -= 1
        return False

    def inOrder(self, root, nums):
        if root:
            self.inOrder(root.left, nums)
            nums.append(root.val)
            self.inOrder(root.right, nums)



