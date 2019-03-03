
"""
https://leetcode.com/problems/binary-tree-cameras/solution/

Algorithm

Let solve(node) be some information about
how many cameras it takes to cover the subtree at this node in various states.
There are essentially 3 states:

[State 0] Strict subtree: All the nodes below this node are covered, but not this node.
[State 1] Normal subtree: All the nodes below and including this node are covered,
but there is no camera here.
[State 2] Placed camera: All the nodes below and including this node are covered,
and there is a camera here (which may cover nodes above this node).
Once we frame the problem in this way, the answer falls out:

To cover a strict subtree, the children of this node must be in state 1.
To cover a normal subtree without placing a camera here,
the children of this node must be in states 1 or 2,
and at least one of those children must be in state 2.
To cover the subtree when placing a camera here, the children can be in any state.

Consider a node in the tree.
It can be covered by its parent, itself, its two children.
Four options.

Consider the root of the tree.
It can be covered by left child, or right child, or itself.
Three options.

Consider one leaf of the tree.
It can be covered by its parent or by itself.
Two options.

If we set a camera at the leaf, the camera can cover the leaf and its parent.
If we set a camera at its parent, the camera can cover the leaf, its parent and its sibling.

We can see that the second plan is always better than the first.
Now we have only one option, set up camera to all leaves' parent.

Here is our greedy solution:

Set cameras on all leaves' parents, thenremove all covered nodes.
Repeat step 1 until all nodes are covered.
Explanation:
Apply a recusion function dfs.
Return 0 if it's a leaf.
Return 1 if it's a parent of a leaf, with a camera on this node.
Return 2 if it's coverd, without a camera on this node.

For each node,
if it has a child, which is leaf (node 0), then it needs camera.
if it has a child, which is the parent of a leaf (node 1), then it's covered.

If it needs camera, then res++ and we return 1.
If it's covered, we return 2.
Otherwise, we return 0.

"""

class SolutionLee:
    def minCameraCover(self, root):
        self.res = 0
        def dfs(root):
            if not root: return 2
            l = dfs(root.left)
            r = dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        return (dfs(root) == 0) + self.res


class SolutionDP:
    def minCameraCover(self, root):
        def solve(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node: return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)

            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(solve(root)[1:])








