# from sortedcontainers import SortedDict
#
# a = SortedDict()
# a[1] = 1
# a[2] = 1
# a[3] = 1
# a[5] = 1
# a[6] = 1

# 1 2 3 5 6
# 0 1 2 3 4
# print(a.bisect_left(4))

# nums = [84139415,693324769,614626365,497710833,615598711,264,65552,50331652,1,1048576,16384,544,270532608,151813349,221976871,678178917,845710321,751376227,331656525,739558112,267703680]
#
# for num in nums:
#     print(bin(num)[2:])
#
#
import collections

# class Solution:
#     def sumPrefixScores(self, words):
#
#         table = collections.defaultdict(int)
#
#         for word in words:
#             for i in range(1, len(word)+1):
#                 table[word[:i]] += 1
#         print(table)
#
#
# words = ["abc","ab","bc","b"]
# a = Solution()
# print(a.sumPrefixScores(words))
#


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root):

        def dfs(root, level):
            if not root:
                return

            if level % 2 == 0 and root.left and root.right:
                root.left.val, root.right.val = root.right.val, root.left.val

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return root

        dfs(root, 0)
        return root


# root = TreeNode(2)
# root.left = TreeNode(3)
# root.right = TreeNode(5)
# root.left.left = TreeNode(8)
# root.left.right = TreeNode(13)
# root.right.left = TreeNode(21)
# root.right.right = TreeNode(34)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(1)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(1)


a = Solution()
print(a.reverseOddLevels(root))



