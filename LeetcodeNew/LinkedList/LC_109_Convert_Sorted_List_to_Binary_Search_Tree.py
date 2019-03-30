"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/237156/recursively-python

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        # here we get the middle point,
        # even case, like '1234', slow points to '2',
        # '3' is root, '12' belongs to left, '4' is right
        # odd case, like '12345', slow points to '2', '12'
        # belongs to left, '3' is root, '45' belongs to right
        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # tmp points to root
        tmp = slow.next
        # cut down the left child
        slow.next = None
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root


class SolutionCaikehe:
    # convert linked list to array
    def sortedListToBST1(self, head):
        ls = []
        while head:
            ls.append(head.val)
            head = head.next
        return self.helper(ls, 0, len(ls) - 1)

    def helper(self, ls, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(ls[start])
        mid = (start + end) >> 1
        root = TreeNode(ls[mid])
        root.left = self.helper(ls, start, mid - 1)
        root.right = self.helper(ls, mid + 1, end)
        return root

    # top-down approach, O(n*logn)
    def sortedListToBST2(self, head):
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.next.val)
        root.right = self.sortedListToBST(slow.next.next)
        slow.next = None
        root.left = self.sortedListToBST(head)
        return root

    # bottom-up approach, O(n)
    def sortedListToBST3(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        return self.convert([head], 0, l - 1)

    def convert(self, head, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(head, start, mid - 1)
        root = TreeNode(head[0].val)
        root.left = l
        head[0] = head[0].next
        root.right = self.convert(head, mid + 1, end)
        return root

    # bottom-up approach, O(n)
    def sortedListToBST(self, head):
        l, p = 0, head
        while p:
            l += 1
            p = p.next
        self.node = head
        return self.convert(0, l - 1)

    def convert(self, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        l = self.convert(start, mid - 1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next
        root.right = self.convert(mid + 1, end)
        return root




