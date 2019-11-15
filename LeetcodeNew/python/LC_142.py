
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):


        slow = fast = dummy = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while dummy != slow:
            slow = slow.next
            dummy = dummy.next

        return dummy

