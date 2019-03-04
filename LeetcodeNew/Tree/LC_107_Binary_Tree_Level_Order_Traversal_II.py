import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs recursively
    def levelOrderBottom(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level + 1)].append(root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

    # dfs + stack
    def levelOrderBottom1(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                stack.append((node.right, level + 1))
                stack.append((node.left, level + 1))
        return res

    # bfs + queue
    def levelOrderBottom2(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level + 1)].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res



    def levelOrderBottomLee(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return res[::-1]

    def levelOrderBottomLee2(self, root):
        res, queue = [], [root]
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return res[-2::-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrderBottom(root)
    print(result)


