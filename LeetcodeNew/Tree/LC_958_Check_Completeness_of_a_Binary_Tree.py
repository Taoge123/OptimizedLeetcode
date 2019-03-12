

"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

"""

"""
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after we met an empty one.
"""

import collections

class SolutionLee:
    def isCompleteTree(self, root):
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1

        return not any(bfs[i:])


"""
Traverse the tree one level at a time, adding both children of each node to the queue as we go. 
Keep a count of how many non-null nodes are left in the queue. 
The first time we encounter a null node popped from the queue, 
if the counter shows nothing left, the tree is complete - otherwise not.
"""


class Solution2:
    def isCompleteTree(self, root):
        count = 1 if root else 0
        nodes = [root]
        while nodes:
            x = nodes.pop(0)
            if not x:
                return count == 0
            count -= 1
            nodes += [x.left, x.right]
            count = count + 1 if x.left else count
            count = count + 1 if x.right else count

        return True

class Solution3:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return False
        q = collections.deque([root])
        while q[0]:
            x = q.popleft()
            q.append(x.left)
            q.append(x.right)

        for node in q:
            if node: return False
        return True

class SolutionOfficial:
    def isCompleteTree(self, root):
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2*v))
                nodes.append((node.right, 2*v+1))

        return  nodes[-1][1] == len(nodes)



