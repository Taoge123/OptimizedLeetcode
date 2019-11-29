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
import random

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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



class SolutionFast:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        cur_node = self.head
        counter = 1
        choice = -1

        while not cur_node is None:
            if random.random() < 1 / counter:
                choice = cur_node.val
            cur_node = cur_node.next
            counter += 1
        return choice




