
"""

https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/discuss/604491/Python-DFS

If we find any one valid path, we return True. So dfs recursion should be:

# dfs(i, node)
if node.val == arr[i]:
    return dfs(i+1, node.left) or dfs(i+1, node.right)
Then we just need to figure out two base cases:

return True
We reach the end of arr and we reach a left node. And that arr[-1] == node.val, which gives us:

if i == n - 1 and not (node.left or node.right):
    return True
return False
When arr[i] != node.val, that path is invalid and there is no need to dfs on that path any more.
Or we finish iterating either the entire arr , or one of the tree path. But not simultaneously.
And we don't have to determine that simultaneousness because if it is, it will be caught in the previous dfs and return True or False.

if not node or i == n or arr[i] != node.val:
    return False
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
[8,3,null,2,1,5,4]
[8]
"""
class SolutionTony:
    def isValidSequence(self, root, arr):
        return self.dfs(root, arr, 0)

    def dfs(self, node, arr, i):
        # if not node and i >= len(arr):
        #     return True

        if not node or i >= len(arr):
            return False

        if node.val != arr[i]:
            return False

        # must check leaves
        if not node.left and not node.right and i == len(arr) - 1:
            return True

        return self.dfs(node.left, arr, i + 1) or self.dfs(node.right, arr, i + 1)



class SolutionDFS:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        n = len(arr)

        def dfs(i, node):
            if not node or i == n:
                return False
            if arr[i] != node.val:
                return False

            if i == n - 1 and not (node.left or node.right):
                return True

            return dfs(i + 1, node.left) or dfs(i + 1, node.right)

        return dfs(0, root)






class SolutionBFS:
    def isValidSequence(self, root: TreeNode, arr) -> bool:
        queue = collections.deque([root])
        i = 0
        n = len(arr)
        while i < n and queue:
            found = False
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()

                if node.val == arr[i]:
                    found = True
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if not found:
                return False

            i += 1

        return i == n and not queue


