# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):

        # 0 means not covered。1 means covered but not has a camera on it. 2 means a camera on it.
        # reference: https://www.itread01.com/content/1546174153.html
        def dfs(node):
            if not node:
                return 1
            l = dfs(node.left)
            r = dfs(node.right)

            if l == 0 or r == 0:
                self.sum += 1
                return 2
            elif l == 2 or r == 2:
                return 1
            else:
                return 0

        self.sum = 0
        if dfs(root) == 0:
            self.sum += 1

        return self.sum

# node has three status iscamera_no_need, notcamera_noneed,notcamera_need

class Solution2:
    def minCameraCover(self, root):
        def dfs(node):
            if not node:
                return float('inf'),0,float('inf')
            if not node.left and not node.right:
                return 1,float('inf'),0
            lis_no,lnot_no,lnot_yes=dfs(node.left)
            ris_no,rnot_no,rnot_yes=dfs(node.right)
            is_no=1+min(lis_no,lnot_no,lnot_yes)+min(ris_no,rnot_no,rnot_yes)
            not_no=min(lis_no+min(ris_no,rnot_no),ris_no+min(lis_no,lnot_no))
            not_yes=lnot_no+rnot_no
            return is_no,not_no,not_yes
        res=dfs(root)
        return min(res[0],res[1])


"""
Thoughts:
From given example, we can find that the root node can always been covered by a camera on left or right.
So that means the root's status will be decided by left or right tree, take that into consideration, we use "bottom-up" rather than "top-down"

We start to solve the problem from leaf node.

Divide:
Node Return :(hasCamera, covered)

if node has a camera , return true
if node has been monitored, return true
Conquer:

if leftHasCamera or rightHasCamera, current node covered = true
if current node's left or right child not covered, that means we have to put a camera at current node to cover that , there is no 2nd option here.
Thus, when #2 happens, we need put down a camera by self.count +=1, update corresponding values

Edge case
We need to check the root's covered status after we run recursion. if it is False, we need +1 to our final result

"""


class Solutio3:
    def minCameraCover(self, root):
        self.needcover = 0
        self.covered = 1
        self.camera = 2
        self.ans = 0
        if self.helper(root) == self.needcover:
            return self.ans + 1
        return self.ans

    def helper(self, root):
        if not root: return -1
        left = self.helper(root.left)
        right = self.helper(root.right)

        if left == self.needcover or right == self.needcover:
            self.ans += 1
            return self.camera

        if left == self.camera or right == self.camera:
            return self.covered

        return self.needcover


