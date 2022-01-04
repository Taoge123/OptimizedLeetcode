import collections
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTonyMap:
    def pseudoPalindromicPaths(self, root):
        table = collections.defaultdict(int)
        return self.dfs(root, table)

    def dfs(self, node, table):
        if not node:
            return 0
        # print(table, '1')
        table[node.val] += 1
        table[node.val] %= 2
        if table[node.val] == 0:
            del table[node.val]
        if node and not node.left and not node.right:
            if len(table.keys()) in [0, 1]:
                return 1
            else:
                return 0
        return self.dfs(node.left, copy.deepcopy(table)) + self.dfs(node.right, copy.deepcopy(table))


class SolutionTonySet:
    def pseudoPalindromicPaths(self, root):
        # table = collections.defaultdict(int)
        table = set()
        return self.dfs(root, table)

    def dfs(self, node, table):
        if not node:
            return 0
        if node.val in table:
            table.discard(node.val)
        else:
            table.add(node.val)
        if node and not node.left and not node.right:
            if len(table) in [0, 1]:
                return 1
            else:
                return 0
        return self.dfs(node.left, set(table)) + self.dfs(node.right, set(table))



class SolutionTonySet2:
    def pseudoPalindromicPaths(self, root):
        # table = collections.defaultdict(int)
        table = set()
        return self.dfs(root, table)

    def dfs(self, node, table):
        if not node:
            return 0

        if node.val in table:
            table.discard(node.val)
        else:
            table.add(node.val)

        res = 0
        if node and not node.left and not node.right:
            if len(table) in [0, 1]:
                res += 1

        res += self.dfs(node.left, table) + self.dfs(node.right, table)

        if node.val in table:
            table.discard(node.val)
        else:
            table.add(node.val)
        return res



class SolutionRika:
    def pseudoPalindromicPaths(self, root):

        table = set()
        self.res = 0
        self.dfs(root, table)
        return self.res

    def dfs(self, root, table):
        if not root:
            return

        if root.val not in table:
            table.add(root.val)
        else:
            table.remove(root.val)

        if not root.left and not root.right:
            if len(table) < 2:
                self.res += 1

        self.dfs(root.left, table)
        self.dfs(root.right, table)

        # backtracking
        if root.val not in table:
            table.add(root.val)
        else:
            table.remove(root.val)



class Solution:
    def pseudoPalindromicPaths(self, root):
        count = set()
        return self.dfs(root, count)

    def dfs(self, root, count):
        if not root:
            return 0
        if root.val in count:
            count.discard(root.val)
        else:
            count.add(root.val)

        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right:
            res += len(count) <= 1

        if root.val in count:
            count.discard(root.val)
        else:
            count.add(root.val)

        return res



class Solution2:
    def pseudoPalindromicPaths(self, root):
        count = 0
        return self.dfs(root, count)

    def dfs(self, root, count):
        if not root:
            return 0
        count ^= 1 << (root.val - 1)
        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right:
            # 10000 or 0000000
            if count & (count - 1) == 0:
                res += 1
        return res




class Solution3:
    def pseudoPalindromicPaths(self, root):
        count = 0
        res = []
        self.dfs(root, [], res)

        for path in res:
            if self.check(path):
                count += 1
        return count

    def dfs(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            path.append(root.val)
            res.append(path)
            return

        self.dfs(root.left, path + [root.val], res)
        self.dfs(root.right, path + [root.val], res)

    def check(self, path):
        return sum(v % 2 for v in collections.Counter(path).values()) < 2




root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(2)


a = SolutionTony()
print(a.pseudoPalindromicPaths(root))