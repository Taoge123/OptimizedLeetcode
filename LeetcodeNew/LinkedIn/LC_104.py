


# BFS + deque
def maxDepth(self, root):
    if not root:
        return 0
    from collections import deque
    queue = deque([(root, 1)])
    while queue:
        curr, val = queue.popleft()
        if not curr.left and not curr.right and not queue:
            return val
        if curr.left:
            queue.append((curr.left, val+1))
        if curr.right:
            queue.append((curr.right, val+1))

