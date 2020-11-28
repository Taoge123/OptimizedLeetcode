
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(root):
            count = [0] * (distance + 1)
            if not root: return count, 0
            if not root.left and not root.right:
                count[0] = 1
                return count, 0
            countLeft, pairsLeft = dfs(root.left)  # left freq, and pairs
            countRight, pairsRight = dfs(root.right)  # right freq, and pairs
            # charge res
            res = pairsLeft + pairsRight

            for i in range(distance):
                for j in range(distance - 1 - i):
                    res += countLeft[i] * countRight[j]

            # charge count
            for i in range(1, distance + 1):
                count[i] = countLeft[i - 1] + countRight[i - 1]

            # return
            return count, res

        return dfs(root)[1]






