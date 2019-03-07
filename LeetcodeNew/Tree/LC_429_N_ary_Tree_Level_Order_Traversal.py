"""
The solution maintains the array for each level.
for _ in range(len(q)) means the number of nodes in each level,
and this loop finds all the children which belong to this level.
"""


class Solution1:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root: return []
        q = deque([root])
        res = []
        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                for c in cur.children:
                    q.append(c)
                level.append(cur.val)
            res.append(level)
        return res


class Solution:
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret












