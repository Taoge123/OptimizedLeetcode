

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

from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue, res = deque([root]), []

        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res


class SolutionBFS:
    def levelOrder(self, root):
        if root is None: return []
        q = [[root]]
        for level in q:
            record = []
            for node in level:
                if node.left: record.append(node.left)
                if node.right: record.append(node.right)
            if record: q.append(record)
        return [[x.val for x in level] for level in q]

class SolutionPythonic:
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans










