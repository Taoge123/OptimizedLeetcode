
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        currA, currB = headA, headB
        lenA = lenB = 0
        while currA is not None:
            lenA += 1
            currA = currA.next

        while currB is not None:
            lenB += 1
            currB = currB.next

        currA, currB = headA, headB

        if lenA > lenB:
            for i in range(lenA - lenB):
                currA = currA.next
        else:
            for i in range(lenB - lenA):
                currB = currB.next

        while currB != currA:
            currA = currA.next
            currB = currB.next

        return currA


