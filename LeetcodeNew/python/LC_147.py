
"""
Given 1 -> 3 -> 2 -> 4 - > null

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
               |    |
              ptr toInsert
-- locate ptr = 3 by (ptr.val > ptr.next.val)
-- locate toInsert = ptr.next

dummy0 -> 1 -> 3 -> 2 -> 4 - > null
          |         |
   toInsertPre     toInsert
-- locate preInsert = 1 by preInsert.next.val > toInsert.val
-- insert toInsert between preInsert and preInsert.next

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionAlan:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = dummy.next = head

        while curr and curr.next:
            if curr.val < curr.next.val:
                curr = curr.next
                continue

            pre = dummy
            node_to_move = curr.next
            while pre.next.val < node_to_move.val:
                pre = pre.next

            # insert between pre and pre.next
            curr.next = node_to_move.next
            tmp = pre.next
            pre.next = node_to_move
            node_to_move.next = tmp

        return dummy.next




class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next =  head
        while head and head.next:
            if head.val > head.next.val:
                # Locate newNode.
                newNode = head.next
                # pre will traverse all the way to before head,
                pre = dummy
                while pre.next.val < newNode.val:
                    pre = pre.next

                head.next = newNode.next
                # Insert nodeToInsert between pre and pre.next.
                newNode.next = pre.next
                pre.next = newNode
            else:
                head = head.next
        return dummy.next

"""
        1  ->  5  ->  4  ->  2  ->  3
dummy        head   
                    newNode
       pre
        1  ->  4  ->  5  ->  2  ->  3
                     head
       pre
"""


class Solution2:
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            # lazy operation, p only move back to dummy when it greater than current value
            if p.next.val > val:
                p = dummy

            while p.next.val < val:
                p = p.next

            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new

        return dummy.next




