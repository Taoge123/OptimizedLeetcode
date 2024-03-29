"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
Accepted
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next


# LC 206 Reverse Linked List
class SolutionBase:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

# Follow up: Please reverse the list into K Group

class Solution3:
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    #prev 是这一轮开头, curr是下一轮开头
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)


class SolutionAlan:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = tail = ListNode(0)
        dummy.next = head
        for _ in range(k):
            tail = tail.next
            if not tail:
                return dummy.next

        # reverse k nodes
        next_head = tail.next
        new_head = self.reverse_k_nodes(head, k)

        # recursive
        head.next = self.reverseKGroup(next_head, k)

        return new_head

    def reverse_k_nodes(self, head, k):
        curr = head
        prev = None

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev




class Solution4:
    def reverseKGroup(self, head, k):
        length, node = 0, head
        while node:
            length += 1
            node = node.next
        #corner case checking, if length < k, then no reverse need
        if k <= 1 or length < k:
            return head
        pre, cur = None, head
        for _ in range(k):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return pre

"""
     1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
pre cur nxt
    pre cur   nxt
        pre   cur  nxt
               3 -> 4 -> 5 -> 6 -> 7 -> 8
        pre is the final new head
              cur became the new start
"""


