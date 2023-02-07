"""
https://leetcode.com/problems/reverse-linked-list-ii/solutions/1725319/recursive-method-07/

https://www.youtube.com/watch?v=iT1YrvSNtlw

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


# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
#
# a = SolutionTony()
# print(a.reverseList(head))

class SolutionPostOrder:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        # head is 4, last_node is 5
        last_node = self.reverseList(head.next)
        print(last_node.val, head.val, head.next.val, head.next.next)
        # head.next so far is 5, head.next.next means 5 point to 4
        head.next.next = head
        head.next = None
        return last_node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

a = SolutionPostOrder()
print(a.reverseList(head))

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



