"""
I use a additional function addLevel to record the level number of nodes,
then according to the level number, I can easily deal with the level order,
see the code for details
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        ans = []
        self.addLevel(ans, 0, root)  # level from 0
        return ans

    def addLevel(self, ans, level, root):
        if not root:
            return
        elif len(ans) <= level:
            ans.append([root.val])
        # if it is an even level, then then level ans should be inversed, so I use extend founction
        elif not level % 2:
            ans[level].extend([root.val])
        # if it is an odd level, then level ans should be ordinal, so I use insert function
        else:
            ans[level].insert(0, root.val)
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)


#Caikehe version solution
class Solution1:
    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        self.dfs(root, 0, res)
        return res


    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.dfs(root.left, level + 1, res)
            self.dfs(root.right, level + 1, res)

# dfs + stack
class Solution2:
    def zigzagLevelOrder(self, root):
        # write your code here
        res, stack = [], [(root, 0)]
        while stack:
            cur, level = stack.pop()
            if cur:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(cur.val)
                else:
                    res[level].insert(0, cur.val)
                stack.append((cur.right, level+1))
                stack.append((cur.left, level+1))
        return res


class Solution3:
    def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level + 1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return res

"""
We don't really need 2 stacks, all we need is

one array that keeps track of current level/depth we are at and
direction, either zig (from left-to-right) or zag (from right-to-left)
the only difference between zig and zag is that 
we reverse the collection/array of nodes at the level 
we wanna process if the direction is zag
"""




