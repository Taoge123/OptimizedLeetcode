class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionTony:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = ListNode(-1)
        fast = ListNode(-1)
        slow.next = fast.next = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:
            return slow.next
        return slow


