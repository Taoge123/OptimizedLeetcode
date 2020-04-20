"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree



as [1 [3[5 6] 2 4]]. Note that this is just an example, you do not necessarily need to follow this format.

Or you can follow LeetCode's level order traversal serialization format, where each group of children is separated by the null value.



For example, the above tree may be serialized as [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14].

You do not necessarily need to follow the above suggested formats, there are many more different formats that work so please be creative and come up with different approaches yourself.



Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
Do not use class member/global/static variables to store states. Your encode and decode algorithms should be stateless.

"""
"""
Serialize with preorder traversal where sentinel "#" indicates the final child of a node has been processed, so the function returns to its parent call.
Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
While the next item is not "#", create a child with the item, add the child to the list of children and recurse to create its subtree.
Repeat until there are no more children, then ignore the "#".


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def serialize(self, root: 'Node') -> str:
        res = []
        self.preorder(root, res)
        return "".join(res)

    def preorder(self, node, res):
        if not node:
            return
        res.append(str(node.val))

        for child in node.children:
            self.preorder(child, res)

        res.append("#")

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return

        tokens = collections.deque(data.split())
        root = Node(int(tokens.popleft()), [])
        self.helper(root, tokens)
        return root

    def helper(self, node, tokens):
        if not tokens:
            return

        while tokens[0] != "#":
            value = tokens.popleft()
            child = Node(int(value), [])
            node.children.append(child)
            self.helper(child, tokens)
        tokens.popleft()


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




class Codec3:
    def serialize(self, root: 'Node') -> str:
        res = []
        self.helper1(root, res)
        return res

    def helper1(self, root, res):
        if not root:
            return
        print(type(res), type(root.val))
        res.append(root.val)
        res.append(len(root.children))

        for child in root.children:
            self.helper1(child, res)

    def deserialize(self, data: str) -> 'Node':
        if not data or len(data) == 0:
            return None

        queue = collections.deque(list(data))
        return self.helper2(queue)

    def helper2(self, queue):
        root = Node()
        root.val = queue.popleft()
        size = queue.popleft()
        root.children = []
        for i in range(size):
            root.children.append(self.helper2(queue))
        return root


root = Node(1, [])
node2 = Node(2, [])
node3 = Node(3, [])
node4 = Node(4, [])
node5 = Node(5, [])
node6 = Node(6, [])
root.children.append(node2)
root.children.append(node3)
root.children.append(node4)
root.children.append(node5)
root.children.append(node6)
node7 = Node(7, [])
node8 = Node(8, [])
node9 = Node(9, [])
node10 = Node(10, [])
node11 = Node(11, [])
node2.children.append(node7)
node2.children.append(node8)
node2.children.append(node9)
node3.children.append(node10)
node3.children.append(node11)

"""
            1
        2    3     4  5  6
       789  10 11    
[1, 5, 2, 3, 7, 0, 8, 0, 9, 0, 3, 2, 10, 0, 11, 0, 4, 0, 5, 0, 6, 0]

"""


a = Codec3()
data = a.serialize(root)
print(a.serialize(root))
print(a.deserialize(data))


