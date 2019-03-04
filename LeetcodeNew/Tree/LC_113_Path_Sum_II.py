"""
https://leetcode.com/problems/path-sum-ii/discuss/158342/Python-DFS-tm
大致思路就是每层递归用一个临时数组保存当前的路径，
最后将sum(temp) == target 来判断此路径是否满足条件，满足则放入Global数组。
这个思路还可以被优化：因为要好几次sum的调用，可以每一层递归的时候把target - root.val传下去。
"""

class Solution1:
    def pathSum(self, root, target):
        self.res = []
        self.dfs(root, target, [])
        return self.res

    def dfs(self, root, target, temp):
        if not root: return
        if not root.left and not root.right:
            temp.append(root.val)
            if sum(temp) == target:
                self.res.append(temp)
        self.dfs(root.left, target, temp + [root.val])
        self.dfs(root.right, target, temp + [root.val])


class Solution2:
    def pathSum(self, root, target):
        self.res = []
        self.dfs(root, target, [])
        return self.res

    def dfs(self, root, target, temp):
        if not root: return
        if not root.left and not root.right and root.val == target:
            temp.append(root.val)
            self.res.append(temp)
        self.dfs(root.left, target - root.val, temp + [root.val])
        self.dfs(root.right, target - root.val, temp + [root.val])


class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        if root.left:
            self.dfs(root.left, sum -root.val, ls +[root.val], res)
        if root.right:
            self.dfs(root.right, sum -root.val, ls +[root.val], res)

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, sum -root.val) + self.pathSum(root.right, sum -root.val)
        return [[root.val ] +i for i in tmp]

    # BFS + queue
    def pathSum3(self, root, sum):
        if not root:
            return []
        res = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curr, val, ls = queue.pop(0)
            if not curr.left and not curr.right and val == sum:
                res.append(ls)
            if curr.left:
                queue.append((curr.left, val +curr.left.val, ls +[curr.left.val]))
            if curr.right:
                queue.append((curr.right, val +curr.right.val, ls +[curr.right.val]))
        return res

    # DFS + stack I
    def pathSum4(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum -root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val -curr.right.val, ls +[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val -curr.left.val, ls +[curr.left.val]))
        return res

    # DFS + stack II
    def pathSum5(self, root, s):
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, ls = stack.pop()
            if not curr.left and not curr.right and sum(ls) == s:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, ls +[curr.right.val]))
            if curr.left:
                stack.append((curr.left, ls +[curr.left.val]))
        return res


