"""
117. Populating Next Right Pointers in Each Node II

"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections

# Level order traversal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        queue, nextLevel = collections.deque([root]), collections.deque()

        while queue:
            node = queue.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if queue:
                node.next = queue[0]
            if not queue:
                queue, nextLevel = nextLevel, queue

        return root

#
# cur = queue
# pre = cur
# head = level
#
# queue is traversal for every single layer
# cur is previous layer
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue, level, curr = root, None, None

        while queue:
            # if queue:
            #     print('queue', queue.val)
            # if level:
            #     print('level', level.val)
            # if curr:
            #     print('curr', curr.val)
            # print('---------------')
            if queue.left:
                if not level:
                    level = curr = queue.left
                else:
                    curr.next = queue.left
                    curr = curr.next
            if queue.right:
                if not level:
                    level = curr = queue.right
                else:
                    curr.next = queue.right
                    curr = curr.next
            if queue:
                print(queue.val)
                print('-')
            queue = queue.next
            if queue:
                print(queue.val)
            print('------')
            if not queue and level:
                queue, level, curr = level, None, None
        return root










