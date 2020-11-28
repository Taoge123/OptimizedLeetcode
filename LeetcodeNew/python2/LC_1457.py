class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root):
        count = set()
        return self.dfs(root, count)

    def dfs(self, root, count):
        if not root:
            return 0
        if root.val in count:
            count.discard(root.val)
        else:
            count.add(root.val)

        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right:
            res += len(count) <= 1

        if root.val in count:
            count.discard(root.val)
        else:
            count.add(root.val)

        return res



class Solution2:
    def pseudoPalindromicPaths(self, root):
        count = 0
        return self.dfs(root, count)

    def dfs(self, root, count):
        if not root:
            return 0
        count ^= 1 << (root.val - 1)
        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right:
            # 10000 or 0000000
            if count & (count - 1) == 0:
                res += 1
        return res




class Solution3:
    def pseudoPalindromicPaths(self, root):
        count = 0
        res = []
        self.dfs(root, [], res)

        for path in res:
            if self.check(path):
                count += 1
        return count

    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            path.append(root.val)
            res.append(path)
            return

        self.dfs(root.left, path + [root.val], res)
        self.dfs(root.right, path + [root.val], res)

    def check(self, path):
        return sum(v % 2 for v in collections.Counter(path).values()) < 2

