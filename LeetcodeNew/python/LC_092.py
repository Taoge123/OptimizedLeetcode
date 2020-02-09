"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""


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


class Solution2:
    def __init__(self):
        self.left = None
        self.stop = False

    def reverseBetween(self, head, m, n):
        if not head:
            return None

        self.left, right = head, head
        self.stop = False

        self.recurseAndReverse(right, m, n)
        return head

    def recurseAndReverse(self, right, m, n):

        # base case. Don't proceed any further
        if n == 1:
            return

        # Keep moving the right pointer one step forward until (n == 1)
        right = right.next

        # Keep moving left pointer to the right until we reach the proper node
        # from where the reversal is to start.
        if m > 1:
            self.left = self.left.next

        # Recurse with m and n reduced.
        self.recurseAndReverse(right, m - 1, n - 1)

        # In case both the pointers cross each other or become equal, we
        # stop i.e. don't swap data any further. We are done reversing at this
        # point.
        if self.left == right or right.next == self.left:
            self.stop = True

        # Until the boolean stop is false, swap data between the two pointers
        if not self.stop:
            self.left.val, right.val = right.val, self.left.val

            # Move self.left one step to the right.
            # The right pointer moves one step back via backtracking.
            self.left = self.left.next




