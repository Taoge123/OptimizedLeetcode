
"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

"""
temp = head.next
head.next = ListNode(v)
head.next.next  = temp
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        x1, x2 = 0, 0
        while l1:
            x1, l1 = x1 * 10 + l1.val, l1.next
        while l2:
            x2, l2 = x2 * 10 + l2.val, l2.next
        x = x1 + x2
        head = ListNode(0)
        while x:
            x, v = divmod(x, 10)
            head.next, head.next.next = ListNode(v), head.next
        return head.next or head



class Solution2:
    def addTwoNumbers(self, l1, l2):
        if not l1.val:
            return l2
        if not l2.val:
            return l1

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        head, val = ListNode(0), 0
        while stack1 or stack2:
            if stack1 and stack2:
                val = stack1.pop() + stack2.pop() + head.val
            else:
                n = max(stack1, stack2)  # None is smaller than anything
                val = n.pop() + head.val

            node = ListNode(val // 10)
            head.val = val % 10
            node.next = head
            head = node

        if head.val == 0:
            head = head.next
        return head



l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)

l2 = ListNode(6)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

a = Solution()
print(a.addTwoNumbers(l1, l2))




