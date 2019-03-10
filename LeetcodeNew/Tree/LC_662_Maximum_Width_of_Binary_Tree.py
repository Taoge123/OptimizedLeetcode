

"""
Example 1:

Input:

           1
         /   \
        3     2
       / \     \
      5   3     9

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


"""
class Solution1:
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans




class Solution2:
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans



"""
在知道如何表达之后，我们要做的是外围存一个global的最大宽度变量，在每层递归的时候，
用将最右边的数减去最左边的，然后和外围的global比对即可。如果比global大，就跟新global。

这题如果用分制也很一样，就是对返回值进行比对即可。
"""

class Solution22:
    def widthOfBinaryTree(self, root):
        self.res = 1
        self.dfs(root, 0, 1, [])
        return self.res

    def dfs(self, root, level, index, start):
        if not root: return
        if len(start) == level:
            start.append(index)
        else:
            self.res = max(self.res, index - start[level] + 1)
        self.dfs(root.left, level + 1, index * 2, start)
        self.dfs(root.right, level + 1, index * 2 + 1, start)




class SolutionBFS:
    def widthOfBinaryTree(self, root):
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0
        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)

        return ans


class SolutionDFS:
    def widthOfBinaryTree(self, root):
        def dfs(node, depth=0, pos=0):
            if node:
                yield depth, pos
                yield from dfs(node.left, depth + 1, pos * 2)
                yield from dfs(node.right, depth + 1, pos * 2 + 1)

        left = {}
        right = {}
        ans = 0
        for depth, pos in dfs(root):
            left[depth] = min(left.get(depth, pos), pos)
            right[depth] = max(right.get(depth, pos), pos)
            ans = max(ans, right[depth] - left[depth] + 1)

        return ans







