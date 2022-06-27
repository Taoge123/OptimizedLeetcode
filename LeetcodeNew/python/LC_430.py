
"""
You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL


Explanation for the above example:

Given the following multilevel doubly linked list:




We should return the following flattened doubly linked list:

h + dfs(h.child) + dfs(h.next)
   要的是末尾

"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



class SolutionTony:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node:
            if node.child:
                right = node.next
                node.next = self.flatten(node.child)
                # whoever is the next, set the prev as the current node, recursion will find the node.next
                node.next.prev = node
                node.child = None
                # current node will keep going to all the way end then we connect the last layer
                while node.next:
                    node = node.next
                # connect to last layer
                if right:
                    node.next = right
                    right.prev = node
            node = node.next
        return head



class SolutionWisdom:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        self.dfs(head)
        return head

    def dfs(self, node):
        child = node.child
        nxt = node.next
        node.child = None

        if child and nxt:
            childEnd = self.dfs(child)
            nextEnd = self.dfs(nxt)

            node.next = child
            child.prev = node

            childEnd.next = nxt
            nxt.prev = childEnd
            return nextEnd

        elif not child and nxt:
            nextEnd = self.dfs(nxt)
            return nextEnd

        elif child and not nxt:
            childEnd = self.dfs(child)
            node.next = child
            child.prev = node
            return childEnd
        else:
            return node


class Solution:
    def flatten(self, head):
        if not head:
            return

        dummy = Node(0,None,head,None)
        stack = []
        stack.append(head)
        prev = dummy

        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root

            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root

        dummy.next.prev = None
        return dummy.next








