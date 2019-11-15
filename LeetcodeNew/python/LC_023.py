"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):

        queue = []
        dummy = curr = ListNode(0)

        for i, item in enumerate(lists):
            if item:
                heapq.heappush(queue, (item.val, i, item))

        while queue:
            pos, node = heapq.heappop(queue)[1:]
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(queue, (node.next.val, pos, node.next))

        return dummy.next



