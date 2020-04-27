import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque()
        queue.append(root)

        while queue[0] != None:
            node = queue.popleft()
            queue.append(node.left)
            queue.append(node.right)

        while len(queue) > 0 and queue[0] == None:
            queue.popleft()
        return len(queue) == 0




class SolutionLee:
    def isCompleteTree(self, root):
        queue = [root]
        i = 0
        while queue[i]:
            queue.append(queue[i].left)
            queue.append(queue[i].right)
            i += 1
        return not any(queue[i:])




