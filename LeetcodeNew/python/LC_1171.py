
"""
The story is that,
I wrote the really concise solution,
it got accepted but actully it's wrong.
I fixed it by adding another while loop.
That is the Solution 1.

If we don't insist on one pass,
we can find the two passes is actually really neat.

That turned back to the intuition that I mentioned:
Assume the input is an array.
How will you solve the problem?

Iterate for the first time,
calculate the prefix sum,
and save the it to seen[prefix]

Iterate for the second time,
calculate the prefix sum,
and directly skip to last occurrence of this prefix
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        dummy = ListNode(0)
        dummy.next = head
        visited = {0: dummy}
        while head:
            prefix += head.val
            visited[prefix] = head
            head = head.next

        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            #jump to the last occurence of this prefix means the sum of nums in between is 0
            head.next = visited[prefix].next
            head = head.next
        return dummy.next



