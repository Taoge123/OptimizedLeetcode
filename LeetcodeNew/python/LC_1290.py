class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = head.val
        while head.next:
            res = res * 2 + head.next.val
            head = head.next
        return res


