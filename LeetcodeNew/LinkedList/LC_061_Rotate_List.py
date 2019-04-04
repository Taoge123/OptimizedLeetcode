
"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""

class SolutionCaikehe:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        k %= l
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        ret = slow.next
        fast.next = head
        slow.next = None
        return ret


class Solution2:
    class Solution(object):
        def rotateRight(self, head, k):
            if not head:
                return None

            if head.next == None:
                return head

            pointer = head
            length = 1

            while pointer.next:
                pointer = pointer.next
                length += 1

            rotateTimes = k % length

            if k == 0 or rotateTimes == 0:
                return head

            fastPointer = head
            slowPointer = head

            for a in range(rotateTimes):
                fastPointer = fastPointer.next

            while fastPointer.next:
                slowPointer = slowPointer.next
                fastPointer = fastPointer.next

            temp = slowPointer.next

            slowPointer.next = None
            fastPointer.next = head
            head = temp

            return head


class Solution3:
    def rotateRight(self, head, k):
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1

        if not n or not k % n:
            return head

        tail = head
        for _ in range(n - k % n - 1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head
        return next

class Solution4:
    def rotateRight(head, k):
        if not head:
            return None

        curr, count = head, 1
        while curr.next:  # find the end of list and count the length
            curr = curr.next
            count += 1
        curr.next = head  # make cycle

        for _ in range(count - (k % count)):
            curr = curr.next  # move to pointer (count-k) times
            # mod is used in case k is greater than length
        prev = curr  # the next node is the new head
        curr = curr.next
        prev.next = None  # cut the cycle, this is the end of the new list
        return curr


