"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/159067/Python-Recursive-Solution-%2B-Analysis

You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level,
doubly linked list. You are given the head of the first level of the list.



Example:

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL



Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

The algorithm only requires O(1) extra space on the heap,
BUT in the worst case, it requires O(n) extra space on the stack,
as we could need to put the entire list on.

The amount of space required is dependent on:

The length of the longest stretch of nodes that only have child or next pointers.
The percentage of nodes which have both a child and a next pointer on them
(the higher the percentage, the better the performance,
because we have nearer to a balanced tree structure).
Due to this structure being equivalent to a
(rather stringy in a lot of cases I suspect) binary tree,
I'm pretty sure it's impossible to write an iterative algorithm that uses O(1) space.
The stack/ queue you use to keep track of the work still
to do could potentially grow to O(n) in the worst case,
and like I said, this worst case is probably common.

The time complexity is O(n) . We handle each node once.
It is impossible to do better than O(n) time,
because we need to actually check the child and next pointers of every node,
otherwise we could miss some parts of the structure out!
"""

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        if not head:
            return

        dummy = Node(0 ,None ,head ,None)
        stack = [head]
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



class Solution2:
    def flatten(self, head):
        # Initialize the current reference and stack of saved next pointers
        curr, tempStack = head, []
        while curr:
            if curr.child:
                # If the current node is a parent
                if curr.next:
                    # Save the current node's old next pointer for future reattachment
                    tempStack.append(curr.next)
                # Current <-> Current.child
                #   \-> None
                curr.next, curr.child.prev, curr.child = curr.child, curr, None;
            if not curr.next and len(tempStack):
                # If the current node is a child without a next pointer
                temp = tempStack.pop()
                # Current <-> Temp
                temp.prev, curr.next = curr, temp
            curr = curr.next
        return head


class Solution3:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.recursively_flatten(head)
        return head

    # Takes the head of the list to be flattened, and returns the tail of the flattened list.
    def recursively_flatten(self, head):

        # Could happen if outer caller passes in an empty list.
        if head == None:
            return None

        # Base case - there is nothing left to flatten.
        if head.next == None and head.child == None:
            return head

        # Recursive case - we need to flatten the child and the tail.
        tail = head.next  # We need to store this as doing child first.
        current_end = head  # Where will we be attaching next?

        if head.child != None:
            child_end = self.recursively_flatten(head.child)
            self.link(current_end, head.child)
            current_end = child_end
            head.child = None

        if tail != None:
            tail_end = self.recursively_flatten(tail)
            self.link(current_end, tail)
            current_end = tail_end

        return current_end

    def link(self, node_1, node_2):
        node_1.next = node_2
        node_2.prev = node_1






