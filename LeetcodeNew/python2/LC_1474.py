
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(None)
        first = dummy
        second = head
        step = 0
        while second:
            if step % ( m +n) < m:
                first.next = second
                first = first.next
            else:
                first.next = None
            second = second.next
            step += 1
        return dummy.next





