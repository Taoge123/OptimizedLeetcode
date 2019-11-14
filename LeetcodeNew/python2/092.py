
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m-1):
            pre = pre.next
        cur= pre.next
        # reverse the defined part
        node = None
        for _ in range(n-m+1):
            nxt = cur.next
            cur.next = node
            node = cur
            cur= nxt
        # connect three parts
        pre.next.next = cur
        pre.next = node
        return dummy.next



