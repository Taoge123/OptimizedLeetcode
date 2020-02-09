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


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            # Nodes to be swapped
            first = head;
            second = head.next;

            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # Reinitializing the head and prev for next swap
            prev = first
            head = first.next

        # Return the new head node.
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

