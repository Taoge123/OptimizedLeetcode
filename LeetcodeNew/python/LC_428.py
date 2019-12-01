
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

import collections

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def preorder(self, node, res):
        if not node:
            return
        res.append(str(node.val))

        for child in node.children:
            self.preorder(child, res)

        res.append("#")

    def serialize(self, root: 'Node') -> str:
        res = []
        self.preorder(root, res)
        return "".join(res)

    def helper(self, node, tokens):
        if not tokens:
            return

        while tokens[0] != "#":
            value = tokens.popleft()
            child = Node(int(value), [])
            node.children.append(child)
            self.helper(child, tokens)
        tokens.popleft()

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return

        tokens = collections.deque(data.split())
        root = Node(int(tokens.popleft()), [])
        self.helper(root, tokens)
        return root


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec2:

    def serialize(self, root: 'Node') -> str:

        if not root:
            return []

        if not root.children:
            return root.val

        return [
            root.val,
            [self.serialize(child) for child in root.children]
        ]

    def deserialize(self, data: str) -> 'Node':

        if data == []:
            return None

        if isinstance(data, int):
            return Node(data, [])

        return Node(
            val=data[0],
            children=[self.deserialize(child) for child in data[1]]
        )

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

