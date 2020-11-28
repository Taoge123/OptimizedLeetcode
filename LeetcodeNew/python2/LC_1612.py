import collections

class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        queue1 = collections.deque()
        queue2 = collections.deque()
        queue1.append(root1)
        queue2.append(root2)

        self.bfs(count1, queue1)
        self.bfs(count2, queue2)
        return count1 == count2

    def bfs(self, count, queue):
        while queue:
            node = queue.popleft()
            if node.val != '+':
                count[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



class Solution2:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1 = collections.Counter(self.dfs(root1))
        count2 = collections.Counter(self.dfs(root2))
        return count1 == count2

    def dfs(self, node):
        if not node:
            return ""
        if node.val == "+":
            return self.dfs(node.left) + self.dfs(node.right)
        else:
            return node.val



