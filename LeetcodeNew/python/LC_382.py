"""
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();

"""
"""
[a, b, c, d]
x = a
x = 50% x, 50%b => 50%a, 50%b
x = 2/3 x, 1/3 c => 1/3 a, 1/3 b, 1/3 c
x = 3/4 x, 1/4 d => 1/4a, 1/4b, 1/4c, 1/4d



"""





import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionFast:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        node = self.head
        counter = 1
        res = -1

        while node:
            if random.random() < 1 / counter:
                res = node.val
            node = node.next
            counter += 1
        return res


class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = self.head
        node = self.head.next
        index = 1

        while node:
            if random.randint(0, index) is 0:
                res = node
            node = node.next
            index += 1
        return res.val








