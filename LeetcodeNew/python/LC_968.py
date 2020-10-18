"""

方法一：动态规划
我们尝试覆盖每个节点，从树的顶部开始向下。所考虑的每个节点都必须由该节点或某个邻居的摄像机覆盖。

算法：

让 solve(node) 函数提供一些信息，说明在不同的状态下，需要多少摄像机才能覆盖此节点的子树。基本上有三种状态:

[状态 0]：森严的子树：该节点下的所有节点都被覆盖，但不包括该节点。
[状态 1]：正常的子树：该节点下的所有节点和该节点均被覆盖，但是该节点没有摄像头。
[状态 2]：放置摄像头：该节点和子树均被覆盖，且该节点有摄像头。
一旦我们用这种方式来界定问题，答案就明显了：

若要满足森严的子树，此节点的孩子节点必须处于状态 1。
若要满足正常的子树，此节点的孩子节点必须在状态 1 或 2，其中至少有一个孩子在状态 2。
若该节点放置了摄像头，则它的孩子节点可以在任一的状态。

"""
"""
方法二：贪心算法
于其试图从上到下覆盖每个节点，不如尝试从上到下覆盖它--考虑新放置一个具有最深节点的相机，a年后沿着树向上移动。

如果节点的子节点被覆盖，且该节点具有父节点，则最好的情况是将摄像机放置在父节点上。

算法：

如果一个节点有孩子节点且没有被摄像机覆盖，则我们需要放置一个摄像机在该节点。
此外，如果一个节点没有父节点且没有被覆盖，则必须放置一个摄像机在该节点。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1.安装监视器；2.被监视；3.未被监视

class Solution:
    def minCameraCover(self, root):
        self.res = 0
        if self.dfs(root) == 3:
            self.res += 1
        return self.res

    # 1.安装监视器；2.被监视；3.未被监视
    def dfs(self, node):
        if not node:
            return 2

        left = self.dfs(node.left)
        right = self.dfs(node.right)
        # 子节点未被监视，因此需要安装监视器
        if left == 3 or right == 3:
            self.res += 1
            return 1

            # 子节点安装了监视器，因此已经被监视
        if left == 1 or right == 1:
            return 2

        # 当前未被监视
        return 3




class SolutionDP:
    def minCameraCover(self, root):
        return min(self.solve(root)[1:])

    def solve(self, node):
        # 0: Strict ST; All nodes below this are covered, but not this one
        # 1: Normal ST; All nodes below and incl this are covered - no camera
        # 2: Placed camera; All nodes below this are covered, plus camera here
        if not node:
            return 0, 0, float('inf')
        L = self.solve(node.left)
        R = self.solve(node.right)
        """
        解释一下 dp数组
        dp0代表当前节点未被覆盖（可能是父节点为支配集里面的点，覆盖了当前节点）但该节点的子节点都被覆盖   时所需要的最小摄像头的数量
        dp1代表当前节点的子节点中有一个或者两个（图论里可以是多个）为支配集里面的点，所以把当前的点也覆盖了  时所需要的最小摄像头的数量
        dp2代表当前节点为支配集里面的点   时所需要的最小摄像头的数量
        """
        # 若想让此节点不被覆盖 但是子节点都被覆盖，则左右两个节点都要满足条件1，此节点等于左右节点dp1之和
        dp0 = L[1] + R[1]
        # 若想让当前节点满足条件1 有两种情况：1.左节点覆盖住了此节点，
        # 此时右节点要想满足全覆盖也有两种情况（dp1 and dp2，取最小值即可）
        # 2. 右节点覆盖住了此节点，此时左节点要想满足全覆盖也有两种情况（dp1 and dp2，取最小值即可）
        dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
        # 若想让当前节点满足条件2，此时左右节点都被此节点覆盖，所以左右节点可以选取任意一种状态
        dp2 = 1 + min(L) + min(R)
        return dp0, dp1, dp2




class SolutionGreedy:
    def minCameraCover(self, root):
        self.res = 0
        covered = {None}
        self.dfs(root, covered)
        return self.res

    def dfs(self, node, covered, par=None):
        if node:
            self.dfs(node.left, covered, node)
            self.dfs(node.right, covered, node)

            if (par is None and node not in covered or
                    node.left not in covered or node.right not in covered):
                self.res += 1
                covered.update({node, par, node.left, node.right})





