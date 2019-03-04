

"""
I use a additional function addLevel to record the level number of nodes,
then according to the level number, I can easily deal with the level order,
see the code for details
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Easiest
class SolutionBFS:
    def zigzagLevelOrder(self, root):
        res, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(res) < level+1:
                    res.append([])
                if level % 2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].insert(0, curr.val)
                queue.append((curr.left, level+1))
                queue.append((curr.right, level+1))
        return res


# dfs + stack
class SolutionDFS:
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
        elif not level % 2:  # if it is an even level, then then level ans should be inversed, so I use extend founction
            ans[level].append([root.val])
        else:
            ans[level].insert(0, root.val)  # if it is an odd level, then level ans should be ordinal, so I use insert function
        self.addLevel(ans, level + 1, root.left)
        self.addLevel(ans, level + 1, root.right)


