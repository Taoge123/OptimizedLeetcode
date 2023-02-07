"""
https://leetcode.com/problems/reverse-linked-list-ii/solutions/1777686/python3-recursive-solution/

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


class SolutionTony:
    def __init__(self):
        self.successor = None

    def reverseBetween(self, head, left, right):
        if left == 1:
            return self.reverseN(head, right)

        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        if n == 1:
            self.successor = head.next
            return head

        last_node = self.reverseN(head.next, n - 1)
        # print(head.val, head.next.val, head.next.next.val, last_node.val, self.successor.val)
        head.next.next = head
        head.next = self.successor
        return last_node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

a = SolutionTony()
print(a.reverseBetween(head, 2, 4))



class SolutionRika:  # non-recurisive
    def reverseBetween(self, head, left: int, right: int):

        dummyhead = ListNode(None)
        dummyhead.next = head

        prev, cur = dummyhead, head

        for i in range(left):
            prevFrozen = prev  # at node 1
            curFrozen = cur  # at node 2
            prev = prev.next  # at node 2
            cur = cur.next  # at node 3

        for i in range(right - left):
            nxt = cur.next
            cur.next = prev
            prev = cur  # at position node 4
            cur = nxt  # at position node 5

        prevFrozen.next = prev  # make 1 point to 4
        curFrozen.next = cur  # make 2 point to 5

        return dummyhead.next


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

