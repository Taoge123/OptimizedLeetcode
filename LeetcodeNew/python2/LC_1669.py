
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        prea, postb = None, None
        cur = ListNode(-1)
        cur.next = list1
        dummy = cur

        for i in range( b +1):
            if i == a:
                prea = cur
            cur = cur.next
        postb = cur.next

        prea.next = list2
        while list2.next:
            list2 = list2.next

        list2.next = postb
        return dummy.next


