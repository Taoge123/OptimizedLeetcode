


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class SolutionBest:
    def __init__(self):
        self.prev = None
        self.head = None
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            self.tail = self.prev
            return

        self.treeToDoublyList(root.left)
        root.left = self.prev
        if self.prev:
            self.prev.right = root
        else:
            self.head = root
        self.prev = root
        self.treeToDoublyList(root.right)

        self.tail.right = self.head
        self.head.left = self.tail
        return self.head


class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        head, tail = self.get_linked_list(root)
        head.left = tail
        tail.right = head
        return head

    def get_linked_list(self, node):
        ''' Helper function to turn subtree starting at node into linked list.
        Returns (head, tail) of the linked list.
        '''

        # if node has no children, both the head and the tail is itself.
        if not node.left and not node.right:
            return (node, node)

            # if a node has a left child, linked list starting at left subtree is predecessor of node.
            # otherwise, the head of the linked list at node is itself.
        lhead, ltail = self.get_linked_list(node.left) if node.left else (node, None)

        # if a node has a right child, linked list starting at right subtree is successor of node.
        # otherwise, the tail of the linked list at node is itself.
        rhead, rtail = self.get_linked_list(node.right) if node.right else (None, node)

        # perform the correct connections
        node.left, node.right = ltail, rhead
        if ltail:
            ltail.right = node
        if rhead:
            rhead.left = node

        # return the head and tail of the linked list with node as the root.
        return (lhead, rtail)

class Solution1:
    def treeToDoublyList(self, root):
        if not root: return
        dummy = Node(0, None, None)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right











