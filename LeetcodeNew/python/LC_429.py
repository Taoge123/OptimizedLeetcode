
import collections

class Solution:
    def levelOrder(self, root: 'Node'):

        res = []
        queue = collections.deque([root])
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            if level:
                res.append(level)
        return res



class Solution2:
    def levelOrder(self, root: 'Node'):

        res = []
        self.getLevel(root, res, 0)
        return res

    def getLevel(self, root, res, level):

        if not root:
            return []

        if level == len(res):
            res.append([])

        res[level].append(root.val)
        for child in root.children:
            self.getLevel(child, res, level + 1)

        return res



