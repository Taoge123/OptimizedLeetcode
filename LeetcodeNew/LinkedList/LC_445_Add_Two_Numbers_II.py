
"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        x1, x2 = 0, 0
        while l1:
            x1, l1 = x1 * 10 + l1.val, l1.next
        while l2:
            x2, l2 = x2 * 10 + l2.val, l2.next
        x = x1 + x2
        head = ListNode(0)
        while x:
            x, v = divmod(x, 10)
            head.next, head.next.next = ListNode(v), head.next
        return head.next or head


class Solution2:
    def addTwoNumbers(self, l1, l2):

        # turn the lists in to ints with simple loops. In case you didn't know, you can put
        # multiple statements on the same line if you use semicolons in Python.
        s1 = 0
        s2 = 0
        while l1: s1 *= 10; s1 += l1.val; l1 = l1.next
        while l2: s2 *= 10; s2 += l2.val; l2 = l2.next

        # take the sum and reconstruct the number from tail to head, because it's easier
        # to isolate and chop off the little digits with modulus and division.
        s3 = s1 + s2
        tail = None
        head = None
        while s3 > 0: head = ListNode(s3 % 10); head.next = tail; tail = head; s3 /= 10
        return head if head else ListNode(0)







