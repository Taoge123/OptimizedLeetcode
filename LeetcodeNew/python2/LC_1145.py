"""
Intuition
The first player colors a node,
there are at most 3 nodes connected to this node.
Its left, its right and its parent.
Take this 3 nodes as the root of 3 subtrees.

The second player just color any one root,
and the whole subtree will be his.
And this is also all he can take,
since he cannot cross the node of the first player.


Explanation
count will recursively count the number of nodes,
in the left and in the right.
n - left - right will be the number of nodes in the "subtree" of parent.
Now we just need to compare max(left, right, parent) and n / 2

Finally, blue player is in the parent, left or the right of the red player.
The player whon colors more wins. So we just count the nodes which blue player can colors that is the parent,
the left or the right of the red player and see whether the max number is more than half of the total nodes.

"""
"""
self.count() will gives us the totla count for the entire tree
counter will gives us the left, and right, n - sum(counter) - 1 means the parent
https://www.youtube.com/watch?v=0MGbvRHYZxc
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        counter = [0, 0]
        self.count(root, x, counter)
        print(counter)
        return max(max(counter), n - sum(counter) - 1) > n // 2

    def count(self, node, x, counter):
        if not node:
            return 0

        left = self.count(node.left, x, counter)
        right = self.count(node.right, x, counter)

        if node.val == x:
            counter[0] = left
            counter[1] = right
        return left + right + 1


class Solution2:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        node = self.find(root, x)
        parent = self.count(root) - self.count(node)
        left = self.count(node.left)
        right = self.count(node.right)
        if (left + right < parent) or (left + parent < right) or (right + parent < left):
            return True
        return False

    def find(self, root, target):
        if not root:
            return None
        if root.val == target:
            return root
        left = self.find(root.left, target)
        right = self.find(root.right, target)
        return right if not left else left

    def count(self, node):
        if not node:
            return 0

        left = self.count(node.left)
        right = self.count(node.right)

        return left + right + 1











