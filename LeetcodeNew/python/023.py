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



