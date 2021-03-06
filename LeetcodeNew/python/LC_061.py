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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        size = 0
        root = head
        while head:
            size += 1
            head = head.next
        k %= size
        if k == 0:
            return root

        fast, slow = root, root
        while k - 1:
            fast = fast.next
            k -= 1
        pre = slow

        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = None
        fast.next = root
        return slow



class SolutionTony:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        curr = head
        count = 1
        while curr and curr.next:
            count += 1
            curr = curr.next
        curr.next = head

        k = k % count
        flag = count - k

        prev = dummy
        cur = head
        for i in range(flag):
            prev = prev.next
            cur = cur.next
        prev.next = None
        return cur




class Solution2:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        oldTail = head
        n = 1
        while oldTail.next:
            oldTail = oldTail.next
            n += 1
        oldTail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        newTail = head
        for i in range(n - k % n - 1):
            newTail = newTail.next
        newHead = newTail.next

        # break the ring
        newTail.next = None

        return newHead



