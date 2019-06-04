

class Solution(object):
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret


class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.output = []
        while root:
            self.output.append([])
            root = self.getLeaves(root)
        return self.output

    def getLeaves(self, root):
        if root.left == None and root.right == None:
            self.output[-1].append(root.val)
            return None

        if root.left:
            root.left = self.getLeaves(root.left)

        if root.right:
            root.right = self.getLeaves(root.right)

        return root


