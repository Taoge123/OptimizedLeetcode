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
                #We will need the position i to avoid the duplicates, otherwise heapq will fail
                heapq.heappush(queue, (item.val, i, item))

        while queue:
            pos, node = heapq.heappop(queue)[1:]
            curr.next = node
            curr = curr.next
            if node.next:
                #pos, same as i, is which list from lists
                heapq.heappush(queue, (node.next.val, pos, node.next))

        return dummy.next




list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(4)
list2.next = ListNode(5)
list2.next.next = ListNode(6)
list3 = ListNode(7)
list3.next = ListNode(8)

lists = []
lists.append(list1)
lists.append(list2)
lists.append(list3)

a = Solution()
print(a.mergeKLists(lists))
