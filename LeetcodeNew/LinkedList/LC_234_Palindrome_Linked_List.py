
"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""


class Solution:
    def isPalindrome(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


class Solution1:
    def isPalindrome(self, head):
        fast = middle = head
        reverse = None

        # find the middle node and reverse node before middle
        while fast and fast.next:
            fast = fast.next.next
            current, middle = middle, middle.next
            current.next, reverse = reverse, current

        if fast:  # mean list has odd count nodes, need change to next.
            middle = middle.next

        # check the reverse equal the middle
        while reverse:
            if reverse.val != middle.val:
                return False
            reverse = reverse.next
            middle = middle.next

        return True






