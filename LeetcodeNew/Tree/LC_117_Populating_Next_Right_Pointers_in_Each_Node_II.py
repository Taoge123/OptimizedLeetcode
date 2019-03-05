import collections

def connect(self, root):
    if not root:
        return
    # connect nodes level by level,
    # similar to level order traversal
    queue = collections.deque([root])
    nextLevel = collections.deque([])
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



class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = collections.deque()
        queue.append(root)
        while queue:
            _len = len(queue)
            for i in range(_len):
                node = queue.popleft()
                if i < _len - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)






