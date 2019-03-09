


"""

https://leetcode.com/problems/print-binary-tree/discuss/106273/Simple-Python-with-thorough-explanation



Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

"""


class SolutionBest:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) / 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1, left, mid - 1)
            update_output(node.right, row + 1, mid + 1, right)

        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output




class SolutionLee:
    def printTree(self, root):
        if not root: return [""]

        def depth(root):
            if not root: return 0
            return max(depth(root.left), depth(root.right)) + 1

        d = depth(root)
        self.res = [[""] * (2 ** d - 1) for _ in range(d)]

        def helper(node, d, pos):
            self.res[-d - 1][pos] = str(node.val)
            if node.left: helper(node.left, d - 1, pos - 2 ** (d - 1))
            if node.right: helper(node.right, d - 1, pos + 2 ** (d - 1))

        helper(root, d - 1, 2 ** (d - 1) - 1)
        return self.res


class SolutionBFS:
    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        N = self.height(root)
        M = 2 ** N - 1
        ret = [[""] * M for x in range(N)]

        bfs = [(root, 0, 0, M)]
        for x in bfs:
            node, i, l, r = x[0], x[1], x[2], x[3]
            j = (r + l) // 2
            ret[i][j] = str(node.val)
            if node.left:
                bfs.append((node.left, i + 1, l, j))
            if node.right:
                bfs.append((node.right, i + 1, j, r))

        return ret






