
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # revese the second hald in-place
        pre, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # Merge in-place
        first, second = head, pre
        while second.next:
            #             first.next, first = second, first.next
            #             second.next, second = first, second.next

            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

        return





class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # revese the second hald in-place
        pre, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # Merge in-place
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return

"""
   1 -> 2 -> 3 -> 4 -> 5
            slow      
                     fast
       pre  cur  nxt 
   1 -> 2 <- 3 <- 4 <- 5
                      pre 
 first               second
       first     second
   1 -> 5 -> 2 -> 4 -> 3
                         
"""






