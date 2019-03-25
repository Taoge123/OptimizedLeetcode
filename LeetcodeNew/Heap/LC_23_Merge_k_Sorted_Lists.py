"""

https://leetcode.com/problems/merge-k-sorted-lists/solution/

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
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:
输入: [1->4->5,1->3->4,2->6]
输出: 1->1->2->3->4->4->5->6

思路分析：
要将k个链表合并成一个有序链表，直接一点思考那就是每次都看k个链表的头部节点谁最小，就把最小的节点加入结果中。
当然，把最小的点加入后，指针需向后移动，将下一个节点和剩下k-1个节点继续比较。

这样每次都要从k个元素中找最小的值，最小堆正好完美契合我们的需求。
用(node.val, node)作为堆中的元素，这样就可以按照node.val进行排序了，堆顶元素保证是值最小的节点。
"""

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for l in lists:
            if not l: continue
            heapq.heappush(heap, (l.val, l))

        L = ret = ListNode(0)
        while heap:
            val, p = heapq.heappop(heap)
            L.next = p
            L = L.next
            if p.next:
                heapq.heappush(heap, (p.next.val, p.next))
        return ret.next

"""
既然题目让我们分析一下复杂度，那我们就来看一下，对于每个结点，都只进行了一次进堆和出堆操作。
所以时间复杂度为O(num)，num表示k个链表中所有节点的数量.
"""

class SolutionBruteForce:
    def mergeKLists(self, lists):

        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


class Solution3:
    def mergeKLists(self, lists):
        q, heap = len(lists), []
        for i in range(q):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        rhead = rtail = ListNode(0)

        while heap:
            i, n = heapq.heappop(heap)[1:]
            rtail.next = n
            rtail = rtail.next
            if n.next:
                heapq.heappush(heap, (n.next.val, i, n.next))

        return rhead.next
