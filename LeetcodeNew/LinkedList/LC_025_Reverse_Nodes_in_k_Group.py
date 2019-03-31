"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
"""
Use a dummy head, and

l, r : define reversing range

pre, cur : used in reversing, standard reverse linked linked list method

jump : used to connect last node in previous k-group to first node in following k-group
"""
"""
k = 3 for example:

step 0: a -> b -> c -> (next k-group)

step 1:      b -> c -> (next k-group)
                  a ---^

step 2:           c -> (next k-group)
             b -> a ---^

step 3:                (next k-group)
        c -> b -> a ---^

finish: c -> b -> a -> (next k-group)

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseKGroup(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:  # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next


"""
This problem is a standard follow up to
LC 206 Reverse Linked List

A lot of the solutions implemented the reversing logic from scratch
I am going to pretend that I just finish writing the standard reverse method, and reuse the method on the follow up.

LC 206 Reverse Linked List
"""


class SolutionGJ1:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        prev, cur, nxt = None, head, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

# Follow up: Please reverse the list into K Group
class SolutionGJ2:
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)


class SolutionCaikehe:
    # Recursively
    def reverseKGroup(self, head, k):
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in xrange(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node

    # Iteratively
    def reverseKGroup(self, head, k):
        if not head or not head.next or k <= 1:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        if k > l:
            return head
        dummy = pre = ListNode(0)
        dummy.next = head
        # totally l//k groups
        for i in range(l // k):
            # reverse each group
            node = None
            for j in range(k - 1):
                nxt = head.next
                head.next = node
                node = head
                head = nxt
            # update nodes and connect nodes
            tmp = head.next
            head.next = node
            pre.next.next = tmp
            tmp1 = pre.next
            pre.next = head
            head = tmp
            pre = tmp1
        return dummy.next



# pre alway point the last one in previous KGoup.
# Constant insert cur kGroup's node after it.
class SolutionLast:
    def reverseKGroup(self, head, k):
        pre, pre.next = self, head
        while self.needReverse(head, k):
            tail = head  # 1st one in cur KGroup
            for _ in range(k):
                pre.next, head.next, head = head, pre.next, head.next
            pre = tail  # now, it become the last one in previous KGroup
        pre.next = head  # maybe there are some rest node.
        return self.next

    def needReverse(self, head, k):
        while head and k:
            k -= 1
            head = head.next
        return k == 0