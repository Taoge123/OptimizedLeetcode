"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        # divide list into two parts
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        # cut down the first part
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, left, right):
        if not left or not right:
            return left or right
        if left.val > right.val:
            left, right = right, left
        # get the return node "head"
        head = pre = left
        left = left.next
        while left and right:
            if left.val < right.val:
                pre.next = left
                left = left.next
            else:
                pre.next = right
                right = right.next
            pre = pre.next
        # l and r at least one is None



