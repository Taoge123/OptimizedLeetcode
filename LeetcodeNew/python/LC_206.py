"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SolutionTony:
    def reverseList(self, head):
        return self.reverse(head, None)

    def reverse(self, node, prev):
        if not node:
            return prev

        nxt = node.next
        node.next = prev
        return self.reverse(nxt, node)


class SolutionPostOrder:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return prev


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            newNode = curr.next
            curr.next = prev
            prev = curr
            curr = newNode

        return prev



