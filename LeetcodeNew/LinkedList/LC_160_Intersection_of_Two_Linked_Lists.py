
"""
https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49838/5-line-python-solution

https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49938/Python-Solution%3A-O(n)-time-and-O(1)-space

https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/50010/My-concise-python-solution-run-in-O(n)-time-and-O(1)-memory

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B,
it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2
(note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
"""


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None


class Solution2:
    def getIntersectionNode(self, headA, headB):
        p, q = headA, headB;
        while p != q:
            p = p.next if p else headB;
            q = q.next if q else headA;
        return p


class Solution3:
    class Solution:
        # @param two ListNodes
        # @return the intersected ListNode
        def getIntersectionNode(self, headA, headB):
            if not headA or not headB: return None
            a, b = headA, headB
            ans = None
            while a or b:
                if not a:   a = headB
                if not b:   b = headA
                if a is b: return a  # and not ans: ans=a
                a, b = a.next, b.next
            # return ans






