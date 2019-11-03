

"""
Binary Tree Level Order Traversal
Time: O(N) | Space: O(size of return array + size of queue) -> Worst Case O(2N)
queue的概念用deque来实现，popleft() 时间复杂为O(1)即可

外围的While用来定义BFS的终止条件，所以我们最开始initialize queue的时候可以直接把root放进去
在每层的时候，通过一个cur_level记录当前层的node.val，
size用来记录queue的在增加子孙node之前大小，因为之后我们会实时更新queue的大小。
当每次从queue中pop出来的节点，把它的左右子节点放进Queue以后，
记得把节点本身的的value放进cur_level
for loop终止后，就可以把记录好的整层的数值，放入我们的return数组里。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        if p and q:
            return p.val == q.val and self.dfs(p.left, q.right) and self.dfs(p.right, q.left)

        return p == q











