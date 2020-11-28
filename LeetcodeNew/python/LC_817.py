
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, G) -> int:
        G = set(G)
        res = 0

        while head:
            if head.val in G and (head.next == None or head.next.val not in G):
                res += 1
            head = head.next

        return res
