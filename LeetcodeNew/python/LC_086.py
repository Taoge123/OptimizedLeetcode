"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):

        small = leftList = ListNode(0)
        big = rightList = ListNode(0)

        while head:

            if head.val < x:
                leftList.next = ListNode(head.val)
                leftList = leftList.next
            else:
                rightList.next = ListNode(head.val)
                rightList = rightList.next

            head = head.next
        leftList.next = big.next
        return small.next




