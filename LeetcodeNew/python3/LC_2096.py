
import collections

class SolutionLCADFS:
    def getDirections(self, root, startValue: int, destValue: int):
        lca = self.lca(root, startValue, destValue)
        queue = collections.deque()
        queue.append([lca, ""])
        beginPath = ""
        destPath = ""

        while queue:
            node, path = queue.popleft()
            if node.val == startValue:
                beginPath = path
                if destPath: break  # break if you have already found destPath
            if node.val == destValue:
                destPath = path
                if beginPath: break  # break if you have already found beginPath

            if node.left:
                queue.append([node.left, path + 'L'])

            if node.right:
                queue.append([node.right, path + 'R'])

        return 'U' * len(beginPath) + destPath

    def lca(self, root, p, q):
        if not root:
            return None

        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        if root.val == p or root.val == q:
            return root

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


class SolutionLCADFS:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        lca = self.dfs(root, startValue, destValue)

        ## generate the path using least common ancestor
        def dfs(root, value):
            if (not root):
                return ''
            left = dfs(root.left, value)
            right = dfs(root.right, value)

            if ('X' in left and 'X' not in right):
                return 'L' + left
            if ('X' in right and 'X' not in left):
                return 'R' + right

            ## last condition to check
            if (root.val == value):
                return 'X'
            return 'L' + left + 'R' + right

        root_to_start = dfs(lca, startValue).replace('X', '')
        root_to_dest = dfs(lca, destValue).replace('X', '')
        rev_start = 'U' * len(root_to_start)
        return rev_start + root_to_dest

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if root.val == p or root.val == q:
            return root

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left