
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""

class Solution1:
    def reorderList(self, head):
        if not head:
            return

        # find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half in-place
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next

        # Merge in-place; Note : the last node of "first" and "second" are the same
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        return


class SolutionCaikehe:
    def reorderList(self, head):
        if not head:
            return
        # ensure the first part has the same or one more node
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        p = slow.next
        slow.next = None
        node = None
        while p:
            nxt = p.next
            p.next = node
            node = p
            p = nxt
        # combine head part and node part
        p = head
        while node:
            tmp = node.next
            node.next = p.next
            p.next = node
            p = p.next.next  # p = node.next
            node = tmp


class Solution3:
    def reorderList(self, head):
        # find the middle of list
        # reverse the second half of list
        # insert one by one each element in 1st and 2nd halves.
        # runtime: 170ms
        if not head:
            return head

        pi = pj = head

        while pj.next and pj.next.next:  # j goes as twice as i.
            pi, pj = pi.next, pj.next.next

        cur = pi.next  # start from 2nd half.
        node = pi.next = None
        while cur:  # reverse 2nd half.
            next = cur.next
            cur.next = node
            node = cur
            cur = next

        cur1, cur2 = head, node
        while cur2:  # insert
            next1, next2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2


