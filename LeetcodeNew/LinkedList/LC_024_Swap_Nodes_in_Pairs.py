
"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionCaikehe:
    # iteratively
    def swapPairs1(self, head):
        if not head or not head.next:
            return head
        second = head.next
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second

    # recursively
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return second


class Solution2:
    def swapPairs(self, head):
        dummy = cur = ListNode(-1)
        dummy.next = head

        while cur.next and cur.next.next:
            p1, p2 = cur.next, cur.next.next
            cur.next, p1.next, p2.next = p2, p2.next, p1
            cur = cur.next.next
        return dummy.next

"""
这题为什么普遍都用Dummynode?

Head的位置可能会变，比如 1 > 2 > Null , 之后会返回 2 > 1 > Null, head的位置从1变成了2
这里Dummynode也充当了prev这个指针，如果不用dummynode，也需要创建一个temp指针保存prev的值
"""


class Solution:
    def swapPairs(self, head):
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy

        while cur.next and cur.next.next:
            first = cur.next
            sec = cur.next.next
            cur.next = sec
            first.next = sec.next
            sec.next = first
            cur = cur.next.next
        return dummy.next




