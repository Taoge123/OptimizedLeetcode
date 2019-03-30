
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

class SolutionLee:
    def deleteDuplicates(self, head):
        if head and head.next:
            head.next = self.deleteDuplicates(head.next)
            return head.next if head.next.val == head.val else head
        return head

class Solution:
    def deleteDuplicates(self, head):
        if head and head.next and head.val == head.next.val:
            head = self.deleteDuplicates(head.next)
        elif head and head.next:
            head.next = self.deleteDuplicates(head.next)
        return head

class Solution1:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next  # skip duplicated node
            cur = cur.next  # not duplicate of current node, move to next node
        return head


class Solution2:
    def deleteDuplicates(self, head):
        if head is None:
            return head
        curr = head
        while curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

