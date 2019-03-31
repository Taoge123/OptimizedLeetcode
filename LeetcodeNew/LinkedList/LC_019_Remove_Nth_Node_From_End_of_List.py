
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionCaikehe:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


class Solution2:
    def removeNthFromEnd(self, head, n):
        dummy = l = ListNode(0)
        dummy.next = r = head
        for _ in range(n):
            r = r.next
        while r:
            l, r = l.next, r.next
        l.next = l.next.next
        return dummy.next


