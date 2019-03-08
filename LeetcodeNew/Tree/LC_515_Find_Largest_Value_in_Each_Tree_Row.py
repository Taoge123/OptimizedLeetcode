
"""
Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""

import collections

class Solution11:
    def largestValues(self, root):
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            res.append(max(x.val for x in q))
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res


class Solution22:
    def largestValues(self, root):
        self.ans = []
        self.helper(root, 0)
        return self.ans

    def helper(self, node, level):
        if not node:
            return
        if len(self.ans) == level:
            self.ans.append(node.val)
        else:
            self.ans[level] = max(self.ans[level], node.val)
        self.helper(node.left, level + 1)
        self.helper(node.right, level + 1)



class Solution:
    def largestValues(self, root):
        if not root:
            return []
        left = self.largestValues(root.left)
        right = self.largestValues(root.right)
        return [root.val] + map(max, left, right)

"""
Note that map(max, left, right) will behave differently under Python3, 
in that if left and right are not the same length, 
corresponding to different depths of the tree, 
max will produce a result with a length of the shorter of the two.
"""

class Solution2:
    def findValueMostElement(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes









