# import math
# class Solution:
#     def closestDivisors(self, num: int):
#         a = self.closePair(num + 1)
#         b = self.closePair(num + 2)
#         return a[1:] if a[0] < b[0] else b[1:]
#
#
#     def closePair(self, num):
#         if not num:
#             return 0
#         for i in range(math.floor(math.sqrt(num)) + 1, 0, -1):
#             j = num // i
#             if i * j == num and num % j == 0:
#                 return abs(int(i - j)), i, j
#         return [num-1, 1, num]
#

# import collections
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#
#     def pseudoPalindromicPaths(self, root: TreeNode) -> int:
#         count = collections.defaultdict(int)
#         self.res = []
#         self.helper(root, count)
#         return self.res
#
#     def helper(self, root, count):
#         if not root.left and not root.right:
#             if root.val not in count:
#                 count[root.val] = 1
#             else:
#                 count[root.val] -= 1
#             self.res.append(count)
#             return
#
#         flag = False
#         if root.val not in count:
#             count[root.val] = 1
#         else:
#             count[root.val] -= 1
#             flag = True
#
#         if root.left:
#             self.helper(root.left, count[root.val])
#
#             # if flag:
#             #     count[root.val] += 1
#             # else:
#             #     if root.val in count:
#             #         del count[root.val]
#
#         if root.right:
#             self.helper(root.right, count)
#             # if flag:
#             #     count[root.val] += 1
#             # else:
#             #     if root.val in count:
#             #         del count[root.val]
#
#
# tree = TreeNode(2)
# tree.left = TreeNode(3)
# tree.left.left = TreeNode(3)
# tree.left.right = TreeNode(1)
# tree.right = TreeNode(1)
# tree.right.right = TreeNode(1)
#
# a = Solution()
# print(a.pseudoPalindromicPaths(tree))
# # print(a.closePair(num))

class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        m, n = len(nums1), len(nums2)

        dp = [[float('-inf') for i in range(n)] for j in range(m)]
        dp[0][0] = nums1[0] * nums2[0]
        for i in range(1, m):
            dp[i][0] = nums1[i] * nums2[0]

        for j in range(1, n):
            dp[0][j] = nums1[0] * nums2[j]

        res = float('-inf')
        for i in range(1, m):
            for j in range(1, n):
                for x in range(i, 0, -1):
                    for y in range(j, 0, -1):
                        dp[i][j] = max(dp[i][j], dp[i-x][j - y] + nums1[i] * nums2[j], dp[i - x][j], dp[i][j - y])
                        res = max(res, dp[i][j])

        return res

nums1 = [-3,-8,3,-10,1,3,9]
nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]


a = Solution()

print(a.maxDotProduct(nums1, nums2))



