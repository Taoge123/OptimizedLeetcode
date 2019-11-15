
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




