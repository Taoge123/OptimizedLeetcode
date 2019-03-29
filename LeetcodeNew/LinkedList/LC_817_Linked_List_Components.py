
"""
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.

Example 1:

Input:
head: 0->1->2->3
G = [0, 1, 3]
Output: 2
Explanation:
0 and 1 are connected, so [0, 1] and [3] are the two connected components.
Example 2:

Input:
head: 0->1->2->3->4
G = [0, 3, 1, 4]
Output: 2
Explanation:
0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
Note:

If N is the length of the linked list given by head, 1 <= N <= 10000.
The value of each node in the linked list will be in the range [0, N - 1].
1 <= G.length <= 10000.
G is a subset of all values in the linked list.
"""

"""
Take second example in the description:
liked list: 0->1->2->3->4
I highlighed the subset G in linked list with color red.
The problem is just to count how many red part there are.
One red part is one connected components.
To do this, we just need to count tails of red parts.
"""

class Solution:
    def numComponents(self, head, G):
        setG = set(G)
        res = 0
        while head:
            if head.val in setG and (head.next == None or head.next.val not in setG):
                res += 1
            head = head.next
        return res


class Solution2:
    def numComponents(self, head, G):
        seen = set(G)
        p = head
        res = len(G)
        while p:
            if p.next and p.val in seen and p.next.val in seen:
                res -= 1
            p = p.next
        return res


class Solution3:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        p, prev, count, G = head, False, 0, set(G)
        while p:
            if p.val in G and not prev:
                count += 1
            prev, p = p.val in G, p.next;

        return count






