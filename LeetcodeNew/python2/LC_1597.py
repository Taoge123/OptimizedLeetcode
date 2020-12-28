# Definition for a binary tree node.
class Node:
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        n = len(s)
        if n == 1:
            return Node(s)

        idx = None
        count = 0
        for i in range(n - 1, 0, -1):
            if s[i] == ")":
                count += 1
            elif s[i] == "(":
                count -= 1
            elif count == 0:
                if s[i] in "+-":
                    idx = i
                    break
                elif s[i] in "*/" and idx is None:
                    idx = i
        if not idx:
            return self.expTree(s[1:-1])
        node = Node(s[idx])
        node.left = self.expTree(s[:idx])
        node.right = self.expTree(s[idx + 1:])
        return node


class Solution2:
    class Solution:
        def expTree(self, s: str) -> 'Node':

            def build(s, start, end):
                if start == end:
                    return Node(s[start])
                count, mul_div = 0, -1
                for i in range(end, start - 1, -1):
                    if s[i] == '(':
                        count += 1
                    elif s[i] == ')':
                        count -= 1
                    elif count == 0 and s[i] in '+-':
                        n = Node(s[i])
                        n.left = build(s, start, i - 1)
                        n.right = build(s, i + 1, end)
                        return n
                    elif count == 0 and s[i] in '*/':
                        mul_div = i
                else:
                    if mul_div == -1:
                        return build(s, start + 1, end - 1)
                    else:
                        node = Node(s[mul_div])
                        node.left = build(s, start, mul_div - 1)
                        node.right = build(s, mul_div + 1, end)
                        return node

            return build(s, 0, len(s) - 1)

