

"""

https://leetcode.com/problems/average-of-levels-in-binary-tree/solution/

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5,
and on level 2 is 11. Hence return [3, 14.5, 11].


Let's visit every node of the tree once, keeping track of what depth we are on.
We can do this with a simple DFS.

When we visit a node, info[depth] will be a two element list,
keeping track of the sum of the nodes we have seen at this depth,
and the number of nodes we have seen. This is necessary
and sufficient to be able to compute the average value at this depth.

At the end of our traversal, we can simply read off the answer.

"""
import collections

class Solution:
    def averageOfLevels(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]



class SolutionBFS:
    def averageOfLevels(self, root):
        q = collections.deque([root])
        result = []
        while q:
            val, n = 0, len(q)
            for i in range(n):
                node = q.popleft()
                val += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(val / float(n))
        return result







