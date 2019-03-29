

"""
https://leetcode.com/problems/delete-node-in-a-linked-list/discuss/140910/Python-

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5,
the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1,
the linked list should become 4 -> 5 -> 9 after calling your function.
"""

"""
其实不能真正意义上的删除指定的Node，因为没有给与Previous Node。
所以从根本意义上，只能取巧的解决这个问题。题目刻意给了很多附件的条件，比如链表value没有重复，
并且指定Node不是Tail，其实都是在给正解做铺垫，代码如下


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


"""
我们真正删除的是指定Node的下一个Node，然后把指定Node的Value更改成下一个Node的值罢了。
为什么这个node.next.next在这里是没问题的，因为题目告诉了说指定的Node不为Tail，所以我们不用担心这个Edge Case。
"""





