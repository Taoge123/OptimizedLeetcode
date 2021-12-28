
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root):

        self.visited = []
        summ = self.dfs(root)
        if summ / 2 != summ // 2:
            return False

        # Need to pop out the total sum [0, -1, 1], in this case 0 is the sum and 0 is in visited
        self.visited.pop()
        target = summ // 2
        return target in self.visited

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        summ = left + right + root.val
        self.visited.append(summ)
        return summ



class SolutionTonyIncorrect:
    def checkEqualTree(self, root):

        self.visited = set()
        self.sum = 0
        self.dfs(root)
        # print(self.sum)
        if self.sum / 2 != self.sum // 2:
            return False

        target = self.sum // 2
        return target in self.visited

    def dfs(self, root):
        if not root:
            return

        self.sum += root.val
        self.visited.add(self.sum)
        self.dfs(root.left)
        self.dfs(root.right)






