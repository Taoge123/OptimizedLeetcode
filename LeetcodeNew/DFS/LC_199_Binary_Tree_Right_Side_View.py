

"""

Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

> 类型：BFS | DFS
> Time Complexity O(N)
> Space Complexity O(N)
思路1：BFS, Level Order，打印最右边

"""

from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root: return []
        q, res = deque([root]), []
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res

"""
思路2： DFS，先递归右，后递归左，记录一个深度，当进入新的一层深度，
将当前root.val放入return数组里。
            1
          2   3
        4  5 6  7
      8

res = [1, 3, 7, 8]

"""


class Solution2:
    def rightSideView(self, root):
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, level):
        if not node: return
        if level == len(self.res):
            self.res.append(node.val)
        self.dfs(node.right, level + 1)
        self.dfs(node.left, level + 1)

#Similar idea but if level > len(arr)-1:
# also works since only left can go beyound it

#Stefan solution
class Solutioin3:
    def rightSideView(self, root):
        if not root:
            return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

#DFS-traverse the tree right-to-left,
# add values to the view whenever we first reach a new record depth.
# This is O(n).
class Solution4:
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view


#Traverse the tree level by level and add the last value of each level to the view. This is O(n).
class Solution5:
    def rightSideView(self, root):
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
