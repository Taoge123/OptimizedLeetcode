"""

https://buptwc.com/2018/08/26/Leetcode-894-All-Possible-Full-Binary-Trees/



A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.



Example 1:

Input: 7
Output:

[[0,0,0,null,null,0,0,null,null,0,0],
[0,0,0,null,null,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],
[0,0,0,0,0,null,null,0,0]]
Explanation:

显然完全二叉树的节点个数必是奇数，故if N % 2 == 0: return []
我们定义cache[i]表示i个节点构造出的完全二叉树的所有可能
如果N = 1，显然只有一种情况
如果N = 3，显然也只有一种情况
如果N = 5，如果左孩子为cache[1]，右孩子则为cache[3];如果左孩子为cache[3]，右孩子为cache[1]
依此类推

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        N -= 1
        if N == 0: return [TreeNode(0)]
        ret = []
        for l in range(1, N, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        return ret



class Solution2:
    # define cache[i] represent the all possible full tree constructed by i nodes.
    def allPossibleFBT(N):
        if N % 2 == 0: return []  # the number of node must be odd
        cache = {}
        for i in range(1, N + 1, 2):  # only consider odd number
            if i == 1:  # initialize
                cache[1] = [TreeNode(0)]
                continue
            cache[i] = []
            for j in range(1, i, 2):  # j represent the number of node in left child
                for lkid in cache[j]:
                    for rkid in cache[i - 1 - j]:
                        node = TreeNode(0)
                        node.left = lkid
                        node.right = rkid
                        cache[i].append(node)
        return cache[N]

"""
Intuition and Algorithm

Let text{FBT}(N)FBT(N) be the list of all possible full binary trees with NN nodes.

Every full binary tree TT with 3 or more nodes, has 2 children at its root. 
Each of those children left and right are themselves full binary trees.

Thus, for N \geq 3N≥3, we can formulate the recursion: text{FBT}(N) =FBT(N)= [All trees with left child from 
text{FBT}(x)FBT(x) and right child from text{FBT}(N-1-x)FBT(N−1−x), for all xx].

Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.

Finally, we should cache previous results of the function text{FBT}FBT 
so that we don't have to recalculate them in our recursion.
"""


class Solution3:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            Solution.memo[N] = ans

        return Solution.memo[N]




