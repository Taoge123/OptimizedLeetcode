"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
下面这种方法比较巧妙了，思路是遍历链表，找到右起第一个不为9的数字，如果找不到这样的数字，说明所有数字均为9，那么在表头新建一个值为0的新节点，进行加1处理，然后把右边所有的数字都置为0即可。举例来说：

比如1->2->3，那么第一个不为9的数字为3，对3进行加1，变成4，右边没有节点了，所以不做处理，返回1->2->4。

再比如说8->9->9，找第一个不为9的数字为8，进行加1处理变成了9，然后把后面的数字都置0，得到结果9->0->0。

再来看9->9->9的情况，找不到不为9的数字，那么再前面新建一个值为0的节点，进行加1处理变成了1，把后面的数字都置0，得到1->0->0->0。
"""


class Solution1:
    def plusOne(self, head: ListNode) -> ListNode:
        head = self.reverse(head)
        carry = 1

        curr = head
        while curr:
            val = curr.val + carry
            if val > 9:
                carry = 1
                val %= 10
            else:
                carry = 0

            curr.val = val
            curr = curr.next

        head = self.reverse(head)

        if carry:
            newNode = ListNode(carry)
            newNode.next = head
            head = newNode
        return head



class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        start = None
        node = head
        while node:
            if node.val < 9:
                start = node
            node = node.next

        if start:
            start.val += 1
            node = start.next
        else:
            newNode = ListNode(1)
            newNode.next = head
            node = head
            head = newNode

        while node:
            node.val = 0
            node = node.next
        return head






