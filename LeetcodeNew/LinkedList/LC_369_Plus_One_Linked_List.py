
"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def plusOne(self, head):

        start = None

        node = head
        while node:
            if node.val < 9:
                start = node
            node = node.next

        if start:
            start.val += 1
            node = start.next
        else:
            new = ListNode(1)
            new.next = head
            node = head
            head = new

        while node:
            node.val = 0
            node = node.next

        return head


class Solution2:
    def plusOne(self, head):
        def add(head):
            if not head:
                return 1
            head.val += add(head.next)
            carry, head.val = divmod(head.val, 10)
            return carry

        carry = add(head)
        if carry and head:
            addc = ListNode(1)
            addc.next = head
            head = addc
        return head









