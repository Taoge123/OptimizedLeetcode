
"""

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor
and successor pointers in a doubly-linked list. For a circular doubly linked list,
the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation,
the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

Example 1:

Input: root = [4,2,5,1,3]

Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship,
while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]
Example 3:

Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.
Example 4:

Input: root = [1]
Output: [1]


Constraints:

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000


Just use inorder traversal, which finds the nodes in ascending order,
and store the head and previous node in global variables. After the traversal is finished,
prev is the "tail" of the double linked list so just connect it to the head.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.head = None
        self.prev = None

    def treeToDoublyList(self, root):
        if not root:
            return None
        self.treeToDoublyListHelper(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head

    def treeToDoublyListHelper(self, node):
        if not node: return
        self.treeToDoublyListHelper(node.left)
        if self.prev:
            node.left = self.prev
            self.prev.right = node
        else:  # We are at the head.
            self.head = node
        self.prev = node
        self.treeToDoublyListHelper(node.right)



class Solution2:
    def treeToDoublyList(self, root):
        if not root:
            return None
        dummy = Node(0, None, root)
        tail = self.helper(root, dummy)
        dummy.right.left = tail
        tail.right = dummy.right
        return dummy.right

    def helper(self, root, head):
        if not root: return head
        ltail = self.helper(root.left, head)
        ltail.right = root
        root.left = ltail
        return self.helper(root.right, root)





