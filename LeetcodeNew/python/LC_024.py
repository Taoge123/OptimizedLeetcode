"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionBetter:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            first = curr.next
            second = curr.next.next

            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next

        return dummy.next





class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first = head
        second = head.next

        # Swapping
        first.next = self.swapPairs(second.next)
        second.next = first

        # Now the head is the second node
        return second

