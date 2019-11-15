

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head



