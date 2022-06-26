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
        # Edge
        if m == n:
            return head
        if not head or not m or not n:
            return None
        # Set starting point
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        for i in range(m - 1):
            start = start.next
        # Set ending point
        end = cur = start.next
        prev = None
        # reverse
        for i in range(n - m + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # Connect
        start.next = prev
        end.next = cur
        return dummy.next

"""
m = 2
n = 4
       1 -> 2 -> 3 -> 4 -> 5
dummy   
     start
           end 
           cur 
prev = None
       1   2 <- 3 <- 4 -> 5
dummy
    start
           end   
                    prev      
                          cur
                           
"""



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


class Solution3:
    def __init__(self):
        self.successor = None

    def reverseBetween(self, head, left: int, right: int):
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, num):
        if num == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, num - 1)
        head.next.next = head
        head.next = self.successor
        return last

