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
    def swapPairs(self, head):
        dummy = cur = ListNode(0)
        dummy.next = head

        while head and head.next:
            temp = head.next.next
            cur.next = head.next
            cur.next.next = head
            head.next = temp
            cur = head
            head = temp

        return dummy.next


