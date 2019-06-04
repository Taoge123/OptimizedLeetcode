# 515. Find Largest Value in Each Tree Row

class Solution(object):
    def largestValues(self, root):
        ans = []
        if root is None:
            return ans
        queue = [root]
        while queue:
            ans.append(max(x.val for x in queue))
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return ans


class Solution(object):
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


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        ln = 0
        lst = [(root, 0)]
        while lst:
            node, level = lst.pop()
            if not node:
                return
            if ln == level:
                res.append([node.val])
                ln += 1
            else:
                res[level].append(node.val)
            if node.left:
                lst.append([node.left, level + 1])
            if node.right:
                lst.append([node.right, level + 1])

        return [max(x) for x in res]





