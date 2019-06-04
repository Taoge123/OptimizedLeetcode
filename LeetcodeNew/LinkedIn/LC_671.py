




def findSecondMinimumValue(self, root):
    if not root or not root.left: return -1
    s = [root]
    smallest = float('inf')
    while s:
        temp = []
        for i in s:
            if i.val > root.val:
                smallest = min(smallest, i.val)
            elif i.left:
                temp.append(i.left)
                temp.append(i.right)
        s = temp
    return -1 if smallest == float('inf') else smallest


def findSecondMinimumValue(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.ans = -1
    self.first = root.val if root else -1

    def traverse(node):
        if node:
            if node.val > self.first and (self.ans == -1 or self.ans > node.val):
                self.ans = node.val
                return
            else:
                traverse(node.left)
                traverse(node.right)

    traverse(root)
    return self.ans


