#DFS

class Solution1:
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




#BFS
class Solution3:
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


class Solution3:
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






