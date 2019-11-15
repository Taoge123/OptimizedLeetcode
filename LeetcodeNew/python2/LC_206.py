
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



