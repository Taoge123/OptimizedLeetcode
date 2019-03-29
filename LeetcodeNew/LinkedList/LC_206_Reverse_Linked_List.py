
"""
https://leetcode.com/problems/reverse-linked-list/discuss/140916/Python-Iterative-and-Recursive-(206)
https://leetcode.com/problems/reverse-linked-list/discuss/246827/Python-Iterative-and-Recursive

https://github.com/yuzhoujr/leetcode/issues/33


Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""

"""
Iterative:
设置一个Prev的参数方便之后的操作。

Step 1: 保存head reference
在While循环中，cur指针用来保留当前Head的位置，因为如果我们操作 head = head.next这一步并且没有对head的位置进行保留， 
我们会失去对head的reference，导致我们之后不能进行反转操作。

Step 2: 保存head.next的reference
head的reference存好以后，我们还需要保存head.next的reference，原因是我们如果对第一个node进行了反转操作，
node就指向我们之前定义好的prev上，而失去了对原先head.next这个位置的拥有权。

head.next这个reference，我们直接用head来保存即可，所以有了head = head.next这么一个操作。当然你要是想写的更加易懂，
你也可以直接新创建一个函数，取名next，然后指向next = head.next。

Step 3: 反转
万事俱备，可以对cur指针进行反转了，指向之前定义的prev。

Step 4: Reference转移
最后不要忘记移动prev到cur的位置，不然prev的位置永远不变
"""

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev


"""
Iterative(保持Head位置)
底下这种写法，保证了Head的位置不被移动，这种操作对于该题的定义毫无意义，
因为最终不需要head的reference，但如果API定义需要head的话，是个好的practice.
还有就是对prev和next两个指针的命名，提高了code的可读性。
"""

#Better approach
class Solution2:
    def reverseList(self, head):
        if not head: return None
        prev, cur = None, head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev


# Recursive
class Solution3:
    def reverseList(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        next_node = head.next  # head -> next_node
        next_node.next = head  # head <- next_node
        head.next = None  # [x] <- head <- next_node
        return new_head

"""
def reverseListRecu(self, ListNode):
    if not head or not head.next: return head
    node, head.next.next, head.next = reverseListRecu(head.next), head, None
    return node

"""


"""
Step 1: Base Case:
if not head or not head.next:
    return head

Base Case的返回条件是当head或者head.next为空，则开始返回

Step 2: Recurse到底
new_head = self.reverseList(head.next)
在做任何处理之前，我们需要不断的递归，直到触及到Base Case,。当我们移动到最后一个Node以后, 
将这个Node定义为我们新的head, 取名new_head. 我们从new_head开始重复性的往前更改指针的方向

Step 3: 返回并且更改指针方向
next_node = head.next    #        head -> next_node 
next_node.next = head    #        head <- next_node 
head.next = None         # [x] <- head <- next_node 

这里一定要注意了，我们每次往上返回的是new_head, 这个new_head指针指向的是最后的Node. 而我们再返回过程中实际操作的head，是在step2: 
Recurse到底这一步向下传递的head的指针, 不要搞混了 , 实在不懂，就把上面这个图画一下，走一遍

Follow up: Reverse Nodes in K-Group
利用上面这种保持Head位置的写法，可以直接将方程带入到这道题常问的Follow Up
也就是Leetcode 25的原题，代码也放在这

含义就是我们找到每次新的head的位置，然后通过我们这题写好的逻辑翻转即可。

"""


class SolutionReverseGroup:
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)




