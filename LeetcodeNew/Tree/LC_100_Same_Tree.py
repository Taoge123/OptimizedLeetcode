
"""

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false


> 类型：DFSF分制
> Time Complexity O(N)
> Space Complexity O(h)
在每一层先检查再递归，所以这是pre-order的思路。
比对相等的条件：

p.val == q.val
if not p or not q: return p == q
如有不等，直接返回False，就不用继续递归了。最后左右孩子返回给Root：return left and right
p.s. 上面的第二个相等条件，检查了2种情况：
1.if not p and not q: return True
2.if not p or not q: return False

"""

import collections

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not p or not q:
            return False
        elif p.val!=q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

#DFS
class Solution2:
    def isSameTree(self, p, q):
        if not p or not q: return p == q
        if p.val != q.val: return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right

#Stack
class Solution3:
    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            stack.append((n1.right, n2.right))
            stack.append((n1.left, n2.left))
        return True

"""
Stack:             4 5 2 3 1
            1                     1
         2    3                 2    3 
       4   5 6  7             4  5  6  7

Queue:            1 2 3 4 5 6 7 
"""

#Queue
class Solution3:
    def isSameTree(self, p, q):
        queue = collections.deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2: continue
            if not n1 or not n2: return n1 == n2
            if n1.val != n2.val: return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True



