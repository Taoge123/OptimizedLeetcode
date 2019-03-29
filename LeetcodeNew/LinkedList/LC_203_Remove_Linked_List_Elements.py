
"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):

        dummy = ListNode(-1)
        dummy.next = head
        pointer = dummy

        while (pointer.next):

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return dummy.next


class Solution2:

    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

        return dummy.next



class Solution3:
    def removeElements(self, head, val):
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
    
