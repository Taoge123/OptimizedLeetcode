class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        front = back = cur = head
        count = 0

        # find the count of the LL and
        # point 'front' ptr to the kth node from beginning
        # in the first pass
        while cur:
            count += 1
            if count == k:
                front = cur
            cur = cur.next

        # point 'back' ptr to the kth node from end
        # in the second pass
        while back:
            if count == k:
                break
            count -= 1
            back = back.next

        # exchange node values
        front.val, back.val = back.val, front.val
        return head

