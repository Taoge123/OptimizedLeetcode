"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/755788/Python-Easy-python-Counter-dfs-solution
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/756278/Python-solution-with-explanation

"""


import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionRika1:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        self.dfs(root, 0, distance)
        return self.res

    def dfs(self, root, depth, target):
        if not root:
            return []

        if not root.left and not root.right:  # 每次返回左右孩子的【深度】list --> 深度为从root到叶子节点的距离
            return [depth]

        leftleaf = self.dfs(root.left, depth + 1, target)
        rightleaf = self.dfs(root.right, depth + 1, target)

        for left in leftleaf:
            for right in rightleaf:
                if left + right - 2 * depth <= target:  # root到左右叶子节点的距离和 - 最小公共祖先到root的距离*2 ==> 两个叶子节点的距离
                    self.res += 1

        return leftleaf + rightleaf



class SolutionRika2:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # similar to #863 all nodes distance k in binary tree --> only one target's neighbor nodes with k distance --> print neighbor
        # but this is getting many leaf_node's neighbor leaf_node with k distance --> how many pairs
        neighbors = collections.defaultdict(list)
        leaves = []
        # cerate neighbors and all leaf nodes
        self.dfs(root, None, leaves, neighbors)

        self.res = 0
        self.path = []
        for node in leaves:
            self.res += self.bfs(node, 0, set(), distance, leaves, neighbors)
        return self.res // 2

    def dfs(self, root, parent, leaves, neighbors):
        if not root:
            return

            # add leaves
        if not root.left and not root.right:
            leaves.append(root)
        # build graph for neighbors
        neighbors[root].append(parent)
        neighbors[parent].append(root)

        self.dfs(root.left, root, leaves, neighbors)
        self.dfs(root.right, root, leaves, neighbors)

    def bfs(self, root, dist, visited, k, leaves, neighbors):
        queue = collections.deque()
        queue.append(root)
        visited.add(root)
        res = 0

        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur and 0 < dist <= k and cur in leaves:  # 必须是下一个叶子节点 + 距离不能为0 或超过 k
                    res += 1

                if dist > k:
                    break
                for nei in neighbors[cur]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)

            dist += 1
        return res

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






