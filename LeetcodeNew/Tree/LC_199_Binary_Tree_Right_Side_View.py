

"""
Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""



# 思路1：BFS, Level Order，打印最右边

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


# 思路2： DFS，先递归右，后递归左，记录一个深度，当进入新的一层深度，将当前root.val放入return数组里。

class Solution:
    def rightSideView(self, root):
        self.res = []
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, depth):
        if not node: return
        if depth == len(self.res):
            self.res.append(node.val)
        self.dfs(node.right, depth + 1)
        self.dfs(node.left, depth + 1)


        




