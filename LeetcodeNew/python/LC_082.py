
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next


class Solution2:
    def deleteDuplicates(self, head):
        pre = dummy = ListNode(0)  # construct a dummy node
        dummy.next = head
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                # this will be verified by next line
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next













