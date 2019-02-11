"""
Doing BFS right-to-left means we can simply return the last node's value
and don't have to keep track of the first node in the current row or even care about rows at all.
Inspired by @fallcreek's solution (not published) which uses two nested loops to go row by row
but already had the right-to-left idea making it easier. I just took that further.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeftMostNode(self, root):
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val


class Solution2:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue=list()
        queue.append(root)
        res=TreeNode(0)
        while queue:
            res=queue.pop(0)
            if res.right:
                queue.append(res.right)
            if res.left:
                queue.append(res.left)
        return res.val

class Solution5:
    def findBottomLeftValue(self, root):
        currLevel, nextLevel = [root], []
        while currLevel:
            currNode = currLevel.pop()
            if currNode.right:
                nextLevel.insert(0, currNode.right)
            if currNode.left:
                nextLevel.insert(0, currNode.left)
            if not currLevel:
                currLevel = nextLevel
                nextLevel = []
        return currNode.val

#DFS
class Solution3:
    def findLeftMostNode(self, root):
        self.max_level = 0
        self.val = None
        self.helper(root, 1)
        return self.val

    def helper(self, root, level):
        if not root: return
        print(level)
        if level > self.max_level:
            self.max_level = level
            self.val = root.val
        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)


class Solution4:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # frist element stores max level, second stores value
        res = [-1, 0]
        self.dfs(root, res, 0)
        return res[1]

    def dfs(self, root, res, level):
        if not root:
            return

        if level > res[0]:
            res[0], res[1] = level, root.val

        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)




a = Solution3()
a.findLeftMostNode()



