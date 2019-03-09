

"""
https://leetcode.com/problems/find-duplicate-subtrees/discuss/106016/O(n)-time-and-space-lots-of-analysis

-
Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4


We can serialize each subtree. For example, the tree

   1
  / \
 2   3
    / \
   4   5
can be represented as the serialization 1,2,#,#,3,4,#,#,5,#,#,
which is a unique representation of the tree.

"""
import collections

class Solution:
    def findDuplicateSubtrees(self, root):
        count = collections.Counter()
        ans = []
        def collect(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial

        collect(root)
        return ans


class Solution2:
    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans


"""
因为求的是从叶子节点往上的subtree是否有重复，这题用Postorder解，然后从叶子节点开始往上return，
每次把以root为节点的subtree存入字典的key，然后将字典重复的root放进res返回。"""


class SolutionYu:
    def findDuplicateSubtrees(self, root):
        self.res = []
        self.dic = {}
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return '#'
        tree = self.dfs(root.left) + self.dfs(root.right) + str(root.val)
        if tree in self.dic and self.dic[tree] == 1:
            self.res.append(root)
        self.dic[tree] = self.dic.get(tree, 0) + 1
        return tree


"""
Yes in-order doesn't work as it mentioned in another thread.
However pre-oder works. When you construct the tree in pre-order, 
you know exactly where you start --- root. 
Then you will go to current node's children unless you meet two "null". 
As you can see, the tree constructed is unique.
"""
class SolutionLee:
    def findDuplicateSubtrees(self, root):
        def trv(root):
            if not root: return "null"
            current = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            res[current].append(root)
            return current

        res = collections.defaultdict(list)
        trv(root)
        return [res[current][0] for current in res if len(res[current]) > 1]



class SolutionStefan:
    def findDuplicateSubtrees(self, root):
        def tuplify(root):
            if root:
                tuple = root.val, tuplify(root.left), tuplify(root.right)
                trees[tuple].append(root)
                return tuple

        trees = collections.defaultdict(list)
        tuplify(root)
        return [roots[0] for roots in trees.values() if roots[1:]]




